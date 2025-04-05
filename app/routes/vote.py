from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from httpx import delete
from .. import schemas, database, model, oauth2
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/vote",
    tags=['Vote']
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db), current_user = Depends(oauth2.get_current_user)):

    post = db.query(model.Post).filter(model.Post.id == vote.post_id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post {vote.post_id} not found")
    
    votes_query = db.query(model.Votes).filter(model.Votes.posts_id == vote.post_id, model.Votes.users_id == current_user.id)

    found_vote = votes_query.first()

    if(vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"user {current_user.id}, has already voted on the post{vote.post_id}")
        
        new_vote = model.Votes(posts_id=vote.post_id, users_id=current_user.id)
        db.add(new_vote)
        db.commit()

        return {"message": "successful vote"}
    
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Vote doesn't exist")
        votes_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "Vote deleted successfully"}
        

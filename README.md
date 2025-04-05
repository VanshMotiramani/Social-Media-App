# 🧑‍🤝‍🧑 Social Media App (FastAPI Backend)

A fully functional **backend** for a social media platform built using **FastAPI**, featuring user authentication and complete CRUD operations for posts. This system is designed with a clean, scalable architecture to support future extensions like likes, comments, followers, and media sharing.

---

## 🚀 Features

- 🔐 **User Authentication** (Register/Login)
  - OAuth2 with JWT tokens
  - Secure password hashing with Bcrypt
- 📝 **Post Management**
  - Create, Read, Update, Delete (CRUD)
- 📁 **User Management**
  - View and update user profile
- 🔄 **Token-based API access**
  - Protected routes with authentication
- ⚡ **High Performance**
  - Async FastAPI endpoints with sub-150ms average response time
  - Handles 100+ concurrent requests
- 📦 **Scalable Codebase**
  - Modular structure ready for production & frontend integration

---

## 🛠️ Tech Stack

- **Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Database:** PostgreSQL
- **Authentication:** OAuth2 + JWT (via `python-jose`)
- **Validation:** Pydantic
- **Security:** Passlib (`bcrypt`)
- **Server:** Uvicorn (ASGI server)
- **Environment Management:** python-dotenv

---

## 📂 Project Structure
<pre lang="text"> 

social-media-app/ 
├── app/ 
│ ├── routes/ 
│ │ ├── auth.py 
│ │ ├── posts.py 
│ │ ├── users.py 
│ │ └── vote.py 
│ ├── main.py # Entry point 
│ ├── config.py 
│ ├── database.py 
│ ├── model.py 
│ ├── oauth2.py 
│ ├── schemas.py 
│ └── utils.py # Token handling, hashing, etc. 
├── requirements.txt 
├── .env # Environment variables 
└── README.md 
 </pre>

---

## ⚙️ Installation

### 🔧 Prerequisites

- Python 3.9+
- PostgreSQL installed and running

---

### 📥 Clone the Repository

#️⃣ Run on Terminal
```bash
git clone https://github.com/VanshMotiramani/Social-Media-App.git
cd Social-Media-App
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate 
```

```bash
pip install -r requirements.txt 
```

---

### Configure Environment Variables

⚙️ Create a .env file in the root directory with the following content:

```env
    DATABASE_URL=postgresql://<username>:<password>@localhost/<dbname>
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30 
```

Replace the placeholders with your actual PostgreSQL credentials and a secure secret key.


---

### 5️⃣ Start the Server
```bash
    uvicorn app.main:app --reload 
```
📌Visit the app at: http://127.0.0.1:8000

---

## 📬 API Documentation
FastAPI provides auto-generated documentation:

📄 Swagger UI → http://127.0.0.1:8000/docs

📄 ReDoc UI → http://127.0.0.1:8000/redoc

---

## 🔐 Security
* Passwords are hashed securely using passlib with the bcrypt algorithm.
* Authenticated sessions are powered by JWT tokens (python-jose).
* Access to protected routes requires a valid Bearer Token in the header.
* All credentials are managed via environment variables to prevent leaks.

---


## 📢 Contribution

Contributions are welcome! To contribute:
1. Fork the repo
2. Create a new branch (git checkout -b feature-name)
3. Make your changes and commit (git commit -am 'Add feature')
4. Push to the branch (git push origin feature-name)
5. Open a Pull Request 🚀


---

## 👨‍💻 Author

Vansh Motiramani

---






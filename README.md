# 🔐 Password Generator

This is a secure and user-friendly **Password Generator** web app built with Flask. It allows users to register, log in, generate strong passwords, and store them securely for easy access.

## 🚀 Features

- ✅ User registration and login with hashed passwords  
- ✅ Secure password generation with customizable options  
- ✅ Store and view saved passwords in a personal dashboard  
- ✅ Show/hide password functionality for security  
- ✅ Flash messages for user feedback  

## 🛠️ Tech Stack

- 🌐 **Frontend**: HTML (Jinja2 templates), CSS  
- 🐍 **Backend**: Python with Flask  
- 🗃️ **Database**: SQLite using SQLAlchemy ORM  
- 🔐 **Security**: Password hashing with Werkzeug  

📦 Installation & Setup

### 1. Clone the Repository

git clone https://github.com/vaishnavijatala/Password_Genrator.git
cd Password_Genrator


### 2. Create a Virtual Environment (Windows)
python -m venv venv
venv\Scripts\activate

### 3.Install Dependencies
pip install -r requirements.txt

### 4.Run the Application
python app.py

📁 Project Structure
📦 Password_Genrator/
├── 📄 app.py                  # Main Flask app
├── 📄 config.py               # Configuration settings
├── 📄 models.py               # SQLAlchemy models for User and SavedPassword
├── 📄 password_utils.py       # Password generation logic
├── 📄 requirements.txt        # Python dependencies
├── 📁 templates/              # HTML templates (Jinja2)
│   ├── 📄 login.html
│   ├── 📄 signup.html
│   ├── 📄 dashboard.html
│   └── 📄 generate.html



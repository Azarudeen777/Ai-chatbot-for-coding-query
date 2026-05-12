<div align="center">

<h1>DevBot</h1>

<p>
AI-Powered Coding Assistant built with Python, Streamlit, Gemini AI, and MySQL
</p>

</div>

<hr>

<h2>Overview</h2>

<p>
DevBot is a secure AI-powered coding assistant developed using Python and Streamlit.
The application allows users to register, log in securely, and interact with an
AI chatbot specialized in programming and software development topics.
</p>

<p>
The project integrates Google Gemini AI for intelligent responses and MySQL for
user authentication and data management.
</p>

<hr>

<h2>Features</h2>

<ul>
  <li>Secure user authentication system</li>
  <li>Password hashing using bcrypt</li>
  <li>User registration and login</li>
  <li>Gemini AI integration</li>
  <li>Coding-focused AI chatbot</li>
  <li>Modern Streamlit-based web interface</li>
  <li>MySQL database connectivity</li>
  <li>Environment variable configuration using .env</li>
</ul>

<hr>

<h2>Technology Stack</h2>

<table>
  <tr>
    <th>Technology</th>
    <th>Purpose</th>
  </tr>
  <tr>
    <td>Python</td>
    <td>Backend Development</td>
  </tr>
  <tr>
    <td>Streamlit</td>
    <td>Web Interface</td>
  </tr>
  <tr>
    <td>Google Gemini AI</td>
    <td>AI Chatbot Integration</td>
  </tr>
  <tr>
    <td>MySQL</td>
    <td>Database Management</td>
  </tr>
  <tr>
    <td>SQLAlchemy</td>
    <td>Database ORM</td>
  </tr>
  <tr>
    <td>bcrypt</td>
    <td>Password Security</td>
  </tr>
  <tr>
    <td>dotenv</td>
    <td>Environment Variable Management</td>
  </tr>
</table>

<hr>

<h2>Project Structure</h2>

<pre>
DevBot/
│
├── auth.py
├── chatapp.py
├── create_user.py
├── database.py
├── web_interface.py
├── requirements.txt
├── .env
└── README.md
</pre>

<hr>

<h2>Installation</h2>

<h3>1. Clone the Repository</h3>

<pre>
git clone https://github.com/your-username/devbot.git
cd devbot
</pre>

<h3>2. Create Virtual Environment</h3>

<pre>
python -m venv venv
</pre>

<h3>3. Activate Virtual Environment</h3>

<p><b>Windows</b></p>

<pre>
venv\Scripts\activate
</pre>

<p><b>Linux / macOS</b></p>

<pre>
source venv/bin/activate
</pre>

<h3>4. Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<hr>

<h2>Environment Variables</h2>

<p>
Create a <code>.env</code> file in the project root directory.
</p>

<pre>
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=devbot_db

GEMINI_API_KEY=your_gemini_api_key
</pre>

<hr>

<h2>Database Setup</h2>

<h3>Create Database</h3>

<pre>
CREATE DATABASE devbot_db;
</pre>

<h3>Create Users Table</h3>

<pre>
CREATE TABLE users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100) UNIQUE,
    password_hash TEXT
);
</pre>

<hr>

<h2>Running the Application</h2>

<pre>
streamlit run web_interface.py
</pre>

<hr>

<h2>Default Admin Account</h2>

<p>
You can create a default admin account using:
</p>

<pre>
python create_user.py
</pre>

<p>
Default credentials:
</p>

<pre>
Username: admin
Password: admin123
</pre>

<hr>

<h2>Security Features</h2>

<ul>
  <li>Password hashing using bcrypt</li>
  <li>Secure database queries using SQLAlchemy</li>
  <li>Environment variable protection using .env</li>
  <li>Protected authentication workflow</li>
</ul>

<hr>

<h2>Requirements</h2>

<pre>
streamlit
google-generativeai
python-dotenv
sqlalchemy
pymysql
bcrypt
pandas
cryptography
</pre>

<hr>

<h2>Future Improvements</h2>

<ul>
  <li>Chat history support</li>
  <li>Session persistence</li>
  <li>Code syntax highlighting</li>
  <li>Multi-user dashboard</li>
  <li>Deployment support</li>
  <li>OAuth authentication</li>
</ul>

<hr>


<hr>

<h2>License</h2>

<p>
This project is intended for educational and learning purposes.
</p>

<hr>

<h2>Author</h2>

<p>
Developed using Python, Streamlit, MySQL, and Google Gemini AI.
</p>

import streamlit as st
from chatapp import structured_generator
from auth import authenticate_user, register_user

# session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "login"
    
def login():

    st.markdown("""
<style>

/* Page background */
.stApp{
    background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
}

/* Center the login container */
section.main > div{
    display:flex;
    justify-content:center;
}

/* Glass card effect */
div[data-testid="column"]{
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(20px);
    border-radius:25px;
    padding:40px;
    border:1px solid rgba(255,255,255,0.15);
    box-shadow:0 10px 40px rgba(0,0,0,0.4);
}

/* Inputs */
.stTextInput input{
    border-radius:12px;
}

/* Buttons */
.stButton button{
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.markdown('<div class="gradient-bar"></div>', unsafe_allow_html=True)

        st.title("DevBot Login")

        username = st.text_input("Email ID")
        password = st.text_input("Password", type="password")

        if st.button("Login"):

            if authenticate_user(username, password):

                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Login successful")
                st.rerun()

            else:
                st.error("Invalid Username or Password")

        if st.button("Create New Account"):
            st.session_state.page = "register"
            st.rerun()

def register():

    st.title("Create Account 🧑‍💻")

    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")

    if st.button("Register"):

        if register_user(new_username, new_password):

            st.success("Account created successfully! You can login now.")
            st.session_state.page = "login"
            st.rerun()

        else:
            st.error("Username already exists")


def chatbot():

    st.title("DevBot")
    st.write("Generate coding-based information using Gemini AI")

    user_input = st.text_input("Enter your queries", "queries ....")

    if st.button("Generate"):

        prompt = f"""
You are CodeMate, an AI chatbot specialized in programming and software development.

Your primary goal is to help users with coding-related questions, including:
- Writing, debugging, and explaining code
- Explaining programming concepts
- Assisting with frameworks, tools, and algorithms
- Helping with project ideas or code optimization

If a user asks a question that is NOT related to programming — politely respond with:
"This question is out of scope. I can only assist with coding or programming-related topics."

User query: {user_input}
"""

        result = structured_generator(prompt)

        st.write(result)

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()


def main():

    if st.session_state.logged_in:
        chatbot()

    else:
        if st.session_state.page == "login":
            login()

        elif st.session_state.page == "register":
            register()


if __name__ == "__main__":
    main()
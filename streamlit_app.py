import streamlit as st

# Define minimal page functions
def home_page():
    st.title("Home Page")
    st.write("Welcome to the home page!")

def about_page():
    st.title("About Us")
    st.write("Learn more about our simple app.")

def contact_page():
    st.title("Contact Us")
    st.write("Feel free to reach out.")
    st.text_input("Your Email")
    st.text_area("Your Message")
    st.button("Send")

# Create pages using Material icons
pages = [
    st.Page(home_page, title="Home", icon=":material/home:", default=True),
    st.Page(about_page, title="About", icon=":material/info:"),
    st.Page(contact_page, title="Contact", icon=":material/mail:"),
]

# Set up top navigation
current_page = st.navigation(pages, position="top")

# Run the selected page
current_page.run()

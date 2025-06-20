import streamlit as st

# Set page config
st.set_page_config(layout="wide")

# Add the Streamlit logo
st.logo("https://www.streamlit.io/images/brand/streamlit-mark-color.svg", link="https://streamlit.io")


# Define minimal page functions
def home_page():
    st.title("Home Page")
    st.write("Welcome to the home page!")
    st.write("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor
        incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
        exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute
        irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
        pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
        deserunt mollit anim id est laborum.
    """)
    st.write("""
        Curabitur pretium tincidunt lacus, eget pretium justo cursus nec. Praesent
        facilisis, urna at consectetur lacinia, urna libero varius velit, nec bibendum
        lectus justo vitae libero. Integer convallis, mi vitae feugiat accumsan, massa
        nibh vulputate justo, vitae iaculis est urna vel justo.
    """)


def about_page():
    st.title("About Us")
    st.write("Learn more about our simple app.")
    st.write("""
        Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis
        ac lectus. Mauris blandit aliquet elit, eget tincidunt nibh pulvinar a. Curabitur
        arcu erat, accumsan id imperdiet et, porttitor at sem. Vestibulum ac diam sit amet
        quam vehicula elementum sed sit amet dui. Quisque velit nisi, pretium et in,
        vulputate at, lorem.
    """)
    st.write("""
        Donec rutrum congue leo eget malesuada. Nulla porttitor accumsan tincidunt.
        Sed porttitor lectus nibh. Nulla quis lorem ut libero malesuada feugiat.
        Cras ultricies ligula sed magna dictum porta. Pellentesque in ipsum id orci porta
        dapibus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere
        cubilia Curae; Donec velit neque, auctor sit amet aliquam vel, ullamcorper sit amet
        ligula.
    """)

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

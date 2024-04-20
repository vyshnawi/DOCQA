import streamlit as st

# Set page title and background color
st.set_page_config(page_title="DocTalk", page_icon=":memo:", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS styles
custom_styles = """
<style>
    body {
        background-color: #f2f2f2;
    }
    .form-container {
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        padding: 20px;
        border-radius: 10px;
        background-color: white;
    }
</style>
"""

# Display custom CSS styles
st.markdown(custom_styles, unsafe_allow_html=True)

# Title
st.title("DocTalk")

# Form components
with st.form(key='my_form'):

    st.write("What you have in mind?")

    feedback = st.text_area("", "")

    submit_button = st.form_submit_button(label='Submit')

# Handle form submission
if submit_button:
  
    st.write("Here is your answer:")
 
    result = st.text_area("", "Do proper exercise, you will be just fine!")

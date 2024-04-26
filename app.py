import streamlit as st
import pickle

# @st.cache_data(allow_output_mutation=True)
def load_model(file_path):
    with open(file_path, 'rb') as file:
        model = pickle.load(file)
    return model

# Define the file path to your .pkl file
file_path = './Embeddings/faiss_index_all-mpnet-base-v2/index.pkl'

# Load the model
model = load_model(file_path)

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

st.markdown(custom_styles, unsafe_allow_html=True)

# Title
st.title("DocTalk")

# Form components
with st.form(key='my_form'):

    st.write("What you have in mind?")

    feedback = st.text_area("", "")

    submit_button = st.form_submit_button(label='Submit')

# Handle form submission
## Assuming the model is a classifier

if submit_button:
    # Perform prediction using the loaded model
    st.write(type(model))
    prediction = model.predict([feedback])[0]
    st.write(f"Prediction: {prediction}")

    st.write("Here is your answer:")
 
    result = st.text_area("", "Do proper exercise, you will be just fine!")

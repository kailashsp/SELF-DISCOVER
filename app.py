import streamlit as st
import os
from self_discover import SelfDiscover


st.set_page_config(
    page_title="SELF-DISCOVER",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("SELF-DISCOVER")


api_key = st.text_input("Enter OpenAI api key ")
task = st.text_area("Enter the task example you want to generate a reasoning structure for ")

if st.button("Generate Reasoning Structure"):
    os.environ["OPENAI_API_KEY"] = api_key
    result = SelfDiscover(task)
    result()
    tab1, tab2, tab3 = st.tabs(["SELECTED_MODULES", "ADAPTED_MODULES", "REASONING_STRUCTURE"])
    with tab1:
        st.header("SELECTED_MODULES")
        st.write(result.selected_modules)

    with tab2:
        st.header("ADAPTED_MODULES") 
        st.write(result.adapted_modules)

    with tab3:
        st.header("REASONING_STRUCTURE") 
        st.write(result.reasoning_structure)
else:
    st.error("Please provide both your API key and a task example.")


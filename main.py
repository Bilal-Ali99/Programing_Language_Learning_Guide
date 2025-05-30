
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain , SequentialChain
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
import time
import json

from sequential_chain import create_learning_chains

load_dotenv()

st.set_page_config(
    page_title="Programming Language Learning Guide",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Initialize Gemini API
@st.cache_resource
def initialize_llm():
    """Initialize and cache the Gemini LLM"""
    try:
        # Configure Gemini API
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        
        # Initialize ChatGoogleGenerativeAI
        llm = ChatGoogleGenerativeAI(
        model = 'gemini-2.0-flash',
        google_api_key = os.getenv("GEMINI_API_KEY"),
        temperature = 0.7 
        )
        return llm
    
    except Exception as e:
        st.error(f"Error initializing LLM: {str(e)}")
        st.logging.error(f"Error Log ")
        return None

def main():
    """Main Application function"""

    if 'last_language' not in st.session_state:
        st.session_state['last_language'] = None
    if 'results' not in st.session_state:
        st.session_state['results'] = None
    if 'generated_language' not in st.session_state:
        st.session_state['generated_language'] = None



    llm = initialize_llm() # Initializing LLM

    if llm is None:
        st.error("Failed to Initialize AI Model Check API Key")
        return
    
    st.title("Programming language Learning Guide")
    st.markdown("---")
    
    st.sidebar.title("Select the Programing Language")
    st.sidebar.markdown("Choose a Language to get Started")

    languages = [
        "Python", "JavaScript", "Java", "C++","PHP", "Ruby",
        "TypeScript", "Swift"
        ]

    selected_language = st.sidebar.selectbox(
        "Programing Language:",
        languages,
        index = 0,
        help="Select the language you want to learn"
        )

    st.sidebar.markdown("---")
    st.sidebar.markdown("Learning Prefrence")

    experience_level = st.sidebar.radio(
        "Your Experience Level: ",
        ["Beginner","Intermediate","Expert"],
        index = 0
        )

    time_commitment = st.sidebar.slider(
        "Hours Per Day: ",
        min_value = 0.5,
        max_value= 4.0,
        value =1.0,
        step= 0.5,
        help="Time you can Dedicate Every Day"
        )

    generate_plan = st.sidebar.button(
        "Generate Learning Plan",
        type = "primary",
        use_container_width= True 
        )

    if generate_plan or st.session_state.get('last_language') != selected_language:
        st.session_state['last_language']
        with st.spinner(f"Creating you personalized {selected_language} learning plan.."):
            try:
                roadmap_chain, schedule_chain, timeline_chain, sequential_chain = create_learning_chains(llm)

                result = sequential_chain({
                    "language" : selected_language,
                    "experience_level" : experience_level,
                    "daily_hours" : time_commitment
                }) 

                tab1, tab2, tab3 = st.tab(["Learning Roadmap","Daily Schedule","Timeline"])

                with tab1:
                    st.header(f"{selected_language} Learning Roadmap")
                    st.markdown(result["roadmap"])
                
                with tab2:
                    st.header(f"Daily Learning Schedule for {selected_language}")
                    st.markdown(result["schedule"])
                
                with tab3:
                    st.header(f"Estimated Time")
                    st.markdown(result["timeline"])
                
                st.session_state['results'] = result
                st.session_state['generated_language'] = selected_language
            
            except Exception as e:
                st.error(f"an Error Occured: {str(e)}")
                st.info("Please Try again or check you API Configuration")

    elif 'results' in st.session_state and st.session_state.get('generated_language') == selected_language:
        result = st.session_state['results']

        tab1, tab2, tab3 = st.tab(["Learning Roadmap","Daily Schedule","Timeline"])

        with tab1:
            st.header(f"{selected_language} Learning Roadmap")
            st.markdown(result["roadmap"])
        
        with tab2:
            st.header(f"Daily Learning Schedule for {selected_language}")
            st.markdown(result["schedule"])
        
        with tab3:
            st.header(f"Estimated Time")
            st.markdown(result["timeline"])

    else:
        st.info ("Select a Language and Click Generate Learning Plan")

        st.markdown("Features")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
            Roadmap
            Get a Detailed path to learn you chosen language
            """)

        with col2:
            st.markdown("""
            Daily Schedule
            Get a Structured Daily Plan to fit for your available time
            """)

        with col3:
            st.markdown("""
            Timeline Estimation
            Know How much time will it take to complete the goal
            """)

    st.markdown("---")
    st.markdown("If you want to learn something new change the language from the sidebar")



if __name__ == "__main__":
    main()
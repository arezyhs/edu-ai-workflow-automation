import streamlit as st
import sys
import os

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from config import Config

def main():
    st.set_page_config(
        page_title="edu-ai-workflow-automation",
        page_icon="🎓",
        layout="wide"
    )
    
    st.title("🎓 AI Educational Content Generator")
    st.markdown("---")
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose a workflow step:",
        [
            "📝 Material Input",
            "📊 Preprocessing", 
            "📋 Summarization",
            "❓ Question Generation",
            "✅ Quality Check",
            "🎨 Illustration Generation",
            "📄 Layout Automation",
            "📈 Results & Export"
        ]
    )
    
    # Main content area
    if page == "📝 Material Input":
        show_material_input()
    elif page == "📊 Preprocessing":
        show_preprocessing()
    elif page == "📋 Summarization":
        show_summarization()
    elif page == "❓ Question Generation":
        show_question_generation()
    elif page == "✅ Quality Check":
        show_quality_check()
    elif page == "🎨 Illustration Generation":
        show_illustration_generation()
    elif page == "📄 Layout Automation":
        show_layout_automation()
    elif page == "📈 Results & Export":
        show_results_export()

def show_material_input():
    st.header("📝 Material Input")
    
    input_method = st.radio(
        "Choose input method:",
        ["Upload PDF", "Manual Text Input"]
    )
    
    if input_method == "Upload PDF":
        uploaded_file = st.file_uploader(
            "Choose a PDF file",
            type="pdf",
            help="Upload educational material in PDF format"
        )
        
        if uploaded_file is not None:
            st.success(f"File uploaded: {uploaded_file.name}")
            # TODO: Process PDF file
            
    elif input_method == "Manual Text Input":
        text_input = st.text_area(
            "Enter educational material:",
            height=300,
            placeholder="Paste or type your educational content here..."
        )
        
        if text_input:
            st.info(f"Text length: {len(text_input)} characters")
            # TODO: Process manual text

def show_preprocessing():
    st.header("📊 Preprocessing")
    st.info("This module will clean and normalize the input material.")
    st.write("Coming soon...")

def show_summarization():
    st.header("📋 Summarization")
    st.info("AI-powered summarization with learning objectives identification.")
    st.write("Coming soon...")

def show_question_generation():
    st.header("❓ Question Generation")
    st.info("Generate various types of educational questions with answers.")
    st.write("Coming soon...")

def show_quality_check():
    st.header("✅ Quality Check")
    st.info("AI-powered validation and proofreading of generated content.")
    st.write("Coming soon...")

def show_illustration_generation():
    st.header("🎨 Illustration Generation")
    st.info("Generate educational illustrations and diagrams.")
    st.write("Coming soon...")

def show_layout_automation():
    st.header("📄 Layout Automation")
    st.info("Automatically create presentations and documents.")
    st.write("Coming soon...")

def show_results_export():
    st.header("📈 Results & Export")
    st.info("View results and export generated content.")
    st.write("Coming soon...")

if __name__ == "__main__":
    try:
        # Validate configuration
        Config.validate_config()
        main()
    except ValueError as e:
        st.error(f"Configuration Error: {e}")
        st.info("Please check your .env file and ensure all required API keys are set.")
import os
import re
import requests
import streamlit as st
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="Website Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced styling
st.markdown("""
    <style>
        .main {
            max-width: 1200px;
        }
        .stTitle {
            text-align: center;
            color: #1f77b4;
        }
        .stSubheader {
            color: #ff7f0e;
        }
        .output-box {
            background-color: #f0f2f6;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #1f77b4;
        }
        .info-box {
            background-color: #e8f4f8;
            padding: 12px;
            border-radius: 5px;
            border-left: 4px solid #17a2b8;
        }
        .error-box {
            background-color: #f8d7da;
            padding: 12px;
            border-radius: 5px;
            border-left: 4px solid #dc3545;
        }
        .success-box {
            background-color: #d4edda;
            padding: 12px;
            border-radius: 5px;
            border-left: 4px solid #28a745;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize OpenAI Client
@st.cache_resource
def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        st.error("❌ OPENAI_API_KEY not found in the .env file")
        st.stop()
    return OpenAI(api_key=api_key)

# Scrape Website Content
def scrape_website(url: str) -> str:
    """Scrape website content using BeautifulSoup."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Remove script, style, and noscript tags
        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()
        
        # Extract text
        text = soup.get_text(separator=" ")
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"[^a-zA-Z0-9.,!?\-':; ]+", "", text)
        
        return text.strip()
    except requests.RequestException as e:
        raise Exception(f"Error fetching URL: {str(e)}")

# System Prompt
SYSTEM_PROMPT = """You are an intelligent and helpful Website Chatbot Assistant. You answer questions based ONLY on the provided website content.

Guidelines:
- Provide accurate, concise, and relevant answers based on the website content
- If the answer cannot be found in the content, clearly state: "I don't have that information based on the website content provided."
- Be friendly and professional in your responses
- If a question is ambiguous, ask for clarification
- Support multiple languages if the content contains them"""

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = []
if "website_content" not in st.session_state:
    st.session_state.website_content = None
if "website_url" not in st.session_state:
    st.session_state.website_url = None

# Title and Description
st.markdown("# 🤖 Website Chatbot")
st.markdown("### Intelligent Q&A about any website content")
st.markdown("---")

# Sidebar Configuration
with st.sidebar:
    st.markdown("## ⚙️ Configuration")
    
    # URL Input
    url_input = st.text_input(
        "Enter Website URL:",
        placeholder="https://example.com",
        help="Enter the full URL of the website you want to chat about"
    )
    
    # Load Website Button
    if st.button("🔄 Load Website", use_container_width=True):
        if url_input:
            with st.spinner("🔄 Loading and processing website..."):
                try:
                    st.session_state.website_content = scrape_website(url_input)
                    st.session_state.website_url = url_input
                    st.session_state.messages = []  # Reset messages for new URL
                    st.success(f"✅ Successfully loaded {len(st.session_state.website_content)} characters from the website!")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        else:
            st.warning("⚠️ Please enter a valid URL")
    
    # Display current URL status
    if st.session_state.website_url:
        st.markdown("---")
        st.markdown("### 📍 Current Website")
        st.caption(st.session_state.website_url)
        st.progress(min(len(st.session_state.website_content) / 100000, 1.0), 
                   text=f"Content Size: {len(st.session_state.website_content):,} characters")
    
    # Clear Chat Button
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Main Content Area
if st.session_state.website_content:
    st.markdown(f"### 💬 Ask Questions About: {st.session_state.website_url}")
    
    # Display Chat History
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.messages:
            if message["role"] == "user":
                with st.chat_message("user", avatar="👤"):
                    st.markdown(message["content"])
            else:
                with st.chat_message("assistant", avatar="🤖"):
                    st.markdown(message["content"])
    
    # User Input
    st.markdown("---")
    user_input = st.chat_input("Ask a question about the website content...")
    
    if user_input:
        # Add user message to session
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })
        
        # Display user message
        with st.chat_message("user", avatar="👤"):
            st.markdown(user_input)
        
        # Get AI Response
        try:
            client = get_openai_client()
            
            # Prepare messages for API
            messages_for_api = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "system", "content": f"Website Content:\n{st.session_state.website_content}"}
            ]
            messages_for_api.extend(st.session_state.messages)
            
            # Get response
            with st.spinner("🤔 Thinking..."):
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=messages_for_api,
                    temperature=0.7,
                    max_tokens=1000
                )
            
            assistant_reply = response.choices[0].message.content
            
            # Add assistant message to session
            st.session_state.messages.append({
                "role": "assistant",
                "content": assistant_reply
            })
            
            # Display assistant response
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown(assistant_reply)
        
        except Exception as e:
            st.error(f"❌ Error getting response: {str(e)}")
else:
    # Landing Page
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 🚀 Getting Started")
        st.markdown("""
        1. **Enter a URL** in the sidebar
        2. **Click "Load Website"** to process the content
        3. **Ask Questions** in the chat box
        4. **Get Instant Answers** powered by AI
        """)
    
    with col2:
        st.markdown("### ✨ Features")
        st.markdown("""
        - 🌐 Scrapes and analyzes any website
        - 🤖 AI-powered Q&A using GPT-4
        - 💬 Interactive chat interface
        - ⚡ Fast and responsive
        - 🔒 Secure API integration
        """)
    
    st.markdown("---")
    st.markdown("### 📝 Example Usage")
    st.info("Try loading a website like https://example.com and ask questions about its content!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888;">
    <small>Website Chatbot • Powered by OpenAI GPT-4 & Streamlit</small>
</div>
""", unsafe_allow_html=True)
import streamlit as st
import requests
import json
from datetime import datetime

st.set_page_config(
    page_title="AI Interview Assistant",
    page_icon="🎯",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.solution-box {
    background-color: #f0f2f6;
    padding: 20px;
    border-radius: 10px;
    margin: 10px 0;
}
.complexity-badge {
    background-color: #ff4b4b;
    color: white;
    padding: 5px 10px;
    border-radius: 20px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("Interview Settings")
    
    question_type = st.selectbox(
        "Question Type",
        ["Coding", "System Design", "Behavioral", "ML Theory"]
    )
    
    company = st.selectbox(
        "Target Company",
        ["Google", "Meta", "Amazon", "Microsoft", "Apple", "General"]
    )
    
    difficulty = st.select_slider(
        "Difficulty",
        ["Easy", "Medium", "Hard"]
    )

# Main content
st.title("🎯 AI Interview Assistant")
st.markdown("Your personal FAANG interview coach powered by AI")

# Input section
col1, col2 = st.columns([3, 1])

with col1:
    question = st.text_area(
        "Enter your interview question:",
        height=150,
        placeholder="e.g., Design a distributed rate limiter..."
    )

with col2:
    st.markdown("### Quick Actions")
    if st.button("📝 Random Question", use_container_width=True):
        # Fetch random question
        pass
    
    if st.button("📊 My Progress", use_container_width=True):
        # Show progress dashboard
        pass

# Solution section
if st.button("🚀 Get Solution", type="primary", use_container_width=True):
    if question:
        with st.spinner("AI is thinking..."):
            # Call backend API
            response = requests.post(
                "http://localhost:8000/api/solve",
                json={
                    "question": question,
                    "question_type": question_type.lower(),
                    "company": company.lower(),
                    "difficulty": difficulty.lower()
                }
            )
            
            if response.status_code == 200:
                solution = response.json()
                
                # Display solution
                st.markdown("## 💡 Solution")
                
                # For coding questions
                if question_type == "Coding":
                    st.markdown("### Approach")
                    st.info(solution["approach"])
                    
                    st.markdown("### Implementation")
                    st.code(solution["code"], language="python")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown("### Time Complexity")
                        st.markdown(f"**{solution['complexity']['time']}**")
                    
                    with col2:
                        st.markdown("### Space Complexity")
                        st.markdown(f"**{solution['complexity']['space']}**")
                
                # For system design
                elif question_type == "System Design":
                    tabs = st.tabs(["Architecture", "Components", "Scaling", "Trade-offs"])
                    
                    with tabs[0]:
                        st.markdown(solution["architecture"])
                        # Display architecture diagram
                    
                    with tabs[1]:
                        for component, details in solution["components"].items():
                            st.markdown(f"**{component}**: {details}")
                    
                    with tabs[2]:
                        st.markdown(solution["scaling"])
                    
                    with tabs[3]:
                        st.markdown(solution["tradeoffs"])

# Progress tracking
if st.checkbox("Show Practice Stats"):
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Problems Solved", "127", "+12 this week")
    
    with col2:
        st.metric("Success Rate", "84%", "+3%")
    
    with col3:
        st.metric("Streak", "15 days", "+1")
    
    with col4:
        st.metric("Interview Ready", "72%", "+8%")
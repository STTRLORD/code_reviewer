import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from typing import List
from langchain_core.output_parsers import PydanticOutputParser
from langchain_groq import ChatGroq

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Code Explainer",
    page_icon="🔍",
    layout="wide"
)

# Initialize model
@st.cache_resource
def get_model():
    return ChatGroq(model="openai/gpt-oss-120b")

model = get_model()

# Pydantic model for structured output
class CodeExplanation(BaseModel):
    language: str = Field(description="Detected programming language")
    explanation: str = Field(description="What the code does, in simple terms")
    time_complexity: str = Field(description="Big-O time complexity of the code, e.g. O(n), O(n^2)")
    space_complexity: str = Field(description="Big-O space complexity of the code")
    issues: List[str] = Field(description="Potential bugs, errors, or problems found in the code")
    improvements: List[str] = Field(description="Suggestions to improve code quality, performance, or readability")
    optimized_code: str = Field(description="An optimized/improved version of the given code, following the suggestions")

parser = PydanticOutputParser(pydantic_object=CodeExplanation)

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an expert code reviewer and software engineer.

Your task is to analyze the given code carefully and provide a structured review.

Instructions:
- Detect the programming language.
- Explain what the code does in simple, clear terms.
- Analyze the time complexity (Big-O) of the code.
- Analyze the space complexity (Big-O) of the code.
- List genuine issues, bugs, or problems in the code (leave empty if none).
- List improvements — optimization, readability, or best-practice suggestions (leave empty if none).

Do not assume functionality that isn't present in the code.

{format_instructions}"""),
    ("human", "Code:\n{code}")
])

# Main UI
st.title("🔍 Code Explainer")
st.markdown("Analyze your code with AI-powered insights")

# Input section
st.subheader("Input Code")
code_input = st.text_area(
    "Paste your code here:",
    height=200,
    placeholder="def example():\n    return 'Hello World'"
)

# Analyze button
if st.button("Analyze Code", type="primary"):
    if not code_input.strip():
        st.warning("Please enter some code to analyze.")
    else:
        with st.spinner("Analyzing code..."):
            try:
                # Create prompt
                final_prompt = prompt.invoke({
                    "code": code_input,
                    'format_instructions': parser.get_format_instructions()
                })
                
                # Get response
                response = model.invoke(final_prompt)
                code_data = parser.parse(response.content)
                
                # Display results
                st.success("Analysis Complete!")
                
                # Language detection
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Detected Language", code_data.language)
                with col2:
                    st.metric("Time Complexity", code_data.time_complexity)
                
                st.metric("Space Complexity", code_data.space_complexity)
                
                # Explanation
                st.subheader("📝 Explanation")
                st.write(code_data.explanation)
                
                # Issues
                if code_data.issues:
                    st.subheader("⚠️ Issues Found")
                    for issue in code_data.issues:
                        st.error(f"• {issue}")
                else:
                    st.subheader("✅ Issues")
                    st.info("No issues detected in the code.")
                
                # Improvements
                if code_data.improvements:
                    st.subheader("💡 Suggestions for Improvement")
                    for improvement in code_data.improvements:
                        st.success(f"• {improvement}")
                else:
                    st.subheader("💡 Suggestions")
                    st.info("No specific improvements suggested.")
                
                # Optimized code
                if code_data.optimized_code:
                    st.subheader("🚀 Optimized Code")
                    st.code(code_data.optimized_code, language=code_data.language.lower())
                
            except Exception as e:
                st.error(f"An error occurred during analysis: {str(e)}")

# Footer
st.markdown("---")
st.markdown("Built with Streamlit, LangChain, and Groq")

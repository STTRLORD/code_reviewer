import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from typing import List
from langchain_core.output_parsers import PydanticOutputParser
from langchain_groq import ChatGroq

load_dotenv()

st.set_page_config(page_title="Code Reviewer", page_icon="◆", layout="centered")

# ---------- Custom CSS ----------
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}

    html, body, [class*="css"] {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Inter, sans-serif;
    }

    :root {
        --bg: #262624;
        --surface: #2d2d2b;
        --surface-hover: #333331;
        --border: #3d3d3a;
        --text: #f5f4ef;
        --text-muted: #a8a29a;
        --text-dim: #77726a;
        --accent: #c17a5c;
        --accent-soft: rgba(193, 122, 92, 0.12);
        --issue: #b08968;
        --improve: #8a9a83;
    }

    .stApp { background-color: var(--bg); }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(8px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes shimmer {
        0% { background-position: -400px 0; }
        100% { background-position: 400px 0; }
    }

    .block-container {
        max-width: 760px;
        padding-top: 3rem;
        padding-bottom: 4rem;
    }

    /* Header */
    .brand {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        margin-bottom: 0.3rem;
    }
    .brand-mark {
        width: 26px; height: 26px;
        border-radius: 7px;
        background: var(--accent);
        display: flex; align-items: center; justify-content: center;
        flex-shrink: 0;
    }
    .app-title { font-size: 1.4rem; font-weight: 600; color: var(--text); letter-spacing: -0.01em; }
    .app-subtitle { font-size: 0.95rem; color: var(--text-dim); margin: 0.4rem 0 2rem 0; }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #232321;
        border-right: 1px solid var(--border);
    }
    section[data-testid="stSidebar"] * { color: var(--text-muted) !important; }
    section[data-testid="stSidebar"] strong { color: var(--text) !important; }

    /* Text area */
    div[data-testid="stTextArea"] textarea {
        background-color: var(--surface) !important;
        border: 1px solid var(--border) !important;
        border-radius: 12px !important;
        color: var(--text) !important;
        font-family: "SF Mono", "Fira Code", Menlo, monospace !important;
        font-size: 0.92rem !important;
        padding: 1rem !important;
        transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }
    div[data-testid="stTextArea"] textarea:focus {
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 3px var(--accent-soft) !important;
    }

    /* Button */
    div.stButton > button {
        background-color: var(--accent);
        color: #fff5ef;
        border: none;
        border-radius: 9px;
        font-weight: 500;
        font-size: 0.95rem;
        padding: 0.6rem 0;
        transition: filter 0.15s ease, transform 0.12s ease;
    }
    div.stButton > button:hover { filter: brightness(1.08); transform: translateY(-1px); }
    div.stButton > button:active { transform: translateY(0); }

    /* Skeleton loader */
    .skeleton {
        border-radius: 10px;
        background: linear-gradient(90deg, var(--surface) 25%, #38382f 50%, var(--surface) 75%);
        background-size: 800px 100%;
        animation: shimmer 1.4s infinite linear;
        margin-bottom: 0.6rem;
    }

    /* Metric row */
    .metric-row { display: flex; gap: 0.75rem; margin: 1.75rem 0; animation: fadeIn 0.35s ease-out; }
    .metric-box {
        flex: 1;
        background-color: var(--surface);
        border: 1px solid var(--border);
        border-radius: 11px;
        padding: 0.9rem 1.1rem;
        transition: border-color 0.2s ease;
    }
    .metric-box:hover { border-color: #4a4a45; }
    .m-label { font-size: 0.72rem; color: var(--text-dim); text-transform: uppercase; letter-spacing: 0.07em; margin-bottom: 0.3rem; font-weight: 500; }
    .m-value { font-size: 1.08rem; color: var(--text); font-weight: 600; }

    /* Section */
    .section-block { animation: fadeIn 0.4s ease-out; }
    .section-heading {
        display: flex; align-items: center; gap: 0.5rem;
        font-size: 1.1rem; font-weight: 600; color: var(--text);
        margin: 2.2rem 0 1rem 0;
    }
    .section-heading svg { flex-shrink: 0; opacity: 0.75; }

    .explain-text { font-size: 1.06rem; line-height: 1.8; color: #ddd8cf; }

    /* Rows */
    .row-item {
        display: flex; align-items: flex-start; gap: 0.75rem;
        background-color: var(--surface);
        border: 1px solid var(--border);
        border-radius: 10px;
        padding: 0.9rem 1.1rem;
        margin-bottom: 0.6rem;
        font-size: 1rem; line-height: 1.6; color: #e2ded6;
        transition: border-color 0.2s ease, background-color 0.2s ease;
    }
    .row-item:hover { border-color: #4a4a45; background-color: var(--surface-hover); }
    .row-dot { flex-shrink: 0; width: 7px; height: 7px; border-radius: 50%; margin-top: 0.55rem; }
    .dot-issue { background-color: var(--issue); }
    .dot-improve { background-color: var(--improve); }

    .empty-note { color: var(--text-dim); font-style: italic; font-size: 0.95rem; padding: 0.4rem 0; }

    /* Empty state before review */
    .empty-state {
        text-align: center;
        padding: 3.5rem 1rem;
        color: var(--text-dim);
        border: 1px dashed var(--border);
        border-radius: 14px;
        margin-top: 1.5rem;
        animation: fadeIn 0.4s ease-out;
    }
    .empty-state .es-title { color: var(--text-muted); font-size: 0.98rem; font-weight: 500; margin-bottom: 0.3rem; }
    .empty-state .es-sub { font-size: 0.88rem; }

    /* Expander */
    details {
        background-color: var(--surface) !important;
        border: 1px solid var(--border) !important;
        border-radius: 11px !important;
    }
    summary { color: var(--text) !important; }

    hr { border-color: var(--border); }
    ::selection { background: var(--accent-soft); }
</style>
""", unsafe_allow_html=True)


def icon(name: str) -> str:
    icons = {
        "doc": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/></svg>',
        "warn": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0Z"/><path d="M12 9v4M12 17h.01"/></svg>',
        "bulb": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M9 18h6M10 22h4M12 2a7 7 0 0 0-4 12.7c.6.5 1 1.2 1 2.05V17h6v-.25c0-.85.4-1.55 1-2.05A7 7 0 0 0 12 2Z"/></svg>',
        "code": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="m16 18 6-6-6-6M8 6l-6 6 6 6"/></svg>',
    }
    return icons.get(name, "")


# ---------- Schema ----------
class CodeExplanation(BaseModel):
    language: str = Field(description="Detected programming language")
    explanation: str = Field(description="What the code does, in simple terms")
    time_complexity: str = Field(description="Big-O time complexity of the code, e.g. O(n), O(n^2)")
    space_complexity: str = Field(description="Big-O space complexity of the code")
    issues: List[str] = Field(description="Potential bugs, errors, or problems found in the code")
    improvements: List[str] = Field(description="Suggestions to improve code quality, performance, or readability")
    optimized_code: str = Field(description="An optimized/improved version of the given code, following the suggestions")


parser = PydanticOutputParser(pydantic_object=CodeExplanation)

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


@st.cache_resource
def get_model():
    return ChatGroq(model="openai/gpt-oss-120b")


if "review" not in st.session_state:
    st.session_state.review = None

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("**Code Reviewer**")
    st.caption("Paste code and get a structured review — logic, complexity, issues, and a cleaner version.")
    st.divider()
    st.caption("Model · openai/gpt-oss-120b")
    st.caption("Runtime · Groq + LangChain")

# ---------- Header ----------
st.markdown("""
<div class="brand">
    <div class="brand-mark"></div>
    <div class="app-title">Code Reviewer</div>
</div>
<div class="app-subtitle">Paste your code below to get a structured breakdown.</div>
""", unsafe_allow_html=True)

code = st.text_area(
    "Paste your code here",
    height=240,
    placeholder="def add(a, b):\n    return a + b",
    label_visibility="collapsed",
)

review_clicked = st.button("Review code", type="primary", use_container_width=True)

if review_clicked:
    if not code.strip():
        st.warning("Please paste some code first.")
    else:
        placeholder = st.empty()
        with placeholder.container():
            st.markdown('<div class="skeleton" style="height:70px;"></div>', unsafe_allow_html=True)
            st.markdown('<div class="skeleton" style="height:110px;"></div>', unsafe_allow_html=True)
            st.markdown('<div class="skeleton" style="height:160px;"></div>', unsafe_allow_html=True)
            try:
                model = get_model()
                final_prompt = prompt.invoke({
                    "code": code,
                    "format_instructions": parser.get_format_instructions()
                })
                response = model.invoke(final_prompt)
                st.session_state.review = parser.parse(response.content)
            except Exception as e:
                st.session_state.review = None
                placeholder.empty()
                st.error(f"Something went wrong: {e}")
                st.stop()
        placeholder.empty()

review = st.session_state.review

if review is None:
    st.markdown("""
    <div class="empty-state">
        <div class="es-title">No review yet</div>
        <div class="es-sub">Paste code above and click "Review code" to get started.</div>
    </div>
    """, unsafe_allow_html=True)
else:
    # Metrics row
    st.markdown(f"""
    <div class="metric-row">
        <div class="metric-box"><div class="m-label">Language</div><div class="m-value">{review.language}</div></div>
        <div class="metric-box"><div class="m-label">Time</div><div class="m-value">{review.time_complexity}</div></div>
        <div class="metric-box"><div class="m-label">Space</div><div class="m-value">{review.space_complexity}</div></div>
    </div>
    """, unsafe_allow_html=True)

    # Explanation
    st.markdown(f'<div class="section-block"><div class="section-heading">{icon("doc")}Explanation</div>'
                f'<div class="explain-text">{review.explanation}</div></div>', unsafe_allow_html=True)

    # Issues
    issues_html = "".join(
        f'<div class="row-item"><div class="row-dot dot-issue"></div><div>{i}</div></div>'
        for i in review.issues
    ) if review.issues else '<div class="empty-note">No issues found.</div>'
    st.markdown(f'<div class="section-block"><div class="section-heading">{icon("warn")}Issues</div>{issues_html}</div>',
                unsafe_allow_html=True)

    # Improvements
    imp_html = "".join(
        f'<div class="row-item"><div class="row-dot dot-improve"></div><div>{i}</div></div>'
        for i in review.improvements
    ) if review.improvements else '<div class="empty-note">No improvements suggested.</div>'
    st.markdown(f'<div class="section-block"><div class="section-heading">{icon("bulb")}Improvements</div>{imp_html}</div>',
                unsafe_allow_html=True)

    # Optimized code
    st.markdown(f'<div class="section-block"><div class="section-heading">{icon("code")}Optimized code</div></div>',
                unsafe_allow_html=True)
    with st.expander("View optimized version", expanded=True):
        st.code(review.optimized_code, language=review.language.lower())
import streamlit as st
from google import genai
import PyPDF2

st.set_page_config(page_title="ResumeIQ", page_icon="📄", layout="wide")
st.title("📄 ResumeIQ — AI Resume Analyzer")
st.caption("Paste a job description and upload your resume to get an instant match score and improvements")

api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")
uploaded_file = st.sidebar.file_uploader("Upload Resume (PDF)", type="pdf")
job_desc = st.text_area("Paste Job Description here", height=200)

def extract_text(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def analyze_resume(api_key, resume_text, job_desc):
    client = genai.Client(api_key=api_key)
    prompt = f"""You are an expert technical recruiter. Analyze this resume against the job description.

Resume:
{resume_text[:5000]}

Job Description:
{job_desc[:3000]}

Provide exactly this output with these headers:

## Match Score
Give a score out of 100 with one sentence explanation.

## Matching Skills
List 5-8 skills from the resume that match the job description.

## Missing Skills
List 5-8 important skills from the job description that are missing from the resume.

## Top 3 Improvements
Give exactly 3 specific changes to make to the resume to increase chances.

## ATS Keywords to Add
List 8-10 keywords from the job description to add to the resume."""

    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=prompt
    )
    return response.text

if uploaded_file and api_key and job_desc:
    with st.spinner("Analysing your resume..."):
        resume_text = extract_text(uploaded_file)
        result = analyze_resume(api_key, resume_text, job_desc)
    st.markdown(result)
elif not api_key:
    st.info("👈 Enter your Gemini API key in the sidebar")
elif not uploaded_file:
    st.info("👈 Upload your resume PDF in the sidebar")
elif not job_desc:
    st.info("☝️ Paste a job description above to get started")
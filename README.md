# 📄 ResumeIQ — AI-Powered Resume Analyzer

> Paste any job description. Upload your resume. Get an instant AI match score and improvement plan.

## 🔗 Live Demo
**[Try it here → adarsh-resumeiq-analyzer.streamlit.app](https://adarsh-resumeiq-analyzer.streamlit.app)**

## 📌 What It Does
- Upload your resume as a PDF
- Paste any job description
- AI instantly outputs:
  - ✅ Match score out of 100
  - ✅ Matching skills found in your resume
  - ✅ Missing skills you should add
  - ✅ ATS keywords to include
  - ✅ Top 3 specific resume improvements

## 🧠 How It Works
1. Resume PDF → text extracted via PyPDF2
2. Job description + resume passed to Gemini with structured prompt
3. Gemini returns analysis in enforced sections
4. Results displayed as clean formatted output in Streamlit

## 🛠️ Tech Stack
| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit |
| AI Model | Google Gemini 2.0 Flash |
| PDF Processing | PyPDF2 |
| Prompt Engineering | Structured output pipeline |
| Deployment | Streamlit Cloud |

## 🚀 Run Locally
```bash
git clone https://github.com/adarshkashyap1002/resumeiq-analyzer
cd resumeiq-analyzer
pip install streamlit google-genai PyPDF2
streamlit run app.py
```

## 👤 Author
**Adarsh Kashyap** — [LinkedIn](https://linkedin.com/in/adarshkashyap1002) | [GitHub](https://github.com/adarshkashyap1002)

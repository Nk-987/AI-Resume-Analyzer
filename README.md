# 🤖 AI Resume Analyzer

An AI-powered web application that analyzes resumes against job descriptions and provides an ATS (Applicant Tracking System) compatibility score.

---

## 🚀 Features

- 📄 Upload resume (PDF)
- 📝 Paste job description
- 📊 ATS score calculation
- 🔍 Keyword matching using NLP
- ⚡ Instant feedback

---

## 🧠 Tech Stack

- Python
- Streamlit
- Scikit-learn
- NLP (TF-IDF, Cosine Similarity)
- PyPDF2

---

## ⚙️ How It Works

1. Extract text from resume
2. Preprocess text (cleaning, tokenization)
3. Convert text into vectors using TF-IDF
4. Compare with job description using cosine similarity
5. Generate ATS score

---

## 📊 Results

- Accurate similarity scoring
- Helps improve resume targeting
- Identifies missing keywords

---

## ▶️ Run Locally

```bash
pip install streamlit scikit-learn nltk PyPDF2
streamlit run app.py

# AI Resume Analyzer

AI Resume Analyzer is a machine learning application that evaluates resumes against job descriptions and calculates an ATS match score.

## Features

- Resume PDF upload
- Job description analysis
- ATS compatibility score
- NLP-based keyword matching

## Tech Stack

- Python
- Streamlit
- Scikit-learn
- NLP (TF-IDF)
- PyPDF2

## How It Works

1. Upload resume
2. Paste job description
3. System preprocesses text
4. TF-IDF vectorization
5. Cosine similarity calculation
6. ATS score generated

## Installation


pip install streamlit scikit-learn nltk PyPDF2


Run:


streamlit run app.py


## Use Case

Helps job seekers evaluate how well their resume matches job descriptions.

## Future Improvements

- Skill gap detection
- Resume improvement suggestions
- Keyword highlighting

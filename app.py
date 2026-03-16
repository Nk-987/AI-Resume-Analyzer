import streamlit as st
import PyPDF2
import string
import nltk

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

st.title("AI Resume Analyzer")

st.write("Upload your resume and compare it with a job description to get an ATS match score.")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description")


def extract_text_from_pdf(file):
    text = ""
    reader = PyPDF2.PdfReader(file)

    for page in reader.pages:
        text += page.extract_text()

    return text


def preprocess_text(text):

    stop_words = set(stopwords.words("english"))
    tokens = word_tokenize(text.lower())

    cleaned = []

    for word in tokens:
        if word not in stop_words and word not in string.punctuation:
            cleaned.append(word)

    return " ".join(cleaned)


def calculate_similarity(resume, job):

    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([resume, job])

    score = cosine_similarity(tfidf[0:1], tfidf[1:2])

    return score[0][0] * 100


if st.button("Analyze Resume"):

    if resume_file is not None and job_description != "":

        resume_text = extract_text_from_pdf(resume_file)

        resume_clean = preprocess_text(resume_text)
        job_clean = preprocess_text(job_description)

        score = calculate_similarity(resume_clean, job_clean)

        st.subheader("ATS Match Score")
        st.success(str(round(score,2)) + " %")

    else:
        st.warning("Please upload resume and paste job description.")

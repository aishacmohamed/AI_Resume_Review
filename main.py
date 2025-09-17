import streamlit as st
import PyPDF2
import io
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Resume Review", page_icon=":page_facing_up:", layout="centered")
st.title("AI Resume Reviewer")
st.markdown("Upload your resume in PDF format and get instant feedback!")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

uploaded_file = st.file_uploader("Upload Your Resume! (PDF or TXT)", type=["pdf", "txt"])
jobrole=st.text_input("Enter the Job Role you are applying for (optional):")

analyze_button = st.button("Analyze Resume")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

if analyze_button and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("File does not have any content...")
            st.stop()
        
        prompt = f"""Please analyze this resume and provide constructive feedback. 
        Focus on the following aspects:
        1. Content clarity and impact
        2. Skills presentation
        3. Experience descriptions
        4. Specific improvements for {jobrole if jobrole else 'general job applications'}
        
        Resume content:
        {file_content}
        
        Start with a score out of 100, then please provide your analysis in a clear, structured format with specific recommendations."""

        Client = OpenAI(api_key = OPENAI_API_KEY)
        response = Client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = [
                {"role": "system", "content": "You are an expert recruiter with years of experience in recruiting and HR."},
                {"role": "user", "content": prompt}
            ],
                temperature=0.7,
                max_tokens=1000
        )
        st.markdown("### Resume Analysis")
        st.markdown(response.choices[0].message.content)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        

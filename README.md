# AI Resume Reviewer

## Overview
The AI Resume Reviewer is a web application built using **Streamlit** and **OpenAI**. It allows users to upload their resumes and receive instant, AI-generated feedback to improve their job applications.

## Features
- **Resume Upload:** Accepts PDF and TXT files.
- **Optional Job Role Input:** Users can specify the job role they are applying for to get targeted feedback.
- **AI-Powered Analysis:** Uses OpenAI's GPT-4o-mini model to provide structured feedback.
- **Evaluation Focus:**
  1. Content clarity and impact
  2. Skills presentation
  3. Experience descriptions
  4. Specific improvements tailored to the job role (if provided)

## How It Works
1. Users upload their resume through the web interface.
2. The application extracts text from the uploaded file.
3. The AI analyzes the resume using a prompt designed for recruiters.
4. Feedback is returned with a score out of 100 and actionable recommendations.

## Technology Stack
- **Python**
- **Streamlit** – for the web interface
- **PyPDF2** – for PDF text extraction
- **OpenAI API** – for AI-powered resume analysis
- **python-dotenv** – for managing environment variables

## Usage
1. Install dependencies:
   ```bash
   uv add streamlit openai python-dotenv PyPDF2

### Setup

1. Create a `.env` file in the project root with your OpenAI API key:


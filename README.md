# 📄 AI Resume Analyzer

An intelligent Resume Parser and ATS-inspired Resume Analyzer built with **Python, Streamlit, NLP, and PyMuPDF**.

The application extracts structured information from PDF resumes, analyzes resume quality, calculates an ATS-style score, and provides actionable improvement suggestions.

---

## ✨ Features

- 📄 Upload PDF resumes
- 👤 Extract personal information
  - Name
  - Email
  - Phone Number
  - LinkedIn
  - GitHub
  - Portfolio
- 🛠 Detect technical skills using a customizable skills database
- 🎓 Extract education details
- 💼 Extract work experience
- 📂 Extract projects
- 📜 Extract certifications
- 📊 ATS-inspired resume scoring
- 💡 Resume improvement suggestions
- 📥 Export parsed data as JSON
- 📥 Export parsed data as CSV
- 🌐 Modern Streamlit web interface

---

## 🖼️ Preview

> *(Add screenshots here after deployment)*

---

## 🏗️ Project Structure

```text
Resume_Parser/
│
├── app.py
├── parser.py
├── extractor.py
├── scorer.py
├── history.py
├── data/
│   └── skills.txt
├── assets/
│   └── sample_resume.pdf
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

### Programming Language

- Python

### Frontend

- Streamlit

### PDF Processing

- PyMuPDF (fitz)

### NLP

- spaCy
- Regular Expressions (Regex)

### Data Handling

- Pandas
- JSON

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Resume_Parser.git
```

Go to the project folder

```bash
cd Resume_Parser
```

Install dependencies

```bash
pip install -r requirements.txt
```

Download the spaCy language model

```bash
python -m spacy download en_core_web_sm
```

Run the application

```bash
streamlit run app.py
```

---

## 📂 Supported Resume Information

The parser currently extracts:

- Personal Details
- Skills
- Education
- Experience
- Projects
- Certifications
- Resume Score
- Improvement Suggestions

---

## 📊 Resume Scoring

The application evaluates resumes based on:

- Contact Information
- Skills
- Education
- Experience
- Projects
- Certifications
- GitHub & LinkedIn Profile
- Overall Resume Completeness

---

## 📤 Export Options

Users can download the extracted information as:

- JSON
- CSV

---

## 🔮 Future Enhancements

- Job Description Matching (ATS)
- Resume Keyword Optimization
- Multiple Resume Comparison
- DOCX Support
- OCR Support for Image-based PDFs
- AI-powered Resume Feedback
- Skill Categorization
- Experience Timeline Visualization
- Dark Mode
- Resume Ranking

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork this repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Rajanya Saha**

AI & ML Undergraduate

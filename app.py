import streamlit as st
import tempfile
import json
import pandas as pd

from parser import ResumeParser
from extractor import ResumeExtractor
from scorer import ResumeScorer


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")

st.caption(
    "Upload a resume and extract structured information using NLP."
)

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)
if uploaded_file:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp:

        temp.write(uploaded_file.read())

        temp_path = temp.name
        
    parser = ResumeParser(temp_path)

    parsed = parser.parse()

    extractor = ResumeExtractor(
        parsed["text"],
        parsed["links"]
    )

    data = extractor.extract_all()

    scorer = ResumeScorer(data)

    score = scorer.calculate_score()
    
    col1, col2 = st.columns([2,1])
    with col1:

        st.header("👤 Personal Information")

        st.write("**Name:**", data["Name"])

        st.write("**Email:**", data["Email"])

        st.write("**Phone:**", data["Phone"])

        st.write("**LinkedIn:**", data["LinkedIn"])

        st.write("**GitHub:**", data["GitHub"])

        st.write("**Portfolio:**", data["Portfolio"])
    
        st.header("🛠 Skills")

        if data["Skills"]:

            st.write(", ".join(data["Skills"]))

        else:
            st.warning("No skills detected.")
    
        st.header("🎓 Education")

        for item in data["Education"]:

            st.write("•", item)
    
        st.header("💼 Experience")

        for item in data["Experience"]:

            st.write("•", item)
        st.header("📂 Projects")

        if data["Projects"]:

            for item in data["Projects"]:

                st.write("•", item)

        else:

            st.info("No projects detected.")
        
        st.header("📜 Certifications")

        if data["Certifications"]:

            for item in data["Certifications"]:

                st.write("•", item)

        else:

            st.info("No certifications detected.")
            
    with col2:

        st.metric(
            "Resume Score",
            score["Resume Score"]
    )

        st.subheader("Suggestions")

        for remark in score["Remarks"]:

            st.write("•", remark)
            
        st.download_button(
            "⬇ Download JSON",
            json.dumps(
            data,
            indent=4),
            file_name="parsed_resume.json",
            key="download_json"
        )
        
    df = pd.DataFrame(
    dict(
        [(k, [v]) for k, v in data.items()]
    )
)

    csv = df.to_csv(index=False)

    st.download_button(
    "⬇ Download CSV",
    csv,
     key="download_csv",
    file_name="parsed_resume.csv"
)
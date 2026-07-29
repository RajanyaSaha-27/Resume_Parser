from parser import ResumeParser
from extractor import ResumeExtractor

parser = ResumeParser("assets/sample_resume.pdf")

data = parser.parse()

extractor = ResumeExtractor(
    text=data["text"],
    links=data["links"]
)

result = extractor.extract_all()

for key, value in result.items():
    print(f"\n{key}")
    print(value)
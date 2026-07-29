from parser import ResumeParser
from extractor import ResumeExtractor
from scorer import ResumeScorer

parser = ResumeParser("assets/sample_resume.pdf")

parsed = parser.parse()

extractor = ResumeExtractor(
    parsed["text"],
    parsed["links"]
)

data = extractor.extract_all()

scorer = ResumeScorer(data)

score = scorer.calculate_score()

print(score)

print()

print("Missing Sections")

print(scorer.missing_sections())
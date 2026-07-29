from parser import ResumeParser

parser = ResumeParser("assets/sample_resume.pdf")

data = parser.parse()

print("=" * 80)
print("TEXT")
print("=" * 80)
print(data["text"])

print("\n")

print("=" * 80)
print("LINKS")
print("=" * 80)
print(data["links"])

print("\n")

print("=" * 80)
print("METADATA")
print("=" * 80)
print(data["metadata"])
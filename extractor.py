import re
import spacy

nlp = spacy.load("en_core_web_sm")


class ResumeExtractor:

    def __init__(self, text: str, links=None):

        self.text = text
        self.links = links if links else []
        self.doc = nlp(text)

    # ----------------------------------------------------
    # Name
    # ----------------------------------------------------

    def extract_name(self):

        for ent in self.doc.ents:
            if ent.label_ == "PERSON":
                return ent.text

        return "Not Found"

    # ----------------------------------------------------
    # Email
    # ----------------------------------------------------
    
    def extract_email(self):

        for link in self.links:

            if link.startswith("mailto:"):
                return link.replace("mailto:", "")

        pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

        match = re.search(pattern, self.text)

        return match.group(0) if match else "Not Found"
    
    # def extract_email(self):

        text = self.text

        # Join broken emails
        text = text.replace("\n", "")
        text = re.sub(r"\s*@\s*", "@", text)
        text = re.sub(r"\s+", "", text)

        pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

        match = re.search(pattern, text)

        return match.group(0) if match else "Not Found"


    # def extract_email(self):

        pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

        match = re.search(pattern, self.text)

        return match.group(0) if match else "Not Found"
    # def extract_email(self):

    # Normalize whitespace/newlines
        text = re.sub(r"\s+", "", self.text)

        pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

        match = re.search(pattern, text)

        return match.group(0) if match else "Not Found"
    # ----------------------------------------------------
    # Phone
    # ----------------------------------------------------

    def extract_phone(self):

        pattern = r"(\+\d{1,3}[\s-]?)?(\(?\d{2,5}\)?[\s-]?)?\d{3,5}[\s-]?\d{3,5}"

        match = re.search(pattern, self.text)

        return match.group(0).strip() if match else "Not Found"

    # ----------------------------------------------------
    # LinkedIn
    # ----------------------------------------------------

    def extract_linkedin(self):

        # Search hyperlinks first

        for link in self.links:

            if "linkedin.com" in link.lower():
                return link

        # Search visible text

        pattern = r"(https?://)?(www\.)?linkedin\.com/[^\s]+"

        match = re.search(
            pattern,
            self.text,
            re.IGNORECASE
        )

        return match.group(0) if match else "Not Found"

    # ----------------------------------------------------
    # GitHub
    # ----------------------------------------------------

    def extract_github(self):

        for link in self.links:

            if "github.com" in link.lower():
                return link

        pattern = r"(https?://)?(www\.)?github\.com/[^\s]+"

        match = re.search(
            pattern,
            self.text,
            re.IGNORECASE
        )

        return match.group(0) if match else "Not Found"

    # ----------------------------------------------------
    # Portfolio
    # ----------------------------------------------------

    def extract_portfolio(self):

        ignore = [
            "linkedin.com",
            "github.com"
        ]

        for link in self.links:

            if not any(site in link.lower() for site in ignore):
                return link

        urls = re.findall(
            r"https?://[^\s]+",
            self.text
        )

        for url in urls:

            if not any(site in url.lower() for site in ignore):
                return url

        return "Not Found"

    # ----------------------------------------------------
    # Skills
    # ----------------------------------------------------

    def extract_skills(self):

        try:

            with open(
                "data/skills.txt",
                "r",
                encoding="utf-8"
            ) as f:

                skills_db = [
                    skill.strip().lower()
                    for skill in f.readlines()
                    if skill.strip()
                ]

        except:

            return []

        found = set()

        text = self.text.lower()

        for skill in skills_db:

            if re.search(
                rf"\b{re.escape(skill)}\b",
                text
            ):
                found.add(skill.title())

        return sorted(found)

    # ----------------------------------------------------
    # Education
    # ----------------------------------------------------

    def extract_education(self):

        keywords = [

            "b.tech",
            "bachelor",
            "master",
            "m.tech",
            "phd",
            "diploma",
            "college",
            "university",
            "school"

        ]

        education = []

        lines = self.text.splitlines()

        for line in lines:

            if any(
                key in line.lower()
                for key in keywords
            ):
                education.append(line.strip())

        return education

    # ----------------------------------------------------
    # Experience
    # ----------------------------------------------------

    def extract_experience(self):

        experience = []

        lines = self.text.splitlines()

        for line in lines:

            if re.search(
                r"\b\d+\+?\s+years?\b",
                line.lower()
            ):
                experience.append(line.strip())

        return experience

    # ----------------------------------------------------
    # Projects
    # ----------------------------------------------------

    def extract_projects(self):

        projects = []

        lines = self.text.splitlines()

        capture = False

        for line in lines:

            if "project" in line.lower():

                capture = True
                continue

            if capture:

                if line.strip() == "":
                    break

                projects.append(line.strip())

        return projects

    # ----------------------------------------------------
    # Certifications
    # ----------------------------------------------------

    def extract_certifications(self):

        certs = []

        lines = self.text.splitlines()

        for line in lines:

            if any(
                word in line.lower()
                for word in [
                    "certificate",
                    "certification",
                    "certified"
                ]
            ):

                certs.append(line.strip())

        return certs

    # ----------------------------------------------------
    # Summary
    # ----------------------------------------------------

    def extract_all(self):

        return {

            "Name": self.extract_name(),

            "Email": self.extract_email(),

            "Phone": self.extract_phone(),

            "LinkedIn": self.extract_linkedin(),

            "GitHub": self.extract_github(),

            "Portfolio": self.extract_portfolio(),

            "Skills": self.extract_skills(),

            "Education": self.extract_education(),

            "Experience": self.extract_experience(),

            "Projects": self.extract_projects(),

            "Certifications": self.extract_certifications()

        }
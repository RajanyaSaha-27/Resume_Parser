class ResumeScorer:

    def __init__(self, data):

        self.data = data

    # -----------------------------------------
    # Score Resume
    # -----------------------------------------

    def calculate_score(self):

        score = 0

        remarks = []

        # ----------------------------
        # Personal Information
        # ----------------------------

        if self.data["Name"] != "Not Found":
            score += 5
        else:
            remarks.append("Name not found")

        if self.data["Email"] != "Not Found":
            score += 5
        else:
            remarks.append("Email missing")

        if self.data["Phone"] != "Not Found":
            score += 5
        else:
            remarks.append("Phone number missing")

        if self.data["LinkedIn"] != "Not Found":
            score += 5
        else:
            remarks.append("Add LinkedIn profile")

        if self.data["GitHub"] != "Not Found":
            score += 5
        else:
            remarks.append("Add GitHub profile")

        # ----------------------------
        # Resume Sections
        # ----------------------------

        if len(self.data["Skills"]) > 0:
            score += 20
        else:
            remarks.append("No technical skills detected")

        if len(self.data["Education"]) > 0:
            score += 15
        else:
            remarks.append("Education section missing")

        if len(self.data["Experience"]) > 0:
            score += 15
        else:
            remarks.append("Experience section missing")

        if len(self.data["Projects"]) > 0:
            score += 15
        else:
            remarks.append("Projects section missing")

        if len(self.data["Certifications"]) > 0:
            score += 10
        else:
            remarks.append("Consider adding certifications")

        # ----------------------------
        # Resume Strength
        # ----------------------------

        skills = len(self.data["Skills"])

        if skills >= 15:
            score += 10

        elif skills >= 10:
            score += 7

        elif skills >= 5:
            score += 5

        return {

            "Resume Score": min(score, 100),

            "Remarks": remarks

        }

    # -----------------------------------------
    # Missing Sections
    # -----------------------------------------

    def missing_sections(self):

        missing = []

        for key in [

            "Skills",

            "Education",

            "Experience",

            "Projects",

            "Certifications"

        ]:

            if len(self.data[key]) == 0:

                missing.append(key)

        return missing
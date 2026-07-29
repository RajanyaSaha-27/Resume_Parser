import fitz  # PyMuPDF
import os


class ResumeParser:
    def __init__(self, file_path: str):
        self.file_path = os.path.abspath(file_path)

    # -------------------------------------
    # Validate File
    # -------------------------------------

    def _validate(self):

        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(
                f"File not found: {self.file_path}"
            )

    # -------------------------------------
    # Extract Resume Text
    # -------------------------------------

    def extract_text(self):

        self._validate()

        text = ""

        with fitz.open(self.file_path) as pdf:

            for page in pdf:

                text += page.get_text("text") + "\n"

        return text.strip()

    # -------------------------------------
    # Extract Hyperlinks
    # -------------------------------------

    def extract_links(self):

        self._validate()

        links = []

        with fitz.open(self.file_path) as pdf:

            for page in pdf:

                page_links = page.get_links()

                for link in page_links:

                    uri = link.get("uri")

                    if uri:
                        links.append(uri)

        return list(dict.fromkeys(links))

    # -------------------------------------
    # Metadata
    # -------------------------------------

    def extract_metadata(self):

        self._validate()

        with fitz.open(self.file_path) as pdf:

            meta = pdf.metadata

        return meta

    # -------------------------------------
    # Everything
    # -------------------------------------

    def parse(self):

        return {

            "text": self.extract_text(),

            "links": self.extract_links(),

            "metadata": self.extract_metadata()

        }
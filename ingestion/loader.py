from pathlib import Path
from pypdf import PdfReader


def load_documents(folder="data/documents"):

    docs = []

    for file in Path(folder).glob("*"):

        # TEXT FILES
        if file.suffix == ".txt":
            with open(file, "r", encoding="utf-8") as f:
                docs.append(f.read())

        # PDF FILES
        elif file.suffix == ".pdf":

            reader = PdfReader(file)

            text = ""

            for page in reader.pages:
                text += page.extract_text()

            docs.append(text)

    return docs
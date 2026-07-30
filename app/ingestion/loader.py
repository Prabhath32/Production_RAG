import fitz
from pathlib import Path

from app.config import PDF_DIRECTORY


class PDFLoader:
    """
    Loads all PDF files from the configured directory and extracts text
    page by page while preserving metadata.
    """

    def __init__(self, pdf_directory=PDF_DIRECTORY):
        self.pdf_directory = Path(pdf_directory)

    def load_documents(self):
        """
        Returns:
            List[dict]:
            [
                {
                    "document": "sample.pdf",
                    "page": 1,
                    "text": "Page content..."
                }
            ]
        """

        documents = []

        pdf_files = list(self.pdf_directory.glob("*.pdf"))

        if not pdf_files:
            raise FileNotFoundError(
                f"No PDF files found in: {self.pdf_directory}"
            )

        print(f"\nFound {len(pdf_files)} PDF(s).\n")

        total_pages = 0

        for pdf_file in pdf_files:

            print(f"Reading: {pdf_file.name}")

            pdf = fitz.open(pdf_file)

            for page_number, page in enumerate(pdf, start=1):

                text = page.get_text("text")

                if text.strip():

                    documents.append(
                        {
                            "document": pdf_file.name,
                            "page": page_number,
                            "text": text
                        }
                    )

                    total_pages += 1

            pdf.close()

        print(f"\nTotal Pages Loaded: {total_pages}")

        return documents
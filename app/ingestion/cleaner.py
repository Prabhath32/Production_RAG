import re


class TextCleaner:
    """
    Cleans raw text extracted from PDF pages.
    """

    @staticmethod
    def clean(text: str) -> str:
        """
        Clean the extracted text.

        Steps:
        1. Remove extra spaces
        2. Remove extra blank lines
        3. Remove tabs
        4. Strip leading/trailing whitespace
        """

        if not text:
            return ""

        # Replace tabs with spaces
        text = text.replace("\t", " ")

        # Remove multiple spaces
        text = re.sub(r"[ ]{2,}", " ", text)

        # Remove multiple blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)

        # Remove trailing spaces at the end of lines
        text = "\n".join(line.strip() for line in text.splitlines())

        # Remove leading/trailing whitespace
        text = text.strip()

        return text

    def clean_documents(self, documents):
        """
        Clean all extracted pages while preserving metadata.
        """

        cleaned_documents = []

        for document in documents:

            cleaned_text = self.clean(document["text"])

            if cleaned_text:

                cleaned_documents.append(
                    {
                        "document": document["document"],
                        "page": document["page"],
                        "text": cleaned_text
                    }
                )

        print(f"Total Cleaned Pages : {len(cleaned_documents)}")

        return cleaned_documents
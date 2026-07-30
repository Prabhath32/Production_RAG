import tiktoken

from app.config import CHUNK_SIZE, CHUNK_OVERLAP


class TextChunker:
    """
    Token-based chunker that preserves paragraph boundaries
    whenever possible.
    """

    def __init__(self):
        self.encoding = tiktoken.get_encoding("cl100k_base")

    def count_tokens(self, text: str) -> int:
        return len(self.encoding.encode(text))

    def split_large_paragraph(self, paragraph: str):
        """
        Split a paragraph that exceeds the chunk size.
        """

        tokens = self.encoding.encode(paragraph)

        chunks = []

        start = 0

        while start < len(tokens):

            end = start + CHUNK_SIZE

            chunk = self.encoding.decode(tokens[start:end])

            chunks.append(chunk)

            start += CHUNK_SIZE - CHUNK_OVERLAP

        return chunks

    def chunk_documents(self, documents):

        all_chunks = []

        chunk_id = 1

        for document in documents:

            paragraphs = [
                p.strip()
                for p in document["text"].split("\n\n")
                if p.strip()
            ]

            current_chunk = ""

            current_tokens = 0

            for paragraph in paragraphs:

                paragraph_tokens = self.count_tokens(paragraph)

                # Paragraph is too large
                if paragraph_tokens > CHUNK_SIZE:

                    if current_chunk:

                        all_chunks.append({
                            "document": document["document"],
                            "page": document["page"],
                            "chunk": chunk_id,
                            "text": current_chunk.strip()
                        })

                        chunk_id += 1

                        current_chunk = ""
                        current_tokens = 0

                    split_chunks = self.split_large_paragraph(paragraph)

                    for piece in split_chunks:

                        all_chunks.append({
                            "document": document["document"],
                            "page": document["page"],
                            "chunk": chunk_id,
                            "text": piece.strip()
                        })

                        chunk_id += 1

                    continue

                # Paragraph fits into current chunk
                if current_tokens + paragraph_tokens <= CHUNK_SIZE:

                    current_chunk += "\n\n" + paragraph

                    current_tokens += paragraph_tokens

                else:

                    all_chunks.append({
                        "document": document["document"],
                        "page": document["page"],
                        "chunk": chunk_id,
                        "text": current_chunk.strip()
                    })

                    chunk_id += 1

                    current_chunk = paragraph

                    current_tokens = paragraph_tokens

            if current_chunk:

                all_chunks.append({
                    "document": document["document"],
                    "page": document["page"],
                    "chunk": chunk_id,
                    "text": current_chunk.strip()
                })

                chunk_id += 1

        print(f"\nTotal Chunks Created : {len(all_chunks)}")

        return all_chunks
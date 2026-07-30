class PromptBuilder:

    @staticmethod
    def build_prompt(
        question: str,
        retrieved_chunks
    ) -> str:

        context = ""

        sources = []

        for result in retrieved_chunks:

            payload = result.payload

            context += f"""
Document : {payload['document']}
Page : {payload['page']}
Chunk : {payload['chunk']}

Content:
{payload['text']}

--------------------------------------------------

"""

            sources.append(
                f"{payload['document']} (Page {payload['page']})"
            )

        prompt = f"""
You are an AI Assistant.

Answer ONLY using the information present in the provided context.

If the answer is not available in the context,
reply with:

"I couldn't find that information in the provided documents."

Do not make assumptions.

==========================
CONTEXT
==========================

{context}

==========================
QUESTION
==========================

{question}

==========================
ANSWER
==========================

Provide a clear and concise answer.

After the answer mention the sources used.
"""

        return prompt
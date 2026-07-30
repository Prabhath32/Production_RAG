from openai import AzureOpenAI

from app.config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT
)


class AzureOpenAIClient:

    def __init__(self):

        self.client = AzureOpenAI(

            azure_endpoint=AZURE_OPENAI_ENDPOINT,

            api_key=AZURE_OPENAI_API_KEY,

            api_version=AZURE_OPENAI_API_VERSION

        )

    def generate_answer(self, prompt: str) -> str:

        response = self.client.chat.completions.create(

            model=AZURE_OPENAI_DEPLOYMENT,

            messages=[

                {
                    "role": "system",
                    "content": (
                        "You are an AI assistant. "
                        "Answer only using the provided context. "
                        "If the answer is not present in the context, "
                        "say 'I couldn't find that information in the documents.'"
                    )
                },

                {
                    "role": "user",
                    "content": prompt
                }

            ],

            temperature=0

        )

        return response.choices[0].message.content
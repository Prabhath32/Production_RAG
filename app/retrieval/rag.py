from app.retrieval.retriever import Retriever
from app.retrieval.prompt import PromptBuilder
from app.llm.azure_openai import AzureOpenAIClient


class RAGPipeline:

    def __init__(self):

        print("Initializing RAG Pipeline...\n")

        self.retriever = Retriever()

        self.llm = AzureOpenAIClient()

        print("RAG Pipeline Ready.\n")

    def ask(self, question: str):

        print("=" * 70)
        print("User Question :", question)
        print("=" * 70)

        # Step 1 : Retrieve Relevant Chunks
        retrieved_chunks = self.retriever.retrieve(question)

        print(f"\nRetrieved {len(retrieved_chunks)} chunks.\n")

        # Step 2 : Build Prompt
        prompt = PromptBuilder.build_prompt(
            question=question,
            retrieved_chunks=retrieved_chunks
        )

        # Step 3 : Generate Answer
        answer = self.llm.generate_answer(prompt)

        return answer, retrieved_chunks
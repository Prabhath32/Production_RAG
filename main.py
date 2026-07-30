from app.retrieval.rag import RAGPipeline


def main():

    print("=" * 70)
    print("        COMPANY KNOWLEDGE BASE - RAG CHATBOT")
    print("=" * 70)

    rag = RAGPipeline()

    while True:

        question = input("\nAsk a Question (type 'exit' to quit): ")

        if question.lower() == "exit":
            print("\nGoodbye!")
            break

        answer, retrieved_chunks = rag.ask(question)

        print("\n" + "=" * 70)
        print("ANSWER")
        print("=" * 70)
        print(answer)

        print("\n" + "=" * 70)
        print("SOURCES")
        print("=" * 70)

        for index, result in enumerate(retrieved_chunks, start=1):

            payload = result.payload

            print(
                f"{index}. "
                f"{payload['document']} "
                f"(Page {payload['page']}, "
                f"Chunk {payload['chunk']}) "
                f"| Score: {result.score:.4f}"
            )


if __name__ == "__main__":
    main()
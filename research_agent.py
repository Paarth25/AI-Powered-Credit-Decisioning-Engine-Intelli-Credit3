from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.docstore.document import Document
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

class ResearchAgent:

    def __init__(self, documents):
        self.embeddings = OpenAIEmbeddings()
        docs = [Document(page_content=d) for d in documents]
        self.db = FAISS.from_documents(docs, self.embeddings)

    def query(self, question):
        docs = self.db.similarity_search(question)
        context = "\n".join([doc.page_content for doc in docs])

        prompt = f"""
        Based on the context below, identify risks and litigation concerns.

        Context:
        {context}

        Question:
        {question}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content
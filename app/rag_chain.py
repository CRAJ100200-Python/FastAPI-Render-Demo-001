from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0
)

def format_docs(docs):
    formatted = []
    for doc in docs:
        if hasattr(doc, "page_content"):
            formatted.append(doc.page_content)
        else:
            formatted.append(doc)
    return "\n\n".join(formatted)

def build_rag_chain(retriever=None):
    prompt = ChatPromptTemplate.from_template("""
You are an HR assistant. Answer ONLY from the context.

Rules:
- Do not use outside knowledge
- If answer is not found, say "Not mentioned"

Context:
{context}

Question:
{question}
""")

    if retriever:
        return (
            {
                "context": retriever | format_docs,
                "question": lambda x: x
            }
            | prompt
            | llm
            | StrOutputParser()
        )
    else:
        return prompt | llm | StrOutputParser()
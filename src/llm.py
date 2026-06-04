from langchain_groq import ChatGroq

def get_llm():
    llm = ChatGroq(
        model_name = "llama-3.3-70b-versatile",
        temperature = 0.7
    )
    return llm

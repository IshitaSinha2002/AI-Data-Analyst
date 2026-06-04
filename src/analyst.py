from langchain_core.prompts import ChatPromptTemplate
from typer import prompt
from src import llm
from src.prompts import SYSTEM_PROMPT

def create_chain(llm):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            ("human", """
        Dataset columns: {columns}
        Sample data: {sample_data}
        Question: {question}
        """)
        ]
    )

    chain = prompt | llm
    return chain
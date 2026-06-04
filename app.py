from dotenv import load_dotenv
from src.llm import get_llm
from src.csv_loader import load_csv
from src.analyst import create_chain
from src.executor import execute_query

load_dotenv()

def main():
    file_path = input("Enter CSV path: ")
    df = load_csv(file_path)
    print("\nData loaded successfully!")
    llm = get_llm()
    chain = create_chain(llm)
    while True:
        question = input("\nEnter your question:\n")
        if question.lower() == "exit":
            break
        response = execute_query(chain, df, question)
        print("\nResponse:\n", response)
    
if __name__ == "__main__":
    main()
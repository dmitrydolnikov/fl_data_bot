import warnings
import matplotlib
matplotlib.use("Agg")
warnings.filterwarnings("ignore", category=UserWarning)
import pandas as pd
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import argparse
EXIT_COMMANDS = {"q", "quit", "exit", "cancel", "end"}

load_dotenv()
key = os.getenv("QWEN_API_KEY")
if not key:
    raise ValueError("Put QWEN_API_KEY=sk-xxxxxxxxxx into .env file")
llm = ChatOpenAI(
    model="qwen-max",
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
    temperature=0.0,
    api_key=key
)

data_file_path = "./data/freelancer_earnings_bd.csv"
df = pd.read_csv(data_file_path)



def ask_question(agent, question: str):
    #print("\n🔍 Question:", question)
    try:
        answer = agent.invoke(question)
        print("🧠 Answer:", answer["output"])
    except Exception as e:
        print(f"⚠️ Error while processing: {e}")

def main():
    parser = argparse.ArgumentParser(description="Ask questions about freelancer earnings data.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("question", nargs="*", help="Question to ask (optional, enter interactive mode if omitted)")
    args = parser.parse_args()

    agent = create_pandas_dataframe_agent(
        llm,
        df,
        agent_type="tool-calling",  # Use the modern "tool-calling" agent type
        allow_dangerous_code=True,  # Allow execution of Python code (use with caution)
        verbose=args.verbose,  # Enable verbose logging for debugging
    )

    response = agent.invoke("What are the columns in the dataset and their data types?")
    print(response["output"])


    if args.question:
        ask_question(agent, args.question)
        return

    print("📊 Freelancer Insights CLI")
    print("Type your question below (e.g. in English or Russian).")
    print("Type 'exit', 'quit', 'q', or 'cancel' to end.\n")
    print("Use -v or --verbose for detailed output.")
    print("example questions: \n")
    print("how much more profitable freelancers taking crypto?")
    print("How many freelancers are there in the dataset?")
    print("What is the distribution of earnings among freelancers?")
    print("how many freelancers there are per client country?")
    print("What is the average earnings per freelancer in the USA?")
    print("Насколько выше доход у фрилансеров, принимающих оплату в криптовалюте, по сравнению с другими способами оплаты??")
    print("Как распределяется доход фрилансеров в зависимости от региона проживания?")
    print("Какой процент фрилансеров, считающих себя экспертами, выполнил менее 100 проектов?")

    try:
        while True:
            user_input = input("❓ Your question: ").strip()
            if user_input.lower() in EXIT_COMMANDS:
                print("👋 Goodbye!")
                break
            if user_input:
                ask_question(agent, user_input + " ; do not attempt to use plotly or matplotlib, just return the data")
    except KeyboardInterrupt:
        print("\n👋 Exiting on Ctrl+C. Goodbye!")
    except EOFError:
        print("\n👋 Exiting on EOF. Goodbye!")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
import sys
from src.llm.analyzer import BugAnalyzer


def main():

    analyzer = BugAnalyzer()

    print("\n=== AI Bug Analyzer ===\n")

    while True:

        error = input("Enter error log (or type 'exit'): ")

        if error.lower() == "exit":
            break

        print("\nAnalyzing...\n")

        result = analyzer.analyze(error)

        print(result)

        print("\n" + "-" * 50 + "\n")


if __name__ == "__main__":
    main()
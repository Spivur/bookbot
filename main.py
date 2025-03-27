from stats import get_num_words
from stats import get_num_characters
from stats import print_report
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        try:
            num_words = get_num_words(get_book_text(sys.argv[1]))
            print("============ BOOKBOT ============")
            print(f"Analyzing book found at {sys.argv[1]}...")
            print("----------- Word Count ----------")
            print(f"Found {num_words} total words")
            print("--------- Character Count -------")
            for row in print_report(get_num_characters(get_book_text(sys.argv[1]))):
                print(f"{row["key"]}: {row["value"]}\n")
            print("============= END ===============")
        except FileNotFoundError as e:
            print(e)

main()
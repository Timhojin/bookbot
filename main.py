from stats import get_num_words, count_characters, rsort_by_num
import sys

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    content = get_book_text(file_path)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    num_of_words = get_num_words(content)
    counted_chars = count_characters(content)
    num_of_chars = rsort_by_num(counted_chars)

    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for index in num_of_chars:
        print(f"{index["name"]}: {index["num"]}")
    print("============= END ===============")

main()
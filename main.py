from stats import count_words, count_chars, sort_chars
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book_content = get_book_text(path)
    word_count = count_words(book_content)
    char_counts = count_chars(book_content)
    chars_sorted = sort_chars(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in chars_sorted:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END =============")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

main()


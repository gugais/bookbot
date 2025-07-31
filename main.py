import sys
from stats import count_words, get_char_counts, sort_char_counts

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    text = get_book_text(filepath)
    num_words = count_words(text)
    counts_chars = get_char_counts(text)
    sorted_counts = sort_char_counts(counts_chars)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print(f"{counts_chars}")
    print(f"{sorted_counts}")
    for char, count in sorted_counts:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()

from stats import count_every_char, words_count, sorting_dictionary, sort_on
import sys


def get_boot_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        book_text = get_boot_text(book_path)
        words_total = words_count(book_text)
        every_char = count_every_char(book_text)
        dictionary_to_sort = sorting_dictionary(every_char)
        dictionary_to_sort.sort(key=sort_on, reverse=True)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {words_total} total words")
        print("--------- Character Count -------")
        for item in dictionary_to_sort:
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")

main()

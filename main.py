from stats import count_every_char, words_count


def get_boot_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    book_text = get_boot_text("books/frankenstein.txt")
    words_total = words_count(book_text)

    print(f"Found {words_total} total words")
    print(50 * "-")
    print(count_every_char(book_text))

main()

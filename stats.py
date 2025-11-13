def words_count(text):
    count = 0
    for word in text.split():
        count += 1

    return count

def count_every_char(text):
    every_char = set()
    for word in text.split():
        for ch in word:
            every_char.add(ch.lower())

    every_char_count = {}

    for symbol in every_char:
        count = 0
        for word in text.split():
            for ch in word:
                if ch.lower() == symbol:
                    count += 1
        every_char_count[symbol] = count

    return every_char_count


from string import ascii_lowercase

with open("wordle-words.txt", "w") as write_file:
    with open("enwiki-20190320-words-frequency.txt") as read_file:
        for line in read_file:
            word, count = line.split()
            if len(word) == 5 and all([l in ascii_lowercase for l in word]):
                write_file.write(word + "\n")

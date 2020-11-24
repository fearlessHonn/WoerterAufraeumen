# coding=utf8
import io

path = input("Dateipfad zum Beispiel eingeben: ")
text_read = io.open(path, mode="r", encoding="utf-8")

text = text_read.read()
text_copy = text.split('\n', 1)[0]
text = text.replace("!", "")
text = text.replace(".", "")
text = text.replace("?", "")
text = text.replace(",", "")

every = [text]
every = [z for item in every for z in item.split()]
gaps = []
words = []
i = 0


def all_same(items):
    return all(x == items[0] for x in items)


for t in every:
    if i < len(every) / 2:
        gaps.append(t)
    else:
        words.append(t)
    i += 1

sol = [0] * len(gaps)
av_gaps = gaps.copy()
av_words = words.copy()
run = True
while run:
    run = False
    for gap_pos, gap in enumerate(gaps):
        pos = []
        for word in words:
            if gap in av_gaps and word in av_words:
                possible = False
                if len(gap) == len(word):
                    possible = True
                    for space, letter in zip(gap, word):
                        if space != letter and space != "_":
                            possible = False
                if possible:
                    pos.append(word)
            else:
                possible = False
        if all_same(pos) and pos:
            sol[gap_pos] = pos[0]
            av_gaps.remove(gap)
            av_words.remove(pos[0])
            run = True
for word_pos, word in enumerate(sol):
    text_copy = text_copy.replace(gaps[word_pos], word, 1)
print("Die Lösung lautet: " + str(text_copy))
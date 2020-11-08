import codecs
import nltk
import re


report = codecs.open("realtime_stemming.txt", "w+", encoding='utf-8')
total = 0


def remove_stemms(n):
    global total
    suffixes = "suffixes.txt"
    doc = str(n) + ".txt"
    stemmed_bag_of_words = str(n) + "_out_1.txt"

    stemmed_bow = codecs.open(stemmed_bag_of_words, "w+", encoding='utf-8')

    doc = [unicode(l.strip(), 'utf-8') for l in open(doc)]
    text = " ".join(doc)

    # tokenize the string
    tokens = nltk.word_tokenize(text)

    # remove all unnessary chars
    # get only sinhala unicode charactors
    regex = re.compile(u'[^\u0D80-\u0DFF]', re.UNICODE)
    tokens = [regex.sub('', w) for w in tokens]
    tokens = filter(None, tokens)

    tokens = list(set(tokens))  # this will remove duplicates
    bag_of_words = sorted(tokens)

    # read all suffixes list
    suffixes = [unicode(l.strip(), 'utf-8') for l in open(suffixes)]
    suffixes = filter(None, suffixes)
    suffixes.sort(lambda x, y: cmp(len(y), len(x)))

    prev = ""
    stems = {}
    found = 0
    for w in bag_of_words:
        if prev != "":
            found = 0
            for suf in suffixes:
                if prev + suf == w:
                    stems[w] = prev
                    stemmed_bow.write(w + ", " + prev + "\n")
                    found = 1
                    break
        if found == 0:
            prev = w
            stemmed_bow.write(prev + "\n")

    report.write("doc" + str(n) + "\n")
    report.write("Total tokens: " + str(len(tokens)) + "\n")
    report.write("Stemmed tokens : " + str(len(stems)) + "\n")

    pre = 100.0 * len(stems) / len(tokens)
    total = total + pre

    report.write("Stemmed presentage : " + str(pre) + "\n")
    report.write("\n\n")

    # close file
    stemmed_bow.close()


remove_stemms(1)


report.write("Average : " + str(1.0 * total / 5) + "\n")
report.close()

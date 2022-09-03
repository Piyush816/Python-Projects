import random
import pyperclip

wordList = ["Morbi", "quis", "tortor", "quis", "diam", "sodales", "mattis", "a", "id", "elit.", "In", "hac", "habitasse", "platea", "dictumst.", "Sed", "at", "arcu", "vitae", "nibh", "consequat", "bibendum", "eu", "nec", "libero.", "Vestibulum", "sit", "amet", "mi", "non", "urna", "auctor", "maximus", "non", "id", "ipsum.", "Sed", "vel", "justo", "nec", "nisi", "placerat", "porta.", "Praesent", "viverra", "eros", "vel", "dolor", "iaculis,", "ac", "aliquam", "elit", "pretium.", "Aenean", "molestie", "dui", "sollicitudin,", "scelerisque", "ex", "eget,", "efficitur", "diam.", "Proin", "velit,",
            "venenatis", "ac", "laoreet", "vel,", "volutpat", "vitae", "mauris.", "Phasellus", "eros", "turpis,", "viverra", "non", "fermentum", "sed,", "laoreet", "hendrerit", "mi.", "Donec", "lorem", "urna,", "finibus", "at", "eleifend", "non,", "ultricies" "sit", "amet", "lectus.", "Nunc", "non", "mauris", "vitae", "lectus", "placerat", "rutrum"]


def textGenerator(noOfWords):
    text = ""
    for i in range(noOfWords):
        text += wordList[random.randrange(0, len(wordList)-1)]+" "

    return text


if __name__ == "__main__":
    try:
        noOfWords = int(input("How many words you want: "))
        pyperclip.copy(textGenerator(noOfWords))
    except:
        print("Invalid Input!")

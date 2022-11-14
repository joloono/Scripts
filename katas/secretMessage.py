LOW_COUNT = 1
MSG = "There is a secret message in the first six sentences of this kata description. " \
      "Have you ever felt like there was something more being said? Was it hard to figure out that unspoken meaning? " \
      "Never again! Never will a secret go undiscovered. Find all duplicates from our message!"


def findSecretSauce(txt: str) -> str:
    """ put in text to analyse """

    secretMessage = ""
    indices = []
    wordsList = [word.lower().strip("!,. ") for word in txt.split()]

    # find secret message if there is any
    for i, word in enumerate(wordsList):
        splitPart = i + 1
        if LOW_COUNT < wordsList.count(word):
            if word in wordsList[splitPart:]:
                indices.append(wordsList[splitPart:].index(word) + splitPart)

    indices.sort()
    for i in indices:
        secretMessage += " " + wordsList[i]

    return secretMessage.strip(" ")


if __name__ == "__main__":
    print(findSecretSauce(MSG))

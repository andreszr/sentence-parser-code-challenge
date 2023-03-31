def replace_sentence(sentence):
    def process_word(word):
        if len(word) <= 2:
            return word
        else:
            return f"{word[0]}{len(set(word[1:-1]))}{word[-1]}"

    result = []
    word = ""
    for char in sentence:
        if char.isalpha():
            word += char
        else:
            result.append(process_word(word))
            result.append(char)
            word = ""

    result.append(process_word(word))

    return "".join(result)
import re


def extract_words_with_inner_capital(text):
    return sorted(re.findall(r'\b\w*[A-Z]\w*\b', text))


def split_paragraphs(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().split('\n\n')


def correct_word(word):
    return word[0] + word[1:].lower()


def correct_text(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    wrong_words = extract_words_with_inner_capital(content)
    corrected_text = content

    for word in wrong_words:
        corrected_text = re.sub(rf'\b{re.escape(word)}\b', correct_word(word), corrected_text)

    with open('output.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(corrected_text)

    return corrected_text


# Example usage:
if __name__ == "__main__":
    filename = 'input.txt'  # Replace with your input file name
    paragraphs = split_paragraphs(filename)
    first_paragraph = paragraphs[0]
    print(first_paragraph)
    wrong_words = extract_words_with_inner_capital(first_paragraph)
    print(wrong_words)
    correct_first_paragraph = correct_text(filename)

import pytest
from text_analizer import extract_words_with_inner_capital, split_paragraphs, correct_text

# First paragraph from the previously generated text
sample_text = """
Once upon a time in a faraway lanD, there lived a King and QueEn who ruled over a Prosperous kingdom. theIr reign was marked by peaCe and harMony, and the people loved thEm dearly. However, the King had a seCret that he had Kept from everyone, including his belOved wife.
"""

def test_extract_words_with_inner_capital():
    expected_result = ['QueEn', 'belOved', 'harMony', 'lanD', 'peaCe', 'seCret', 'thEm', 'theIr']
    result = extract_words_with_inner_capital(sample_text)
    assert result == expected_result

def test_extract_words_empty_text():
    empty_text = ""
    expected_result = []
    result = extract_words_with_inner_capital(empty_text)
    assert result == expected_result

def test_extract_words_no_inner_capital():
    text = "This text has no inner capital letters."
    expected_result = []
    result = extract_words_with_inner_capital(text)
    assert result == expected_result

def test_correct_text(tmpdir):
    # Create a temporary input file
    input_text = """
    Once upon a time in a faraway lanD, there lived a King and QueEn who ruled over a Prosperous kingdom. theIr reign was marked by peaCe and harMony, and the people loved thEm dearly. However, the King had a seCret that he had Kept from everyone, including his belOved wife.
    """
    input_file = tmpdir.join("input.txt")
    input_file.write(input_text)

    # Create a temporary correct output file
    correct_output_text = """
    Once upon a time in a faraway land, there lived a King and Queen who ruled over a Prosperous kingdom. their reign was marked by peace and harmony, and the people loved them dearly. However, the King had a secret that he had kept from everyone, including his beloved wife.
    """
    correct_output_file = tmpdir.join("correct_output.txt")
    correct_output_file.write(correct_output_text)

    # Correct the text and write to output.txt
    output_text = correct_text(input_file.strpath)

    # Read the content of output.txt
    output_file = tmpdir.join("output.txt")
    with open(output_file.strpath, 'r', encoding='utf-8') as file:
        corrected_content = file.read()

    # Compare the corrected content with the correct output content
    assert corrected_content == correct_output_text.strip()

if __name__ == "__main__":
    pytest.main()
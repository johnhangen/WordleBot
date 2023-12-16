# Wordle Solver

<p>
    <img alt="Docker" src="https://img.shields.io/badge/-Docker-46a2f1?style=flat-square&logo=docker&logoColor=white" />
    <img alt="python" src="https://img.shields.io/badge/-Python-13aa52?style=flat-square&logo=python&logoColor=white" />
</p>

## Overview

The Wordle Solver is a Python-based tool designed to assist in solving the popular word game, Wordle. This tool uses a class named `WordlePos` to filter a list of words based on specific criteria matching the Wordle game's mechanics. The criteria include known letters in specific positions, known letters that are in the word but not in specific positions, and letters that are not in the word.

## Features

- **Real Letter Position Identification**: The solver can identify letters that are correctly positioned in the word.
- **Letter Position Exclusion**: It identifies letters that are in the word but not in specific positions.
- **Letter Exclusion**: It can exclude words containing specific letters.
- **Word Ranking**: Words are ranked based on the frequency of letters in the English language, providing a probable best guess.

## `WordlePos` Class

### Initialization

- `words`: A list of possible words.
- `real_letters`: Letters that are known to be in specific positions (use '_' for unknown positions).
- `not_pos`: A dictionary indicating letters that are in the word but not in specific positions.
- `not_letters`: Letters that are known not to be in the word.

### Methods

- `find_words()`: Filters the list of words based on the criteria.
- `get_words()`: Returns the filtered and sorted list of words.
- `is_valid_word(word)`: Checks if a word is valid based on the set criteria.

## Usage

1. Initialize the `WordlePos` class with a list of words.
2. Set the criteria based on the Wordle game's feedback.
3. Call `get_words()` to retrieve the list of potential correct words, sorted by probability.

## Future Enhancements

- **Graphical User Interface (GUI)**: The next step in the project's development is to create a user-friendly GUI. This will make the tool more accessible and intuitive to use, allowing users to input the Wordle game's feedback directly and receive the solver's suggestions in a more engaging format.

## Contributing

Contributions to the project are welcome! Whether it's improving the logic, optimizing the code, or helping develop the GUI, your input is valuable. Please feel free to fork the repository, make your changes, and submit a pull request.

## License

MIT

---

Happy Wordle solving!

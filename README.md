# Bengali Word Distortion Generator-Powerred GPT4

## Description

This project contains a Python script designed to apply various linguistic distortions to Bengali words using prompt engineering with GPT4. It's particularly useful train LM model to correct ASR output in the post-processing stage. 

## Features
- Applies multiple types of distortions to words.
- Supports a range of distortions including vowel lengthening, consonant omission, affricate softening, and more.
- Filters words based on length.
- Exports the distorted words to a TSV / CSV(Tab-Separated Values) file.


## Usage
- Place any list of words in a text file named filtered_unique_words.txt, with one word per line.
- Run the script:
    ```bash
    python applying_noises.py
    ```
## Input & Output
- **Input**: The script reads words from a file named filtered_unique_words.txt.
- **Output**: The results are saved in distorted_words.tsv, where each word is accompanied by its various distorted forms.
The output will be saved in a file named distorted_words.tsv in the same directory.

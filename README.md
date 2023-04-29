# Vocabulary.com Scraper

This is a Python script that scrapes Vocabulary.com lists and retrieves words, definitions, and examples in a .txt format which you can then import into Anki.

## Requirements

- requests library
- Beautiful Soup 4 library

You can install the libraries using pip:
```
pip install requests
pip install beautifulsoup4
```

## Usage

Run the script and enter the link to a Vocabulary.com list when prompted.
The script will extract the words, definitions, and examples from the list(s) and write them to a text file with the list name.

## Example
```
Enter Vocabulary.com link: https://www.vocabulary.com/lists/23400
Words, definitions, and examples have been written to 100_Top_SAT_Words_-_Vocabulary_List__Vocabularycom.txt.
```

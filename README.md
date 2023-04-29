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

## The example output
```
abate	become less in amount or intensity	
abdicate	give up power, duties, or obligations	
aberration	a state or condition markedly different from the norm	
abstain	refrain from doing, consuming, or partaking in something	
adversity	a state of misfortune or affliction	
aesthetic	characterized by an appreciation of beauty or good taste	
amicable	characterized by friendship and good will	
anachronistic	chronologically misplaced	
...
spurious	plausible but false	
submissive	inclined or willing to give in to orders or wishes of others	
substantiate	establish or strengthen as with new evidence or facts	
subtle	difficult to detect or grasp by the mind or analyze	
superficial	of, affecting, or being on or near the surface	
superfluous	more than is needed, desired, or required	
surreptitious	marked by quiet and caution and secrecy	
tactful	having a sense of what is considerate in dealing with others	
tenacious	stubbornly unyielding	
transient	lasting a very short time	
venerable	profoundly honored	
vindicate	show to be right by providing justification or proof	
wary	marked by keen caution and watchful prudence	
```

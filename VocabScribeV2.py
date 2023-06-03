import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import os

webdriver_path = 'Chrome'

driver = webdriver.Chrome(service=Service(webdriver_path))

url = input("Enter Vocabulary.com link: ")

driver.get(url)

html_content = driver.page_source

soup = BeautifulSoup(html_content, 'html.parser')

wordlist = soup.find_all('li', class_='wordlist')

if wordlist:
    links = []
    for li in wordlist:
        header = li.find('div', class_='header')
        if header:
            h2 = header.find('h2')
            if h2 and h2.find('a'):
                link = "https://www.vocabulary.com/" + h2.find('a')['href']
                links.append(link)

    with open('Links.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(links))

    driver.quit()

    with open('Links.txt', 'r') as f:
        links = f.read().splitlines()

    for link in links:
        time.sleep(5)
        driver = webdriver.Chrome(service=Service(webdriver_path))
        driver.get(link)
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        words = soup.find_all('a', class_='word')
        definitions = soup.find_all('div', class_='definition')
        examples = soup.find_all('div', class_='example')
        word_list = []
        for i in range(len(words)):
            word = re.sub(r'\s+', ' ', words[i].text.strip())
            definition = re.sub(r'\s+', ' ', definitions[i].text.strip())
            example_div = examples[i] if i < len(examples) else None
            example_a = example_div.find('a', class_='source') if example_div else None
            if example_a:
                example_a.extract()
            example = re.sub(r'\s+', ' ', example_div.text.strip()) if example_div else ''
            word_list.append(word + '\t' + definition + '\t' + example)
        filename = re.sub('[^\w\s-]', '', soup.title.text.strip())
        filename = filename.replace(' ', '_') + '.txt'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(word_list))
        print(f"Words, definitions, and examples have been written to {filename}.")
        driver.quit()
else:
    words = soup.find_all('a', class_='word')
    definitions = soup.find_all('div', class_='definition')
    examples = soup.find_all('div', class_='example')
    word_list = []
    for i in range(len(words)):
        word = re.sub(r'\s+', ' ', words[i].text.strip())
        definition = re.sub(r'\s+', ' ', definitions[i].text.strip())
        example_div = examples[i] if i < len(examples) else None
        example_a = example_div.find('a', class_='source') if example_div else None
        if example_a:
            example_a.extract()
        example = re.sub(r'\s+', ' ', example_div.text.strip()) if example_div else ''
        word_list.append(word + '\t' + definition + '\t' + example)
    filename = re.sub('[^\w\s-]', '', soup.title.text.strip())
    filename = filename.replace(' ', '_') + '.txt'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(word_list))
    print(f"Words, definitions, and examples have been written to {filename}.")
driver.quit()
batch_filename = 'OneFile.txt'
with open(batch_filename, 'w', encoding='utf-8') as batch_file:
    for filename in os.listdir():
        if filename.endswith('.txt') and 'Vocabulary_List' in filename:
            with open(filename, 'r', encoding='utf-8') as f:
                batch_file.write(f.read().strip() + '\n')

os.remove('Links.txt')
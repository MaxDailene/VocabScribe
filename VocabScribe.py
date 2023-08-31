from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import os
import random

def scrape_vocabulary_links(url):
    driver = webdriver.Chrome()
    driver.get(url)
    
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    links = []

    wordlist = soup.find_all('li', class_='wordlist')
    if wordlist:
        for li in wordlist:
            header = li.find('div', class_='header')
            if header:
                h2 = header.find('h2')
                if h2 and h2.find('a'):
                    link = "https://www.vocabulary.com/" + h2.find('a')['href']
                    links.append(link)

    driver.quit()
    return links

def scrape_word_data(link):
    driver = webdriver.Chrome()
    driver.get(link)
    
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    word_list = []

    word_elements = soup.find_all('a', class_='word')
    definition_elements = soup.find_all('div', class_='definition')

    if soup.find('div', class_='description'):
        example_elements = soup.find_all('div', class_='description')
    else:
        example_elements = soup.find_all('div', class_='example')

    for i in range(len(word_elements)):
        word = re.sub(r'\s+', ' ', word_elements[i].text.strip())
        definition = re.sub(r'\s+', ' ', definition_elements[i].text.strip())
        example_div = example_elements[i] if i < len(example_elements) else None
        example_a = example_div.find('a', class_='source') if example_div else None
        if example_a:
            example_a.extract()
        example = re.sub(r'\s+', ' ', example_div.text.strip()) if example_div else ''
        word_list.append(word + '\t' + definition + '\t' + example)

    filename = re.sub('[^\w\s-]', '', soup.title.text.strip()).replace(' ', '_') + '.txt'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(word_list))

    driver.quit()
    return filename

def generate_unique_filename(base_filename):
    index = 1
    while True:
        filename = f"{base_filename}{index}.txt"
        if not os.path.exists(filename):
            return filename
        index += 1


def main():
    url = input("Enter Vocabulary.com link: ")

    links = scrape_vocabulary_links(url)
    
    if links:
        for link in links:
            filename = scrape_word_data(link)
            print(f"Words, definitions, and examples have been written to {filename}.")
    else:
        filename = scrape_word_data(url)
        print(f"Words, definitions, and examples have been written to {filename}.")
    
    batch_base_filename = 'OneFile'
    batch_filename = generate_unique_filename(batch_base_filename)

    combined_text = ''

    for filename in os.listdir():
        if filename.endswith('.txt') and 'Vocabulary_List' in filename:
            with open(filename, 'r', encoding='utf-8') as f:
                combined_text += f.read().strip() + '\n'
            if filename != batch_filename:
                os.remove(filename)

    with open(batch_filename, 'w', encoding='utf-8') as batch_file:
        batch_file.write(combined_text)

    if os.path.exists('Links.txt'):
        os.remove('Links.txt')

if __name__ == "__main__":
    main()
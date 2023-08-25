from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import os
import random

def scrape_vocabulary(url, driver_path):
    driver = webdriver.Chrome(service=Service(driver_path))
    driver.get(url)
    
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

def main():
    driver_path = 'Chrome'  # Update this with the path to your Chrome WebDriver
    url = input("Enter Vocabulary.com link: ")
    
    filename = scrape_vocabulary(url, driver_path)
    print(f"Words, definitions, and examples have been written to {filename}.")
    
    batch_filename = 'OneFile.txt'
    with open(batch_filename, 'w', encoding='utf-8') as batch_file:
        for filename in os.listdir():
            if filename.endswith('.txt') and 'Vocabulary_List' in filename:
                with open(filename, 'r', encoding='utf-8') as f:
                    batch_file.write(f.read().strip() + '\n')

    if os.path.exists('Links.txt'):
        os.remove('Links.txt')

if __name__ == "__main__":
    main()

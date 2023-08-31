from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import traceback

def main():
    driver = webdriver.Chrome()

    while True:
        word = input("Enter a word to look up (or type 'exit' to quit): ")
        if word.lower() == 'exit':
            break
        
        sentences_to_scrape = int(input("How many sentences do you want to scrape? "))
        scrape_next_page = sentences_to_scrape == 5
        
        while True:
            try:
                url = "https://www.vocabulary.com/dictionary/" + word
                driver.get(url)
                time.sleep(5)
                short_paragraph = driver.find_element("css selector", "p.short").text
                long_paragraph = driver.find_element("css selector", "p.long").text
                
                sentence_elements = driver.find_elements("css selector", "div.sentence")
                max_sentences = min(sentences_to_scrape, len(sentence_elements))
                
                sentences = [element.text for element in sentence_elements[:max_sentences]]
                
                with open("Words-ExamplePairs.txt", "a", encoding="utf-8") as file:
                    sentences_str = '\t'.join(sentences) if sentences else ''
                    file.write("{}\t{}\t{}\t{}\n".format(word, short_paragraph, long_paragraph, sentences_str))
                
                if scrape_next_page:
                    next_link = driver.find_element("css selector", "a.next.right")
                    next_link.click()
                    sentences_to_scrape = int(input("How many sentences do you want to scrape on the next page? "))
                    scrape_next_page = sentences_to_scrape == 5
                else:
                    break
            except Exception as e:
                with open("error_log.txt", "a", encoding="utf-8") as log_file:
                    log_file.write("Error for word '{}': {}\n".format(word, str(e)))
                    log_file.write(traceback.format_exc() + "\n")
                print("An error occurred. Check 'error_log.txt' for details.")
                break
        
    driver.quit()

if __name__ == "__main__":
    main()
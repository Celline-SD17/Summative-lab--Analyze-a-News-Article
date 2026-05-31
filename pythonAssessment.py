#!/bin/usr/ env 
import re
from collections import Counter

#Read text file
def read_text_file(filename):
    try:
        with open("News Article for Python Assessment.txt", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return ""
   
#Counting the number of times a specific Word
def count_specific_word(text, search_word):
    words=re.findall(r"\b\w+\b", text.lower())
    return words.count(search_word.lower())

#Identify the most common word
def identify_most_common_word(text):
    if not text.strip():
        return None
    words = re.findall(r"\b\w+\b", text.lower())

    if not words:
        return None
    word_counts = Counter(words)
    return word_counts.most_common(1)[0][0]

#Calculate the average length of words
def calculate_average_word_length(text):
    words = re.findall(r"\b\w+\b", text)

    if not words:
        return 0
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

#Count the number of paragraphs
def count_paragraphs(text):
    if not text.strip():
        return 1
    
    paragraphs = [p for p in text.split("\n\n") if p.strip()]
    return len(paragraphs)

#Counting the number of sentences in the text
def count_sentences(text):
    if not text.strip():
        return 1
    sentences = re.split(r"[.!?]+", text)
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)

#Main program
def main():
    filename = input("Enter the news article file name: ")
    text = read_text_file(filename)

    if text =="":
        return
    search_word = input("Enter the word you want to search: ")
    print("\n--- TEXT ANALYSIS RESULTS ---")
    word_count = count_specific_word(text, search_word)
    print(f"Occurrences of '{search_word}': {word_count}")
    common_word = identify_most_common_word(text)
    print(f"Most common word: {common_word}")

    average_length = calculate_average_word_length(text)
    print(f"Average word length: {average_length:.2f}")

    paragraph_count = count_paragraphs(text)
    print(f"Number of paragraphs: {paragraph_count}")

    sentence_count = count_sentences(text)
    print(f"Number of sentences: {sentence_count}")
if __name__ == "__main__":
    main()









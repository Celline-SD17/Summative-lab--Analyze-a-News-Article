#!/usr/bin/Env python3 
import re
#Read text file

   
#Counting the number of times a specific Word
def count_specific_word(text, search_word):
    words=re.findall(r"\b\w+\b", text.lower())
    return words.count(search_word.lower())

#Identify the most common word

def identify_most_common_word(text):

    if text.strip() == "":
        return None

    words = re.findall(r"\b\w+\b", text.lower())

    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    most_common_word = ""
    highest_count = 0

    for word, count in word_counts.items():
        if count > highest_count:
            highest_count = count
            most_common_word = word

    return most_common_word


#Calculate the average length of words

def calculate_average_word_length(text):
    words = re.findall(r"\b\w+\b", text)

    if len(words) == 0:
        return 0

    total = 0

    for word in words:
        total += len(word)

    return total / len(words)

#Count the number of paragraphs
def count_paragraphs(text):
    if text.strip() == "":
        return 1

    paragraphs = text.split("\n\n")

    count = 0
    for p in paragraphs:
        if p.strip():
            count += 1

    return count


#Counting the number of sentences in the text

def count_sentences(text):
    if text.strip() == "":
        return 1
    count = 0

    for char in text:
        if char in ".!?":
            count += 1

    return count

#Main program
def main():
    file_name = input("Enter the article file name: ")

    with open(file_name, "r", encoding="utf-8") as file:
        article_text = file.read()

    search_word = ""

    while search_word == "":
        search_word = input("Enter a word to search for: ")
        if search_word == "":
            print("No search word provided")
        else:
            print("Searching article...")
            #Displaying results
    print("\n--- TEXT ANALYSIS RESULTS ---")
    print("Occurrences:", count_specific_word(article_text, search_word))
    print("Most Common Word:", identify_most_common_word(article_text))
    print("Average Word Length:", calculate_average_word_length(article_text))
    print("Paragraphs:", count_paragraphs(article_text))
    print("Sentences:", count_sentences(article_text))
            

if __name__ == "__main__":
    main() 




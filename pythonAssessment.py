#!/bin/usr/ env 
#!/bin/usr/ env 
import re
from collections import Counter
#Read text file
file_name = input("Enter the article file name: ")
with open("News Article for Python Assessment.txt" , "r", encoding="utf-8") as file:
    article_text = file.read()
   
#Counting the number of times a specific Word
def count_specific_word(text, search_word):
    words=re.findall(r"\b\w+\b", text.lower())
    return words.count(search_word.lower())

#Identify the most common word

def identify_most_common_word(text):

    if text.strip() == "":
        return None

    words = text.lower().split()

    word_counts = {}

    for word in words:
        cleaned_word = word.strip(".,!?;:'\"()")

        if cleaned_word in word_counts:
            word_counts[cleaned_word] += 1
        else:
            word_counts[cleaned_word] = 1

    most_common_word = ""
    highest_count = 0

    for word in word_counts:

        if word_counts[word] > highest_count:
            highest_count = word_counts[word]
            most_common_word = word

    return most_common_word


#Calculate the average length of words

def calculate_average_word_length(text):

    words = text.split()

    if len(words) == 0:
        return 0

    total_letters = 0

    for word in words:
        cleaned_word = word.strip(".,!?;:'\"()")
        total_letters += len(cleaned_word)

    average = total_letters / len(words)

    return float(average)

#Count the number of paragraphs

def count_paragraphs(text):

    if text.strip() == "":
        return 1

    paragraphs = text.split("\n\n")

    count = 0

    for paragraph in paragraphs:

        if paragraph.strip() != "":
            count += 1

    return count

#Counting the number of sentences in the text
def count_sentences(text):

    if text.strip() == "":
        return 1

    count = 0

    for character in text:

        if character == ".":
            count += 1

        elif character == "!":
            count += 1

        elif character == "?":
            count += 1

    return count
#Validating a search word
search_word = ""

while search_word == "":
    search_word = input("Enter a word to search for: ")

    if search_word == "":
        print("Search word cannot be empty.")
    else:
        print("Searching article...")

#Displaying results
print("\n--- TEXT ANALYSIS RESULTS ---")
print(
    f"Occurrences of '{search_word}':",
    count_specific_word(article_text, search_word)
)

print(
    "Most Common Word:",
    identify_most_common_word(article_text)
)

print(
    "Average Word Length:",
    calculate_average_word_length(article_text)
)

print(
    "Number of Paragraphs:",
    count_paragraphs(article_text)
)

print(
    "Number of Sentences:",
    count_sentences(article_text)

)





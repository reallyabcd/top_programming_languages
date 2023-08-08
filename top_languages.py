# Import requests library to make HTTP requests
import requests

# Import BeautifulSoup library to parse HTML data
from bs4 import BeautifulSoup

# Import Counter library to count the frequency of words
from collections import Counter

# Define a function that takes a query as an input and returns a list of titles from my web search tool
def get_titles(query):
    # Make a GET request to my web search tool with the query as a parameter
    response = requests.get(f"https://bing.com/search?q={query}")
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the response content as HTML using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        # Find all the elements with the class "b_algo" that contain the titles of the articles
        titles = soup.find_all("h2", class_="b_algo")
        # Create an empty list to store the titles
        title_list = []
        # Loop through each title element
        for title in titles:
            # Get the text content of the title element and strip any whitespace
            title_text = title.get_text().strip()
            # Append the title text to the title list
            title_list.append(title_text)
        # Return the title list
        return title_list
    else:
        # Print an error message if the response status code is not 200 (OK)
        print(f"Error: {response.status_code}")

# Define a function that takes a list of titles as an input and returns a list of programming languages based on the words in the titles
def get_languages(titles):
    # Create an empty list to store the languages
    language_list = []
    # Define a set of common words that are not programming languages
    common_words = {"the", "of", "in", "to", "for", "and", "a", "an", "is", "are", "be", "by", "on", "with", "as", "or", "at", "from", "how", "what", "why", "when", "where", "who"}
    # Loop through each title in the titles list
    for title in titles:
        # Split the title into words by whitespace and punctuation
        words = title.split()
        # Loop through each word in the words list
        for word in words:
            # Strip any whitespace and punctuation from the word and convert it to lowercase
            word = word.strip().lower()
            # Check if the word is not empty and not in the common words set
            if word and word not in common_words:
                # Append the word to the language list
                language_list.append(word)
    # Return the language list
    return language_list

# Define a function that takes a list of languages as an input and returns a list of tuples with the language name and frequency sorted in descending order
def get_top_languages(languages):
    # Create a Counter object from the languages list that counts the frequency of each language
    counter = Counter(languages)
    # Get a list of tuples with the language name and frequency sorted by frequency in descending order
    top_languages = counter.most_common()
    # Return the top languages list
    return top_languages

# Define a query for my web search tool (you can change this according to your

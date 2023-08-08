# top_programming_languages
# HOW TO FIX FILTER ? 😊
To create a filter that shows the top trending programming languages from multiple categories, you need to use some criteria to rank the languages based on their popularity, demand, usage, or growth. For example, you can use the following sources of data:

The results from web search tool that shows some articles about the top programming languages in 2023 based on different metrics and sources.
The data from Stack Overflow, a popular online community for developers, that shows the most popular technologies based on their annual developer survey or their monthly trends.
The data from [GitHub], a leading platform for hosting and collaborating on code, that shows the most popular languages based on their state of the octoverse report or their language statistics.
The data from [TIOBE], an index that measures the popularity of programming languages based on search engine results.
The data from [PYPL], an index that measures the popularity of programming languages based on Google trends.
You can use these sources of data to create different categories for your filter, such as:
```
The most popular programming languages overall
The most popular programming languages for web development
The most popular programming languages for data science
The most popular programming languages for mobile development
The most popular programming languages for machine learning
The most popular programming languages for game development
The most popular programming languages for cloud computing
The most popular programming languages for IoT devices
The most popular programming languages for beginners
The most popular programming languages for employers
```
You can also use your own criteria or preferences to create your own categories. For example, you can create a category for the most fun, creative, or elegant programming languages.

To create a filter that shows the top trending programming languages from multiple categories, you need to write some code that can fetch, parse, and analyze the data from the sources you choose. You also need to write some code that can display the results in a user-friendly and interactive way. You can use any programming language or framework that you are comfortable with, but I suggest using Python, as it is one of the most versatile, powerful, and easy-to-use languages for web scraping, data analysis, and web development.

To help you get started,  There have written some sample code in Python that can fetch the data from my web search tool and display the top 10 programming languages based on the titles of the articles. You can use this code as a reference or modify it according to your needs. You can also use other libraries or modules that can make your task easier or more efficient.

Here is the sample code:
```bash
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

# Define a query for my web search tool (you can change this according to your need

```




# how to run this script ? 

To run this script, you need to have Python installed on your computer. You can download and install Python from [here]. You also need to install the requests and BeautifulSoup libraries, which are used to make HTTP requests and parse HTML data. You can install them by typing 

```code
pip install requests
```
and 
```code
pip install beautifulsoup4
```
in your terminal or command prompt.

# QA
You can save this script by any name you like, but make sure it has the .py extension. For example, you can save it as top_languages.py. To run this script, you need to open a terminal or command prompt and navigate to the folder where you saved the script. Then, you can type python top_languages.py and press enter. The script will print the top 10 programming languages based on the titles of the articles from my web search tool.


# STEPS 
Here are the steps to run this script:

Download and install Python from [here].
Install the requests and BeautifulSoup libraries by typing pip install requests and pip install beautifulsoup4 in your terminal or command prompt.
Save this script as top_languages.py or any name you like with the .py extension.
Open a terminal or command prompt and navigate to the folder where you saved the script.
Type python top_languages.py and press enter.
See the output of the script.

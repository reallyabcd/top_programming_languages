import requests
from bs4 import BeautifulSoup
from collections import Counter

def get_titles(query):
    response = requests.get(f"https://bing.com/search?q={query}")
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        titles = soup.find_all("a", class_="b_algo")
        title_list = []
        for title in titles:
            title_text = title.get_text().strip()
            title_list.append(title_text)
        return title_list
    else:
        print(f"Error: {response.status_code}")

def get_languages(titles):
    language_list = []
    common_words = {"the", "of", "in", "to", "for", "and", "a", "an", "is", "are", "be", "by", "on", "with", "as", "or", "at", "from", "how", "what", "why", "when", "where", "who"}
    for title in titles:
        words = title.split()
        for word in words:
            word = word.strip().lower()
            if word and word not in common_words:
                language_list.append(word)
    return language_list

def get_top_languages(languages):
    counter = Counter(languages)
    top_languages = counter.most_common()
    return top_languages

query = "top web languages"
titles = get_titles(query)
languages = get_languages(titles)
top_languages = get_top_languages(languages)

print(f"The top 5 web languages based on the titles of the articles from my web search tool are:")
for i in range(min(5, len(top_languages))):
    print(f"{i+1}. {top_languages[i][0]} ({top_languages[i][1]} times)")

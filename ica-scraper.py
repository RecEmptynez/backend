from bs4 import BeautifulSoup
import requests
import spacy

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def get_ingredient(ingredient,nlp):
    # Remove adjectives
    doc = nlp(ingredient)
    for token in doc:
        if token.dep_ == "ROOT":
            return token.text

def generate_ingredients(nlp):
    url = "https://www.ica.se/recept/?sort=rating"
    base_url = "https://www.ica.se"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    cards = soup.find_all("a", {"class": "recipe-card__content__title font-rubrik-2--mid"}, href=True)
    links = [base_url + card['href'] for card in cards]

    ingredients_list = []
    printProgressBar(0, len(links), prefix = 'Scraping:', suffix = 'Complete', length = 50)
    
    for i,link in enumerate(links):
        soup = BeautifulSoup(requests.get(link).text, "html.parser")
        
        printProgressBar(i + 1, len(links), prefix = 'Scraping:', suffix = 'Complete', length = 50)
        
        ingredients_html = soup.find_all("span", {"class": "ingredients-list-group__card__ingr"})
        title = soup.find("h1", {"class": "recipe-header__title"}).text.strip()
        
        for ingredient in ingredients_html:
            ingredient = ingredient.text.strip()
            ingredient = get_ingredient(ingredient,nlp)
            ingredients_list.append(ingredient+"\n")
        
    with open("ingredients.txt", "w", encoding='utf-8') as f:
        f.writelines(ingredients_list)

if __name__ == '__main__':
    nlp = spacy.load("sv_core_news_sm")
    generate_ingredients(nlp)
    
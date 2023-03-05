from bs4 import BeautifulSoup
import requests
import spacy
import json
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep
#******************************
#Must run python -m spacy download sv_core_news_sm
#******************************
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


#Get the root of the ingredient aka the ingredient name
def get_ingredient(ingredient,nlp):
    doc = nlp(ingredient)
    for token in doc:
        if token.dep_ == "ROOT":
            return token.text

def generate_ingredients(nlp):
    
    #Get the ica recipe page
    url = "https://www.ica.se/recept/?sort=rating"
    base_url = "https://www.ica.se"
    #soup = BeautifulSoup(requests.get(url).text, "html.parser")
    xpath_cookie = "//button[contains(text(), 'Godkänn kakor')]"
    #xpath_show_more_recipe = "//span[contains(text(), 'Visa fler recept')]"
    #xpath_show_more_recipe = "/html/body/div[1]/div/div[2]/div/div[8]/button"
    xpath_show_more_recipe = "/html/body/div/div/div[2]/div/div[8]/button/span[1]"
    #fixing several ------------------------------------
    
    
    driver = webdriver.Chrome(executable_path = r'./chromedriver')
    #driver = webdriver.Firefox()
    driver.get(url)
    #driver.find_element_by_xpath("//button[contains(text(), 'Visa fler recept')]").click()
    sleep(2)
    try:
        driver.find_element(By.XPATH, xpath_cookie).click()
    except:
        print("no cookie window")
    sleep(2)
    for i in range(2):
        sleep(1)
        try:
            driver.find_element(By.XPATH, xpath_show_more_recipe).click()
        except:
            print("doesnt woek")
    sleep(2)
    cards = driver.find_elements(By.CSS_SELECTOR, ".recipe-card__content__title.font-rubrik-2--mid")
    #print(cards)
    print(len(cards))

    links = []
    for link in cards:
        links.append(link.get_attribute("href"))
    print(len(links))

    #cards = soup.find_all("a", {"class": "recipe-card__content__title font-rubrik-2--mid"}, href=True)
    # --------------------------------------------------------
    #Get the links to the recipes
    #links = [base_url + card['href'] for card in cards]
    
    #Initialize the recipes list
    recipes_list = []
    
    #Print the progress bar
    printProgressBar(0, len(links), prefix = 'Scraping:', suffix = 'Complete', length = 50)
    
    #Loop through the links and get the ingredients
    for i,link in enumerate(links):
        
        #Initialize the ingredients list
        recipe_ingredients_list = []

        #Get the recipe page
        soup = BeautifulSoup(requests.get(link).text, "html.parser")
        
        #Print the progress bar
        printProgressBar(i + 1, len(links), prefix = 'Scraping:', suffix = 'Complete', length = 50)
        
        #Get HTML for ingredients
        ingredients_html = soup.find_all("span", {"class": "ingredients-list-group__card__ingr"})
        
        #Extract the title
        title = soup.find("h1", {"class": "recipe-header__title"}).text.strip()

        #Add the title to the ingredients list
        for ingredient in ingredients_html:
            ingredient = ingredient.text.strip()
            ingredient = get_ingredient(ingredient,nlp)
            recipe_ingredients_list.append(ingredient+"\n")
    
        #Create json dictionary for this recipe
        recipe_json = {
            "title": title,
            "ingredients": recipe_ingredients_list,
            "url": link,
        }

        # Add the recipe to the list of recipes
        recipes_list.append(recipe_json)

    #Write the ingredients to a file
    with open("ingredients.json", "w", encoding='utf-8') as f:
        json.dump(recipes_list, f, indent=4)


#Main flow of the program
if __name__ == '__main__':
    #Load the Swedish model
    nlp = spacy.load("sv_core_news_sm")
    #Generate the ingredients
    generate_ingredients(nlp)
    
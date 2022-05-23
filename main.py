import requests
import string
import logging
from thefuzz import process

logging.getLogger().setLevel(logging.ERROR)


def get_list_of_cocktails():
    a_to_z = string.ascii_lowercase
    name_and_ingridients = {}
    for alphabet in a_to_z:
        response = requests.get(
            "https://www.thecocktaildb.com/api/json/v1/1/search.php?f=" + alphabet
        ).json()
        if response["drinks"] is not None:
            for index in range(len(response["drinks"])):
                cocktail_name_from_api = str(response["drinks"][index]["strDrink"])
                ingridients_list = []
                for cocktail_name, cocktail_ingridients in response["drinks"][index].items():
                    if "Ingredient" in cocktail_name and cocktail_ingridients is not None:
                        ingridients_list.append(cocktail_ingridients)
                        sorted_list = sorted(ingridients_list)
                name_and_ingridients[cocktail_name_from_api] = sorted_list
    return name_and_ingridients


def exact_match(api, inputlist):
    list_of_ingridients = []
    for cocktail_name, cocktail_ingridients in api.items():
        for ingridient in cocktail_ingridients:
            if ingridient in inputlist:
                list_of_ingridients.append(ingridient)
        if list_of_ingridients != cocktail_ingridients:
            list_of_ingridients = []
        else:
            print(cocktail_name)
            list_of_ingridients = []


def fuzzy_match(api, inputlist):
    list_of_ingridients = []
    for cocktail_name, cocktail_ingridients in api.items():
        for ingridient in cocktail_ingridients:
            if process.extract(ingridient, inputlist, limit=1)[0][1] > 90:
                list_of_ingridients.append(ingridient)
        if list_of_ingridients != cocktail_ingridients:
            list_of_ingridients = []
        else:
            print(cocktail_name)
            list_of_ingridients = []


def ingridients_input():
    print("Please enter a list of comma separated ingredients available to you:")
    comma_separated_list = input().split(",")
    stripped_list_of_ingridients = list(map(str.strip, comma_separated_list))
    fuzzy_match(get_list_of_cocktails(), stripped_list_of_ingridients)
    #exact_match(get_list_of_cocktails(), stripped_list_of_ingridients)


# Lemon juice ,Dark rum,Grenadine, Gin, Grand Marnier, Grenadine, Cranberry juice, Ice


if __name__ == "__main__":
    ingridients_input()

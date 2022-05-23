
## Cocktails

Create a Virtual Environment:

``python3 -m venv .venv``

``source .venv/bin/activate``


Install dependencies form the requirements.txt file:

``pip install -r requirements.txt`` 


Run the code from root of the directory, with:

``python main.py``


It will ask for a list of comma separated ingredients. Program will go through all the 
cocktails and their ingredients (provided by an API from https://www.thecocktaildb.com/)
and return a list of Cocktails that can be made (one of each line).
for eg.

    >>> Lemon juice ,Dark rum,Grenadine, Gin, Grand Marnier, Grenadine, Cranberry juice, Ice

will return

    >>> A1
    >>> Adam
    >>> Ruby Tuesday


### Matching the ingredients available to us, to the actual Cocktail's ingredients.

There are two match functions in the ``main.py``.
- ``exact_match`` - Loops through all the cocktails, looks for each cocktail's ingredient
if it matches the elements in the list of the user provided ingredients. However, it 
doesn't account for spelling mistakes and case sensitivity. 

- ``fuzzy_match`` This performs the same task as ``exact_match`` function. But it also 
accounts for spelling mistakes and case sensitivity.

To switch between the searches, uncomment the other function with ``ingridients_input`` 
function. 

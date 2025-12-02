

def dictionary_demo():
    sample_dict = {
        "name": "Alice",
        "age": 30,
        "city": "New York",
        2 : 3  # key value can be mixed types
    }

    acronyms = ['LOL', 'IDK', 'TBH', 'SMH']
    translations = ['Laughing Out Loud', "I Don't Know", 'To Be Honest', 'Shaking My Head']

    acronyms_2_translations = dict(zip(acronyms, translations))

    empty_dict = {}

    empty_dict['new_key'] = 'new_value' # add a new key-value pair
    empty_dict['new_key'] = 'updated_value' # update the value for an existing key

    del empty_dict['new_key']  # delete a key-value pair

    val = empty_dict.get('non_existent_key', 'default_value') # returns 'default_value' if key not found avoid key error
    print("Value for 'non_existent_key':", val)

    if 'age' in sample_dict: # check existence of a key
        print("Age is present in sample_dict.")


def movie_schedule():
    """
    Display the current movie schedule, prompt the user for a movie name, and print the corresponding showtime.
    """
    print(movie_schedule.__doc__)
    current_movies = {
        "Inception": "7:00 PM",
        "The Matrix": "9:00 PM",
        "Interstellar": "6:30 PM"
    }

    print("We are showing the following movies")

    for movie in current_movies.keys():
        print(movie, end=" ")
    print()

    # the same as above, more pythonic
    for movie in current_movies:
        print(movie, end=" ")
    print()

    movie_name = input("Enter the movie name to get its showtime: ")
    showtime = current_movies.get(movie_name)
    if showtime:
        print(f"The showtime for {movie_name} is {showtime}.")
    else:
        print(f"Sorry, we don't have showtime information for {movie_name}.")

def contacts():
    """
    Contacts: Demonstrates a dictionary containing a list of dictionaries as a value.
    """
    print(contacts.__doc__)
    # dictionary with a list of dictionaries as a value
    contacts = {
        'number': '4',
        'students': [
            {'name': 'Alice', 'phone': '123-456-7890'},
            {'name': 'Bob', 'phone': '987-654-3210'},
            {'name': 'Charlie', 'phone': '555-555-5555'},
            {'name': 'Diana', 'phone': '444-444-4444'}
        ]
    
    }

    for student in contacts['students']:
        print(f"Name: {student['name']}, Phone: {student['phone']}")


def json_demo():
    """
    Demonstrates how to convert a dictionary to a JSON string and back.
    """
    print(json_demo.__doc__)
    import json

    sample_dict = {
        "name": "Bob",
        "age": 25,
        "city": "Los Angeles",
        "is_student": False,
        "courses": ["Math", "Science", "Art"]  # value can be a list for a dictionary key
    }

    # Convert dictionary to JSON string
    json_str = json.dumps(sample_dict)
    print("JSON String:", json_str)

    # Convert JSON string back to dictionary
    dict_from_json = json.loads(json_str)
    print("Dictionary from JSON:", dict_from_json)

def request_astronauts_in_space():
    """
    Requests data from a public API to get the current number of astronauts in space and their names.
    """
    print(request_astronauts_in_space.__doc__)
    import requests

    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    data = response.json() # decode JSON response to a dictionary

    number_of_astronauts = data['number']
    astronauts = data['people']

    print(f"There are currently {number_of_astronauts} astronauts in space:")
    for astronaut in astronauts:
        print(f"- {astronaut['name']} on the {astronaut['craft']}")

def request_whether():
    pass

if __name__ == "__main__":
   #contacts()
   #json_demo()
   request_astronauts_in_space()
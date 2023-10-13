import openai
import random
import requests
import shutil
import os
import json

# Initialize the OpenAI API client
openai.api_key = "API KEY"

def parse_json():
    with open('./alien-profiles.json', 'r') as file:
        data = json.load(file)
    profiles = data["alienProfiles"]

    selected_profile = random.choice(profiles)

    name = selected_profile['name']
    bio = selected_profile['bio']
    interests = selected_profile['interests']
    planet_name = selected_profile['planetName']
    age = selected_profile['age']
    alien_id = selected_profile['alien-id']

    return {"name": name,
            "bio": bio,
            "interests": interests,
            "planet": planet_name,
            "age": age,
            "id": alien_id}

def alien_traits(bio):
    input_text = bio
    response = openai.ChatCompletion.create(
                  model="gpt-3.5-turbo",
                  messages=[{"role": "system", "content": 'You are an AI assistant that parses dating app bios, \
                  and can distill them down to three words separated by commas that describe the person whose bio that is.'},
                            {"role": "user", "content": input_text}
                  ])

    result = response["choices"][0]["message"]["content"]
    values_list = [value.strip() for value in result.split(',')]
    return values_list

def respond_to_user(prompt, conversation_history, role_prompt):
    input_text = conversation_history + "\nUser: " + prompt + "\nAlien:"
    response = openai.ChatCompletion.create(
                  model="gpt-3.5-turbo",
                  messages=[{"role": "system", "content": role_prompt},
                            {"role": "user", "content": input_text}
                  ])

    result = response["choices"][0]["message"]["content"]

    conversation_history = conversation_history + "\nUser: " + prompt + "\nAlien: " + result
    return result, conversation_history

def get_pickup_line():
    user_input = input("What's your best pickup line for this alien?: ")
    return user_input
    # return get_user_guess_from_frontend()

def get_message():
    user_input = input("You: ")
    return user_input

def pass_pickup_line():
    if random.random() < 0.3:
        return True
    else:
        return False

def get_user_guess_from_frontend():
    # This function should interact with the frontend to get the user's guess
    pass


def print_receipt_with_message(image_ascii, message):
    # Placeholder to print to a receipt printer
    print_to_receipt_printer(image_ascii, message)


def print_to_receipt_printer(content):
    # This function should interact with the receipt printer and print the content
    pass


def main_game_loop():
    alien = parse_json()
    print(alien["name"] + " from " + alien["planet"])
    print(alien["age"])

    print(alien_traits(alien["bio"]))

    role_prompt = """You are an alien looking for love, but you have high standards!
    You are chatting with the user on a dating app.
    You are interested in the User as a potential mate because you find them sexy.
    You are not very familiar with Earth culture, but appreciate it.
    You are confident and funny and like to reference sex. """ + \
    " Your traits are " + ' and '.join(alien_traits(alien["bio"])) + ". " + \
    " You like " + ' and '.join(alien["interests"]) + ". " + \
    """Your messages must be under 200 characters.
    Reference the user's message in your reply.
    Reference your traits and your likes.
    Only give the words that you would say to the user.
    Do not write your role. """

    print(role_prompt)

    conversation_history = ""

    result = respond_to_user(get_pickup_line(), conversation_history, role_prompt)
    print(result[0])
    conversation_history = result[1]

    for i in range(3):
        result = respond_to_user(get_message(), conversation_history, role_prompt)
        print(result[0])
        conversation_history = result[1]

    # get_pickup_line()
    #
    # if (pass_pickup_line()):
    #     print("SUCCESS! smutty response here and receipt print.")
    # else:
    #     print("You failed (:")


def convert_image_to_ascii(image_path):
    # Convert the image to ASCII here and return as string
    return "ASCII Representation of Image"

def display_image_to_user(image_url):
    # Placeholder function to display the generated image on the GUI
    pass

def display_message_to_user(message):
    # Placeholder function to display a message on the GUI
    pass

if __name__ == "__main__":
    main_game_loop()

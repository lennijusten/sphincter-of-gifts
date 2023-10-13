import openai
import random
import requests
import shutil
import os
import json

# Initialize the OpenAI API client
openai.api_key = "YOUR API"

def parse_json():
    with open('./alien-profiles.json', 'r') as file:
        data = json.load(file)
    profiles = data["alienProfiles"]

    selected_profile = random.choice(profiles)

    print(selected_profile)
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

def alien_interests():
    return ["babes", "fish", "bedtime stories"]

def respond_to_user(prompt, conversation_history):
    input_text = conversation_history + "\nUser: " + prompt + "\nAlien:"
    response = openai.ChatCompletion.create(
                  model="gpt-3.5-turbo",
                  messages=[{"role": "system", "content": 'You are an alien looking for love, \
                  but you have high standards! You are chatting with the user on a dating app. \
                  You are interested in the User as a potential mate because you find them sexy. \
                  You are not very familiar with Earth culture, but appreciate it. \
                  You are cocky and funny and like to reference sex. \
                  You have many alien hobbies and personality traits. \
                  Your messages must be under 200 characters. \
                  Reference the user\'s message in your reply. \
                  Only give the words that you would say to the user.'},
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
    user_input = input()
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
    # print(alien_age())
    #
    # conversation_history = ""
    #
    # for i in range(3):
    #     result = respond_to_user(get_pickup_line(), conversation_history)
    #     print(result[0])
    #     conversation_history = result[1]
    #
    # print(conversation_history)

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

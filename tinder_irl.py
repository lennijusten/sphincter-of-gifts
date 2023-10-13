import openai
import random
import requests
import shutil
import os

# Initialize the OpenAI API client
# openai.api_key = "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"
openai.api_key = "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"

def alien_name():
    with open('./names.txt', 'r') as file:
        names = file.readlines()
    name = random.sample(names, 1)
    name = name[0].strip()
    return name

def alien_location():
    with open('./planets.txt', 'r') as file:
        planets = file.readlines()
    planet = random.sample(planets, 1)
    planet = planet[0].strip()
    return planet

def generate_bio():
    # prompt = """Write a funny and weird sentence or two describing yourself that makes people intrigued about you.
    # Do not describe physical traits. Only describe personality traits and hobbies.
    # Keep it under 100 characters. Make it weird but do not use that word.
    # Do not make every sentence alien-themed. Keep it subtle.
    # Do not use hashtags or emojis. Only write the words."""

    prompt = """25 of the following: Keep this under 100 characters.
    Something funny and slightly sexy that an alien would say about themselves referencing human culture.
    Do not use hashtags or emojis. Only write the words."""

    response = openai.ChatCompletion.create(
                  model="gpt-3.5-turbo",
                  messages=[{"role": "system", "content": 'You are an alien looking for love, \
                  but you have high standards!'},
                            {"role": "user", "content": prompt}
                  ])

    result = response["choices"][0]["message"]["content"]
    return result

def get_pickup_line():
    user_input = input("What's your best pickup line for this alien?: ")
    return user_input
    # return get_user_guess_from_frontend()

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
    print(alien_name() + " from " + alien_location())
    print(generate_bio())

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

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

def alien_age():
    age = random.randint(1, 999)
    with open('./time-units.txt', 'r') as file:
        units = file.readlines()
    unit = random.sample(units, 1)
    unit = unit[0].strip()
    return str(age) + " " + str(unit)

def tinder_bio():
    pass

def respond_to_user(prompt, conversation_history):
    input_text = conversation_history + "\nUser: " + prompt + "\nAlien:"
    response = openai.ChatCompletion.create(
                  model="gpt-3.5-turbo",
                  messages=[{"role": "system", "content": 'You are an alien looking for love, \
                  but you have high standards! You are chatting with the user on a dating app. \
                  You are interested in the User as a potential mate because you find them sexy. \
                  You are not very familiar with Earth culture, but appreciate it. \
                  You are very funny and like to reference sex. \
                  You have many alien hobbies and personality traits. Your messages must be under 200 characters. \
                  Reference the user\'s message in your reply. Only give the words that you would say to the user.'},
                            {"role": "user", "content": input_text}
                  ])

    print(input_text)
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
    print(alien_age())

    conversation_history = ""

    print(respond_to_user(get_pickup_line(), conversation_history))

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

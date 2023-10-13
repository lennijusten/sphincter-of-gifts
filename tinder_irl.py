import openai
import random
import requests
import shutil
import os

# Initialize the OpenAI API client
openai.api_key = "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"

def generate_bio():
    prompt = """Write an online dating bio. Do not use alien-themed language.
    Keep it under 100 characters. Make it weird and cultured but do not use those words.
    Do not make every sentence alien-themed.
    Do not use hashtags or emojis."""

    response = openai.ChatCompletion.create(
                  model="gpt-3.5-turbo",
                  messages=[{"role": "system", "content": 'You are looking for love, writing your online dating bio, \
                  but you have high standards and think you are way hotter than almost everyone on the app. \
                  You are whimsical and artsy.'},
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
    print(generate_bio())

    get_pickup_line()

    if (pass_pickup_line()):
        print("SUCCESS! smutty response here and receipt print.")
    else:
        print("You failed (:")


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

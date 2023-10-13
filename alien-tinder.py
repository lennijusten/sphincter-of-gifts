import openai
import json
import random
import requests
import shutil
import os

# Initialize the OpenAI API client
openai.api_key = "YOUR_OPENAI_API_KEY"

def create_run_directory():
    directory_name = "alien_profiles"
    if os.path.exists(directory_name):
        shutil.rmtree(directory_name)
    os.makedirs(directory_name)
    return directory_name

def get_alien_prompt():
    # Generate a chic party-themed prompt using ChatGPT
    response = openai.Completion.create(
        model="gpt-4.0-turbo",
        prompt="Describe an elegant alien attending a chic intergalactic party.",
        max_tokens=100
    )
    return response.choices[0].text.strip()

def generate_image(run_directory, save_as_filename=None):
    # Get a chic party-themed prompt from ChatGPT for the alien profile
    alien_prompt = get_alien_prompt()

    # Generate an alien image using the new prompt
    response = openai.Image.create(model="image-alpha-001", prompt=alien_prompt, size="512x512")
    image_url = response.data[0]["url"]
    if save_as_filename:
        full_path = os.path.join(run_directory, save_as_filename)
        save_image(image_url, full_path)
    return image_url


def save_image(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)


def get_user_response():
    # Placeholder for user input from GUI
    return get_user_guess_from_frontend()


def get_user_guess_from_frontend():
    # This function should interact with the frontend to get the user's guess
    pass


def swipe_left_or_right():
    # Placeholder for swipe functionality from GUI
    return get_swipe_direction_from_frontend()


def get_swipe_direction_from_frontend():
    # This function should interact with the frontend to detect if user swiped left or right
    pass


def evaluate_response(alien_traits, user_response):
    prompt = f"Evaluating the similarity between the traits '{alien_traits}' and the user's guess '{user_response}'."
    response = openai.Completion.create(model="gpt-4.0-turbo", prompt=prompt, max_tokens=150)
    result = response.choices[0].text.strip()
    return "match" in result


def print_receipt_with_message(image_ascii, message):
    # Placeholder to print to a receipt printer
    print_to_receipt_printer(image_ascii, message)


def print_to_receipt_printer(content):
    # This function should interact with the receipt printer and print the content
    pass


def main_game_loop():
    run_directory = create_run_directory()
    while True:
        # Generate an alien image and show it
        alien_filename = "alien_profile.png"
        image_url = generate_image(run_directory, alien_filename)
        display_image_to_user(image_url)  # Placeholder to display image on GUI

        # Check user's swipe decision
        decision = swipe_left_or_right()
        if decision == "left":
            continue  # Generate new alien profile
        elif decision == "right":
            # Randomly choose alien traits
            alien_traits = random.choice(["friendly, shy, mysterious", "aggressive, bold, dominant", "curious, intelligent, approachable"])
            user_response = get_user_response()
            match = evaluate_response(alien_traits, user_response)

            if match:
                message = "You truly understand me! Let's explore the cosmos together! ❤️"
                image_ascii = convert_image_to_ascii(alien_filename)  # Placeholder to convert image to ASCII
                print_receipt_with_message(image_ascii, message)
                break
            else:
                message = "Sorry, this isn’t a good fit. You don’t see me for who I am."
                display_message_to_user(message)  # Placeholder to display message on GUI

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





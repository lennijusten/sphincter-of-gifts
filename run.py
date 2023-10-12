import openai
import json
import random
import requests
import shutil
import os

# Initialize the OpenAI API client
openai.api_key = ""


def create_run_directory():
    # Create a directory name for this run
    directory_name = "run"

    # Delete the directory if it already exists
    if os.path.exists(directory_name):
        shutil.rmtree(directory_name)

    # Now, create the directory again
    os.makedirs(directory_name)

    return directory_name


def generate_image(prompt, run_directory, save_as_filename=None):
    # Generate an image using DALL·E 2
    response = openai.Image.create(
        model="image-alpha-001",
        prompt=prompt,
        size="512x512"
    )
    # Extract the image URL from the response
    image_url = response.data[0]["url"]
    if save_as_filename:
        full_path = os.path.join(run_directory, save_as_filename)  # Join the directory and filename here
        save_image(image_url, full_path)
    return image_url


def save_image(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)


def get_user_response():
    # Get user input from CLI
    user_response = input("Enter your guess based on the image: ")
    return user_response


def evaluate_response(initial_prompt, user_response):
    # Use GPT-4 API to evaluate response
    prompt = f"Considering the date idea '{initial_prompt}' and the user's guess '{user_response}', evaluate the " \
             f"semantic and thematic similarity of the two ideas. Consider both the intent and the details. Rate the " \
             f"similarity on a scale from 0 to 100, with 100 being an exact match and 0 being completely unrelated. " \
             f"Only return a number. "

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": 'You are a helpful computer assistant. Evaluate the semantic and thematic similarity between '
                        'two date ideas.'},
            {"role": "user", "content": prompt}
        ]
    )

    score = int(response["choices"][0]["message"]["content"])
    return score >= 80


def give_hint(initial_prompt, user_response, hint_number, key, run_directory):
    # Generate a hint based on the difference between user's response and the actual idea
    hint_prompt_text = f"Given that the original idea was '{initial_prompt}' and the user guessed '{user_response}', provide a refined description that narrows it down without directly revealing the answer."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": 'You are a helpful computer assistant that provides refined descriptions for image generation.'},
            {"role": "user", "content": hint_prompt_text}
        ]
    )

    refined_description = response["choices"][0]["message"]["content"]
    print(refined_description)

    # Generate an image and save it in the run-specific directory
    filename = f"{key}_hint_{hint_number}.png"
    image_url = generate_image(refined_description, run_directory, filename)
    return image_url


def print_ticket():
    print("Here's your drink ticket for the special spicy alien cocktail! 🍹")


def main_game_loop():
    # Create a directory for this run
    run_directory = create_run_directory()

    # Read date ideas from the JSON file
    with open("date-ideas.json", "r") as file:
        date_ideas_data = json.load(file)["date_ideas"]

    # Select a random date idea
    random_date_idea = random.choice(date_ideas_data)
    initial_prompt = random_date_idea["prompt"]
    print(f"Initial prompt key: {random_date_idea['key']}")
    print(f"Initial prompt: {initial_prompt}")

    max_guesses = 3
    current_guesses = 0

    while current_guesses < max_guesses:
        # Initial image
        initial_filename = f"{random_date_idea['key']}_initial.png"  # Just the filename without the directory
        image_url = generate_image(initial_prompt, run_directory, initial_filename)
        print(f"Check out this image to guess the date idea: {image_url}")
        user_response = get_user_response()
        is_correct = evaluate_response(initial_prompt, user_response)

        if is_correct:
            # User guessed correctly, reward them
            print("Congratulations! You guessed the date idea correctly.")
            print_ticket()
            break
        else:
            current_guesses += 1
            if current_guesses == max_guesses:
                # If the user has used all their guesses, then break out without giving another hint
                print("Sorry, that's not quite right.")
                break
            print(f"Sorry, that's not quite right. You have {max_guesses - current_guesses} guesses left.")
            new_image_url = give_hint(initial_prompt, user_response, current_guesses, random_date_idea['key'],
                                      run_directory)

    if current_guesses >= max_guesses:
        print("The alien tells you the date won't work due to communication problems.")


if __name__ == "__main__":
    main_game_loop()

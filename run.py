import openai
import json
import random
import urllib

api_key = "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"

# Initialize the OpenAI API client
openai.api_key = api_key

def generate_initial_image(prompt):
    # Generate an image using DALL·E 2
    response = openai.Image.create(
        model="image-alpha-001",
        prompt=prompt,
        size="256x256"  # You can adjust the size as needed
    )
    # Extract the image URL from the response
    image_url = response.data[0]["url"]
    return image_url


def get_user_response():
    # Simulate user input (replace this with actual user input)
    user_response = "User's guess goes here"
    return user_response


def evaluate_response(initial_prompt, user_response):
    # Placeholder logic, replace with actual evaluation criteria
    # For example, you could compare the user response to the initial prompt
    # and check for similarity or correctness based on your requirements.
    # Return True if the response is correct, False otherwise.
    return user_response.lower() == initial_prompt.lower()


def main_game_loop():
    # Read date ideas from the JSON file
    with open("date-ideas.json", "r") as file:
        date_ideas = json.load(file)["date_ideas"]

    # Select a random date idea
    initial_prompt = random.choice(date_ideas)
    print(f"Inital prompt: {initial_prompt}")

    max_guesses = 3
    current_guesses = 0

    while current_guesses < max_guesses:
        image_url = generate_initial_image(initial_prompt)
        user_response = get_user_response()
        is_correct = evaluate_response(initial_prompt, user_response)

        if is_correct:
            # User guessed correctly, reward them
            print("Congratulations! You guessed the date idea correctly.")
            break
        else:
            current_guesses += 1
            print(f"Sorry, that's not quite right. You have {max_guesses - current_guesses} guesses left.")

    if current_guesses >= max_guesses:
        print("The alien tells you the date won't work due to communication problems.")




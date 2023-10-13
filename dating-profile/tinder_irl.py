import openai
import random
import requests
import shutil
import os
import json

# Initialize the OpenAI API client
openai.api_key = "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"

# Port for the arduino
port = ""

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
    img = selected_profile['img']

    return {"name": name,
            "bio": bio,
            "interests": interests,
            "planet": planet_name,
            "age": age,
            "id": alien_id,
            "img": "img/" + img}

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
    if random.random() < 0.5:
        return True
    else:
        return False

def print_ticket(prompt: str = "SET THE PROMPT"):
    from arduino import Arduino, gen_ticket_id

    if "|" in prompt:
        print("WARNING: The prompt contains a pipe character, which is used to separate the prompt from the ticket ID. Removing it.")
        prompt = prompt.replace("|", "")

    arduino = Arduino(port)
    arduino.wait_until_ready()
    print(arduino.recv().decode('utf-8'))
    arduino.write_and_recv(f"{prompt}|{gen_ticket_id()}")

def generate_role_prompt(alien):
    role_prompt = """You are an alien looking for love, but you have high standards!
    You are chatting with the user on a dating app.
    You are not very familiar with Earth culture, but appreciate it.
    You are confident and funny and like to reference sex. """ + \
    " Your traits are " + ' and '.join(alien_traits(alien["bio"])) + ". " + \
    " You like " + ' and '.join(alien["interests"]) + ". "

    if (pass_pickup_line()):
        role_prompt += "You are interested in the User as a potential mate because you find them sexy. You really like what the user wrote. Try to seduce them. "
    else:
        role_prompt += "You hate what the user wrote. You find them ugly and think they have a bad personality. Reject them bombastically. "

    role_prompt += """Your messages must be under 300 characters.
    Reference the user's message in your reply.
    Reference your traits and your likes if they are relevant.
    Only give the words that you would say to the user.
    Do not write your role. """

    return role_prompt

def main_game_loop():
    print("entering main game loop")
    alien = parse_json()
    print(alien["name"] + " from " + alien["planet"])
    print(alien["age"])

    # print(alien_traits(alien["bio"]))
    role_prompt = generate_role_prompt(alien)

    # print(role_prompt)

    conversation_history = ""

    result = respond_to_user(get_pickup_line(), conversation_history, role_prompt)
    print(result[0])
    conversation_history = result[1]
    #
    # for i in range(3):
    #     result = respond_to_user(get_message(), conversation_history, role_prompt)
    #     print(result[0])
    #     conversation_history = result[1]

    # get_pickup_line()

def display_message_to_user(message):
    # Placeholder function to display a message on the GUI
    pass

if __name__ == "__main__":
    main_game_loop()

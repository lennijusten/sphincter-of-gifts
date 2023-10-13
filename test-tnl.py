import requests
from PIL import Image
from io import BytesIO
import time

# Constants
TNL_API_KEY = "257f129c-edbb-45ff-9645-973ff80ca294"
IMAGINE_URL = "https://api.thenextleg.io/v2/imagine"
MESSAGE_URL = "https://api.thenextleg.io/v2/message/{}?expireMins=2"

# Send a request to the Imagine endpoint
def request_image(prompt):
    payload = {
        "msg": prompt
    }
    headers = {
        'Authorization': f'Bearer {TNL_API_KEY}',
        'Content-Type': 'application/json'
    }
    response = requests.post(IMAGINE_URL, headers=headers, json=payload)
    return response.json().get("messageId")

# Poll the GET Message endpoint to retrieve the image URL
def get_image_url(message_id):
    headers = {
        'Authorization': f'Bearer {TNL_API_KEY}',
    }
    while True:
        response = requests.get(MESSAGE_URL.format(message_id), headers=headers)
        data = response.json()
        if data.get("progress") == 100:
            return data.get("imageUrl")
        elif data.get("progress") == "incomplete":
            print("Image generation is incomplete. Please try again later.")
            return None
        time.sleep(5)  # Wait for 5 seconds before polling again

# Save the image to a file
def save_image(image_url, filename):
    response = requests.get(image_url)
    with open(filename, 'wb') as file:
        file.write(response.content)

if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    message_id = request_image(prompt)
    print(message_id)
    if message_id:
        image_url = get_image_url(message_id)
        print(image_url)
        if image_url:
            filename = input("Enter the filename to save the image: ")
            save_image(image_url, filename)
            print(f"Image saved as {filename}")



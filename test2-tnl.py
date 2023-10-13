
import time

import requests

BASE_URL = "https://api.thenextleg.io/v2"
AUTH_TOKEN = "257f129c-edbb-45ff-9645-973ff80ca294"
AUTH_HEADERS = {
    "Authorization": f"Bearer {AUTH_TOKEN}",
    "Content-Type": "application/json",
}


def sleep(milliseconds):
    time.sleep(milliseconds / 1000)


def fetch_to_completion(message_id, retry_count, max_retry=20):
    image_res = requests.get(f"{BASE_URL}/message/{message_id}", headers=AUTH_HEADERS)
    image_response_data = image_res.json()

    if image_response_data["progress"] == 100:
        return image_response_data

    if image_response_data["progress"] == "incomplete":
        raise Exception("Image generation failed")

    if retry_count > max_retry:
        raise Exception("Max retries exceeded")

    if image_response_data["progress"] and image_response_data["progressImageUrl"]:
        print("---------------------")
        print(f'Progress: {image_response_data["progress"]}%')
        print(f'Progress Image Url: {image_response_data["progressImageUrl"]}')
        print("---------------------")

    sleep(5000)
    return fetch_to_completion(message_id, retry_count + 1)


def main(prompt="A Rhinoceros in a amazon, photorealistic, 4k"):
    # Generate the image
    image_res = requests.post(
        f"{BASE_URL}/imagine", headers=AUTH_HEADERS, json={"msg": prompt}
    )
    image_response_data = image_res.json()
    print("\n=====================")
    print("IMAGE GENERATION MESSAGE DATA")
    print(image_response_data)
    print("=====================")

    completed_image_data = fetch_to_completion(image_response_data["messageId"], 0)

    print("\n=====================")
    print("COMPLETED IMAGE DATA")
    print(completed_image_data)
    print("=====================")

    # Invoke a variation
    variation_res = requests.post(
        f"{BASE_URL}/button",
        headers=AUTH_HEADERS,
        json={
            "button": "V1",
            "buttonMessageId": completed_image_data["response"]["buttonMessageId"],
        },
    )
    variation_response_data = variation_res.json()
    print("\n=====================")
    print("IMAGE VARIATION MESSAGE DATA")
    print(variation_response_data)
    print("=====================")

    completed_variation_data = fetch_to_completion(
        variation_response_data["messageId"], 0
    )

    print("\n=====================")
    print("COMPLETED VARIATION DATA")
    print(completed_variation_data)
    print("=====================")


if __name__ == "__main__":
    main()


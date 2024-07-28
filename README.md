# Keylogger

A simple yet effective Keylogger made from Python

----------------------

How it works:

This keylogger works by reading key presses using the module "Keyboard"

This module reads the keypresses and sends the data to a text file (Keylogged.txt)

From here, the function send_to_webhook reads the file contents and sends it to the webhook URL

To prevent bloating and resending of the same text to the webhook, the file contents of the text file are erased completely

The process continues

----------------------

Use it as you want, I don't care.

made by Themanhimself115

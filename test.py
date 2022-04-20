from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s')
    
def on_press(key):
    if key == Key.esc:
        return False
    logging.info(key)

with Listener(on_press=on_press) as listener:
    listener.join()
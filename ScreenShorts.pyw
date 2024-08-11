from PIL import ImageGrab
import time
import os
from datetime import datetime
import keyboard 


if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

def capture_screenshots(interval=5):
    try:
        while True:
            
            if keyboard.is_pressed('Pause'):
                print("Stopping screenshot capture...")
                break
            
            
            screenshot = ImageGrab.grab()
            
            
            timestamp = datetime.now().strftime("%d-%m-%Y_%Hg%Mp%Ss")
            
            
            filename = f"screenshots/screenshot_{timestamp}.png"
            screenshot.save(filename)
            
            print(f"Saved {filename}")  
            
            
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Screenshot capture stopped.")

if __name__ == "__main__":
    capture_screenshots(interval=5)

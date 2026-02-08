import time
import sys
from tkinter import Tk, Canvas

# Function to convert each character to its 8-bit binary representation (simulated ADC conversion)
def adc_convert_to_binary(word):
    binary_data = []
    for char in word:
        ascii_value = ord(char)  # Get ASCII value
        binary_value = format(ascii_value, '08b')  # Convert ASCII to 8-bit binary
        binary_data.append(binary_value)  # Store the binary value for each character
        print(f"Simulated ADC converting '{char}' to binary: {binary_value}", end='', flush=True)
        #time.sleep(0.1)  # Simulate the ADC processing time
    return ''.join(binary_data)

# Function to blink the screen based on binary data
def blink_screen(binary_data, on_duration=0.3, off_duration=0.5):  # Increased duration
    root = Tk()
    root.attributes("-fullscreen", False)  # Fullscreen mode
    canvas = Canvas(root, bg="black")
    canvas.pack(fill="both", expand=True)
    
    try:
        for bit in binary_data:
            # Log each bit being processed
            print(f"Current Bit: {bit}")
            
            if bit == '1':
                canvas.configure(bg="white")  # Light on
            elif bit == '0':
                canvas.configure(bg="gray")  # Light off
            else:
                canvas.configure(bg="black")
            root.update()

            time.sleep(on_duration)  # Duration of light on/off
            # canvas.configure(bg="black")  # Reset to black for off
            # root.update()
            # time.sleep(off_duration)  # Gap between bits
    finally:
        root.destroy()

# Main script
if __name__ == "__main__":
    message = "hello world"
    binary_message = adc_convert_to_binary(message)  # Get the binary sequence using ADC
    modified_message = []
    modified_message.append('2222222222222222')
    for i in range(len(binary_message)):
        modified_message.append(binary_message[i] + '2')
    modified_message.append('2222222222222222')

    print(f"Binary representation of '{message}': {binary_message}")

    modified_message = ''.join(modified_message)
    print(modified_message)

    blink_screen(modified_message)  # Blink the screen based on binary data
import pandas as pd

# Function to process CSV file and extract lux readings
def process_csv(file_path):
    # Read the CSV file
    data = pd.read_csv(file_path)
    
    # Assuming the CSV file has a column named 'Lux'
    if "Illuminance (lx)" not in data.columns:
        raise ValueError("The CSV file must contain a 'Lux' column.")
    
    lux_readings = data["Illuminance (lx)"].tolist()
    return lux_readings

# Function to simulate DAC: Convert lux readings to binary
def simulate_dac(lux_readings, threshold=50):
    binary_data = []
    for lux in lux_readings:
        # Convert lux value to binary using a threshold
        bit = '1' if lux > threshold else '0'
        binary_data.append(bit)
    return ''.join(binary_data)

# Function to convert binary data into original string
def binary_to_string(binary_data):
    # Ensure binary data length is a multiple of 8
    if len(binary_data) % 8 != 0:
        raise ValueError("Binary data length must be a multiple of 8.")
    
    characters = []
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]  # Extract 8 bits
        char = chr(int(byte, 2))  # Convert binary to character
        characters.append(char)
    
    return ''.join(characters)

# Main function to execute the process
def main():
    # Replace 'your_file.csv' with the path to your CSV file
    file_path = 'Raw Data.csv'
    
    # Step 1: Process CSV file to get lux readings
    lux_readings = process_csv(file_path)
    print("Lux readings:", lux_readings)
    
    # Step 2: Simulate DAC to convert lux readings to binary
    binary_data = simulate_dac(lux_readings, threshold=50)  # Adjust threshold if needed
    print("Binary data:", binary_data)
    
    # Step 3: Convert binary data back to original string
    original_message = binary_to_string(binary_data)
    print("Original message:", original_message)

# Run the main function
if __name__ == "__main__":
    main()
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Read CSV file
def read_csv_file(file_path):
    try:
        data = pd.read_csv(file_path, header=0)  
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    except pd.errors.EmptyDataError:
        print("No data in file. Please check file contents.")
        return None

# Find local maxima
def find_local_maxima(data):
    y_values = data.iloc[:, 1].values  
    peaks, _ = find_peaks(y_values)  
    return peaks

# Create line graph with local maxima highlighted
def plot_data_with_maxima(data, maxima_indices, value):
    x_values = data.iloc[:, 0]
    y_values = data.iloc[:, 1]

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, marker='o', label="Illuminance")
    
    # Highlight maxima
    plt.scatter(x_values.iloc[maxima_indices], y_values.iloc[maxima_indices],
                color='red', label="Local Maxima", zorder=5)
    
    plt.xlabel("Time (s)")
    plt.ylabel("Illuminance (lx)")
    plt.title(f"Illuminance over Time with Local Maxima for {value}")
    plt.grid(True)
    plt.legend()
    plt.show()

# Filter maxima
def filter_maxima(data, maxima_indices, upper_threshold, lower_threshold):
    maxima_values = data.iloc[maxima_indices].values
    filtered_maxima = [1 if value[1] > upper_threshold else 0 if value[1] > lower_threshold else 2 for value in maxima_values]
    return filtered_maxima

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

# Main function
def main():
    file_path = input("Enter CSV file path: ")
    data = read_csv_file(file_path)
    
    if data is not None:
        maxima_indices = find_local_maxima(data)
        print(f"Local maxima indices: {maxima_indices}")
        print(f"Local maxima values: {data.iloc[maxima_indices].values}")
        filtered_maxima = filter_maxima(data, maxima_indices, upper_threshold=20, lower_threshold=10.5)
        print(f"Filtered maxima: {filtered_maxima}")
        filtered_maxima_str = ''.join(str(x) for x in filtered_maxima if x is not None)
        print(f"Filtered maxima: {filtered_maxima_str}")
        filtered_maxima_str = filtered_maxima_str.replace('2', '')
        print(f"Filtered maxima: {filtered_maxima_str}")

        value = binary_to_string(filtered_maxima_str)
        print(f"\nDecoded value from Lifi Signal: {value}")

        plot_data_with_maxima(data, maxima_indices, value)

if __name__ == "__main__":
    main()
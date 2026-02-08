import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Read CSV file
def read_csv_file(file_path):
    try:
        data = pd.read_csv(file_path, header=0)  # header=0 to treat first row as headers
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    except pd.errors.EmptyDataError:
        print("No data in file. Please check file contents.")
        return None

# Find local maxima
def find_local_maxima(data):
    y_values = data.iloc[:, 1].values  # Assuming the second column contains y-values
    peaks, _ = find_peaks(y_values)  # Detect peaks
    return peaks

# Create line graph with local maxima highlighted
def plot_data_with_maxima(data, maxima_indices):
    x_values = data.iloc[:, 0]
    y_values = data.iloc[:, 1]

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, marker='o', label="Illuminance Data")
    
    # Highlight maxima
    plt.scatter(x_values.iloc[maxima_indices], y_values.iloc[maxima_indices],
                color='red', label="Local Maxima", zorder=5)
    
    plt.xlabel("Time (s)")
    plt.ylabel("Illuminance (lx)")
    plt.title("Illuminance over Time with Local Maxima")
    plt.grid(True)
    plt.legend()
    plt.show()

# Main function
def main():
    file_path = input("Enter CSV file path: ")
    data = read_csv_file(file_path)
    
    if data is not None:
        maxima_indices = find_local_maxima(data)
        print(f"Local maxima indices: {maxima_indices}")
        print(f"Local maxima values: {data.iloc[maxima_indices].values}")
        plot_data_with_maxima(data, maxima_indices)

if __name__ == "__main__":
    main()

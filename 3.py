import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file, skipping the first row (headers)
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


# Create line graph
def plot_data(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data.iloc[:, 0], data.iloc[:, 1], marker='o')
    plt.xlabel("Time (s)")
    plt.ylabel("Illuminance (lx)")
    plt.title("Illuminance over Time")
    plt.grid(True)
    plt.show()


# Main function
def main():
    # file_path = input("Enter CSV file path: ")
    file_path = "Raw Data.csv"
    data = read_csv_file(file_path)
    
    if data is not None:
        plot_data(data)


if __name__ == "__main__":
    main()
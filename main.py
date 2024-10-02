import os
import tkinter as tk
from tkinter import filedialog
from compression_algorithms.lz77 import compress_file_lz77, decompress_file_lz77
from compression_algorithms.lzw import compress_file_lzw, decompress_file_lzw
from compression_algorithms.shannon_fano import compress_file_shannon_fano, decompress_file_shannon_fano
from utils.file_viewer import print_file_contents

# Global variable to hold the selected input file and its compressed versions
input_file = None
compressed_files = {}

def select_file():
    global input_file
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text Files", "*.txt")])
    
    if file_path:
        input_file = file_path
        print(f"Selected file: '{input_file}'")
    else:
        print("No file selected. Please try again.")

def compress_file(algorithm):
    global compressed_files
    print(f"Compressing using {algorithm}...")
    if input_file:
        # Extract the file name without the extension
        base_name = os.path.basename(input_file)
        compressed_file = os.path.join('data', f'{base_name}.{algorithm.lower()}')

        try:
            if algorithm == 'Shannon-Fano':
                tree = compress_file_shannon_fano(input_file, compressed_file)
                compressed_files['Shannon-Fano'] = (compressed_file, tree)
            elif algorithm == 'LZ77':
                compress_file_lz77(input_file, compressed_file)
                compressed_files['LZ77'] = compressed_file
            elif algorithm == 'LZW':
                compress_file_lzw(input_file, compressed_file)
                compressed_files['LZW'] = compressed_file

            print(f"File '{input_file}' has been compressed using {algorithm}:\nOutput file: '{compressed_file}'")
        except Exception as e:
            print(f"An error occurred while compressing the file: {str(e)}")
    else:
        print("No file selected. Please select a file first.")

def decompress_file(algorithm):
    print(f"Decompressing using {algorithm}...")
    if algorithm in compressed_files:
        compressed_file = compressed_files[algorithm][0] if algorithm == 'Shannon-Fano' else compressed_files[algorithm]
        base_name = os.path.basename(compressed_file)
        decompressed_file = os.path.join('data', f'decompressed_{base_name}')

        try:
            if algorithm == 'Shannon-Fano':
                tree = compressed_files['Shannon-Fano'][1]
                decompress_file_shannon_fano(compressed_file, decompressed_file, tree)
            elif algorithm == 'LZ77':
                decompress_file_lz77(compressed_file, decompressed_file)
            elif algorithm == 'LZW':
                decompress_file_lzw(compressed_file, decompressed_file)

            print(f"File '{compressed_file}' has been decompressed using {algorithm}:\nOutput file: '{decompressed_file}'")
        except Exception as e:
            print(f"An error occurred while decompressing the file: {str(e)}")
    else:
        print("No compressed file available for the selected algorithm.")

def view_compressed_files():
    print("Viewing compressed files in 'data' directory...")
    
    # Check if the data directory exists
    if not os.path.exists('data'):
        print("The 'data' directory does not exist.")
        return

    compressed_files = [f for f in os.listdir('data') if f.endswith(('.shannon-fano', '.lz77', '.lzw')) and not f.startswith('decompressed_')]
    
def view_compressed_files():
    print("Viewing compressed files in 'data' directory...")
    
    # Check if the data directory exists
    if not os.path.exists('data'):
        print("The 'data' directory does not exist.")
        return

    compressed_files = [f for f in os.listdir('data') if f.endswith(('.shannon-fano', '.lz77', '.lzw')) and not f.startswith('decompressed_')]
    
    if compressed_files:
        for file in compressed_files:
            file_path = os.path.join('data', file)
            print(f"\nContents of '{file}':")
            try:
                with open(file_path, 'rb') as f:  # Open in binary mode
                    contents = f.read()
                    
                    # Attempt to decode contents as text
                    try:
                        text_output = contents.decode('utf-8')  # Try decoding to string
                        print("Text content:")

                        print(text_output)
                    except (UnicodeDecodeError, TypeError):
                        # If decoding fails, fall back to displaying in hexadecimal format
                        print("Failed to decode as text...!!\n")

                        print("Displaying in hexadecimal format:\n")
                        hex_output = contents.hex()  # Convert to hexadecimal representation
                        for i in range(0, len(hex_output), 32):  # Print in chunks for readability
                            print(hex_output[i:i + 32])
            except Exception as e:
                print(f"Error reading file '{file}': {str(e)}")
    else:
        print("No compressed files found in the 'data' directory.")


def view_decompressed_files():
    print("Viewing decompressed files in 'data' directory...")
    
    # Check if the data directory exists
    if not os.path.exists('data'):
        print("The 'data' directory does not exist.")
        return

    decompressed_files = [f for f in os.listdir('data') if f.startswith('decompressed_')]

    if decompressed_files:
        for file in decompressed_files:
            file_path = os.path.join('data', file)
            print(f"\nContents of '{file}':")
            try:
                with open(file_path, 'r', encoding='utf-8') as f:  # Open in text mode for readable files
                    contents = f.read()
                    print(contents)
            except Exception as e:
                print(f"Error reading file '{file}': {str(e)}")
    else:
        print("No decompressed files found in the 'data' directory.")

def main():
    # Ensure data directory exists
    if not os.path.exists('data'):
        os.makedirs('data')

    while True:
        print("\n--- Compression Algorithms Menu ---")
        print("1. Select File")
        print("2. Compress using Shannon-Fano")
        print("3. Compress using LZ77")
        print("4. Compress using LZW")
        print("5. Decompress Files")
        print("6. View Compressed Files")
        print("7. View Decompressed Files")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            select_file()
        elif choice == '2':
            compress_file('Shannon-Fano')
            decompress_file('Shannon-Fano')
        elif choice == '3':
            compress_file('LZ77')
            decompress_file('LZ77')
        elif choice == '4':
            compress_file('LZW')
            decompress_file('LZW')
        elif choice == '5':
            print("Decompressing files...")
            decompress_file('Shannon-Fano')
            decompress_file('LZ77')
            decompress_file('LZW')
        elif choice == '6':
            view_compressed_files()
        elif choice == '7':
            view_decompressed_files()
        elif choice == '8':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

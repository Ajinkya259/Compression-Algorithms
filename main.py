import tkinter as tk
from tkinter import filedialog
from compression_algorithms.lz77 import compress_file_lz77, decompress_file_lz77
from compression_algorithms.lzw import compress_file_lzw, decompress_file_lzw
from compression_algorithms.shannon_fano import compress_file_shannon_fano, decompress_file_shannon_fano
from compression_algorithms.hybrid import compress_file_hybrid, decompress_file_hybrid
import os

class CompressionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Compression Algorithms")
        self.root.geometry("600x400")

        self.folder_path = tk.StringVar()  # Variable to hold selected folder path
        self.input_file = None
        self.compressed_files = {}

        # Add heading label
        heading_label = tk.Label(self.root, text="Implementation of File Compression-Decompression Algorithms", font=("Arial", 14, "bold"))
        heading_label.pack(pady=10)

        # File selection
        folder_frame = tk.Frame(self.root)
        folder_frame.pack(pady=10)

        tk.Label(folder_frame, text="Select File:").pack(side=tk.LEFT, padx=10, pady=10)
        tk.Entry(folder_frame, textvariable=self.folder_path, width=50).pack(side=tk.LEFT, padx=10, pady=10)

        tk.Button(folder_frame, text="Browse", command=self.browse_file).pack(side=tk.LEFT, padx=10, pady=10)

        # Output text display (dynamic)
        self.output_text = tk.StringVar()
        output_label = tk.Label(self.root, textvariable=self.output_text, wraplength=500, justify='left')
        output_label.pack(pady=10, side=tk.BOTTOM)

        # Button layout
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        # Button definitions
        compress_sf_button = tk.Button(button_frame, text="Compress using Shannon-Fano", command=lambda: self.compress_file('Shannon-Fano'), width=25)
        compress_lz77_button = tk.Button(button_frame, text="Compress using LZ77", command=lambda: self.compress_file('LZ77'), width=25)
        compress_lzw_button = tk.Button(button_frame, text="Compress using LZW", command=lambda: self.compress_file('LZW'), width=25)
        compress_hybrid_button = tk.Button(button_frame, text="Compress using Hybrid", command=lambda: self.compress_file('Hybrid'), width=25)
        decompress_button = tk.Button(button_frame, text="Decompress Files", command=self.decompress_files, width=25)
        view_compressed_button = tk.Button(button_frame, text="View Compressed Files", command=self.view_compressed_files, width=25)
        view_decompressed_button = tk.Button(button_frame, text="View Decompressed Files", command=self.view_decompressed_files, width=25)
        exit_button = tk.Button(button_frame, text="Exit", command=self.exit_program, width=25)

        # Pack buttons in grid layout
        compress_sf_button.pack(pady=5)
        compress_lz77_button.pack(pady=5)
        compress_lzw_button.pack(pady=5)
        compress_hybrid_button.pack(pady=5)
        decompress_button.pack(pady=5)
        view_compressed_button.pack(pady=5)
        view_decompressed_button.pack(pady=5)
        exit_button.pack(pady=5)

    def browse_file(self):
        file_selected = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text Files", "*.txt")])
        if file_selected:
            self.input_file = file_selected  # Set the selected file path
            self.folder_path.set(os.path.dirname(file_selected))  # Set the folder path from the selected file
            self.output_text.set(f"Selected file: '{file_selected}'")
        else:
            self.output_text.set("No file selected. Please try again.")

    def compress_file(self, algorithm):
        if self.input_file:
            base_name = os.path.basename(self.input_file)
            compressed_file = os.path.join('data', f'{base_name}.{algorithm.lower()}')
            
            try:
                if algorithm == 'Shannon-Fano':
                    tree = compress_file_shannon_fano(self.input_file, compressed_file)
                    self.compressed_files['Shannon-Fano'] = (compressed_file, tree)
                elif algorithm == 'LZ77':
                    compress_file_lz77(self.input_file, compressed_file)
                    self.compressed_files['LZ77'] = compressed_file
                elif algorithm == 'LZW':
                    compress_file_lzw(self.input_file, compressed_file)
                    self.compressed_files['LZW'] = compressed_file
                elif algorithm == 'Hybrid':
                    tree = compress_file_hybrid(self.input_file, compressed_file)
                    self.compressed_files['Hybrid'] = (compressed_file, tree)

                self.output_text.set(f"File '{self.input_file}' has been compressed using {algorithm}.\nOutput file: '{compressed_file}'")
            except Exception as e:
                self.output_text.set(f"Error during compression: {str(e)}")
        else:
            self.output_text.set("No file selected. Please select a file first.")

    def decompress_files(self):
        if self.compressed_files:
            try:
                for algorithm, data in self.compressed_files.items():
                    compressed_file = data[0] if algorithm in ['Shannon-Fano', 'Hybrid'] else data
                    decompressed_file = os.path.join('data', f'decompressed_{os.path.basename(compressed_file)}')

                    if algorithm == 'Shannon-Fano':
                        tree = self.compressed_files['Shannon-Fano'][1]
                        decompress_file_shannon_fano(compressed_file, decompressed_file, tree)
                    elif algorithm == 'LZ77':
                        decompress_file_lz77(compressed_file, decompressed_file)
                    elif algorithm == 'LZW':
                        decompress_file_lzw(compressed_file, decompressed_file)
                    elif algorithm == 'Hybrid':
                        tree = self.compressed_files['Hybrid'][1]
                        decompress_file_hybrid(compressed_file, decompressed_file)

                self.output_text.set("Decompression completed for all algorithms.")
            except Exception as e:
                self.output_text.set(f"Error during decompression: {str(e)}")
        else:
            self.output_text.set("No files have been compressed yet.")

    def view_compressed_files(self):
        try:
            ordered_files = ['Shannon-Fano', 'LZ77', 'LZW', 'Hybrid']
            contents = ""

            for algorithm in ordered_files:
                if algorithm in self.compressed_files:
                    compressed_file = self.compressed_files[algorithm][0] if algorithm in ['Shannon-Fano', 'Hybrid'] else self.compressed_files[algorithm]
                    contents += f"\nContents of '{compressed_file}':\n"
                    
                    with open(compressed_file, 'rb') as f:
                        contents += f.read().hex() + "\n"
            
            if contents:
                self.output_text.set(contents)
            else:
                self.output_text.set("No compressed files found.")
        except Exception as e:
            self.output_text.set(f"Error: {str(e)}")

    def view_decompressed_files(self):
        try:
            files = [f for f in os.listdir('data') if f.startswith('decompressed_')]
            if files:
                contents = "\nDecompressed Files:\n"
                for file in files:
                    file_path = os.path.join('data', file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        contents += f"\nContents of '{file}':\n"
                        contents += f.read() + "\n"
                self.output_text.set(contents)
            else:
                self.output_text.set("No decompressed files found.")
        except Exception as e:
            self.output_text.set(f"Error: {str(e)}")

    def exit_program(self):
        self.root.quit()

# Create the main window
root = tk.Tk()
app = CompressionApp(root)
root.mainloop()

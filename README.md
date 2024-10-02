# Compression Algorithms Project

## Overview
This project implements three popular compression algorithms: LZ77, LZW, and Shannon-Fano. The application allows users to compress and decompress text files, providing insights into the contents of compressed files in both text and hexadecimal formats.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Usage](#usage)
- [Algorithms](#algorithms)
- [License](#license)

## Features
- **Compression**: Compress text files using LZ77, LZW, or Shannon-Fano algorithms.
- **Decompression**: Decompress files that were previously compressed.
- **View Contents**: View compressed file contents in text or hexadecimal format.
- **User-Friendly Interface**: A simple console-based menu for easy navigation.

## Technologies Used
- **Python**: The programming language used for implementation.
- **Tkinter**: For file selection dialog.
- **Custom Compression Algorithms**: Implementations of LZ77, LZW, and Shannon-Fano algorithms.

## Setup
To set up the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ajinkya259/compression-algorithms.git
   cd compression-algorithms
2. **Install Required Packages**:Ensure you have Python installed. Install any required packages using:
    pip install -r requirements.txt
3. **Create the Data Directory**: The application will create a data directory to store compressed and decompressed files. Ensure the directory is created during the execution of the program.


## Usage
**Run the Application**:
    python main.py
    
1. Select a File: Choose a text file to compress.

2. Compress Files: Use the menu options to compress the selected file using LZ77, LZW, or Shannon-Fano.

3. Decompress Files: Decompress files using the corresponding options in the menu.

4. View Compressed and Decompressed Files: Check the contents of compressed files in both text and hexadecimal formats.

## Algorithms
1. LZ77
LZ77 compression algorithm utilizes a sliding window approach to replace repeated occurrences of data with references.

2. LZW
LZW (Lempel-Ziv-Welch) is a dictionary-based compression algorithm that replaces repeated sequences of data with a single reference.

3. Shannon-Fano
Shannon-Fano is a variable-length prefix coding algorithm that encodes symbols based on their frequencies, providing better compression for frequently occurring symbols.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Thanks to the creators of the compression algorithms and libraries that assisted in developing this project.


### Notes:
- **Replace `ajinkya259`**: Be sure to replace `https://github.com/ajinkya259/compression-algorithms.git` with the actual URL of your repository.
- **Installation Instructions**: Adjust the installation instructions as necessary depending on any additional dependencies or steps required for your project.
- **Additional Sections**: Feel free to add sections like "Contributing" or "Future Work" if relevant to your project. 

This `README.md` provides a clear and concise overview of your project, making it easy for others to understand and use your application.

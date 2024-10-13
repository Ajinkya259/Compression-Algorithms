import pickle
from compression_algorithms.lz77 import lz77_compress, lz77_decompress
from compression_algorithms.lzw import lzw_compress, lzw_decompress
from compression_algorithms.shannon_fano import build_shannon_fano_tree, encode_shannon_fano, decode_shannon_fano

def hybrid_compress(data):
    """
    Compress data using a hybrid algorithm (Shannon-Fano followed by LZ77).
    Returns a tuple of compressed data and necessary metadata (tree or dictionaries).
    """
    try:
        # Step 1: Shannon-Fano encoding
        shannon_tree = build_shannon_fano_tree(data)
        shannon_encoded_data = encode_shannon_fano(data, shannon_tree)
        print("Shannon-Fano compression completed.")

        # Step 2: LZ77 compression on the Shannon-Fano output
        lz77_compressed_data = lz77_compress(shannon_encoded_data)
        print("LZ77 compression completed.")

        return lz77_compressed_data, shannon_tree  # returning compressed data and the tree for decompression

    except Exception as e:
        print(f"Error during hybrid compression: {e}")

def hybrid_decompress(compressed_data, shannon_tree):
    """
    Decompress data that was compressed using the hybrid algorithm.
    Requires the compressed data and the Shannon-Fano tree.
    """
    try:
        # Step 1: LZ77 decompression
        lz77_decompressed_data = lz77_decompress(compressed_data)
        print("LZ77 decompression completed.")

        # Step 2: Shannon-Fano decoding on the LZ77 decompressed output
        decoded_data = decode_shannon_fano(lz77_decompressed_data, shannon_tree)
        print("Shannon-Fano decompression completed.")

        return decoded_data

    except Exception as e:
        print(f"Error during hybrid decompression: {e}")

def compress_file_hybrid(input_file, output_file):
    """
    Compress the contents of a text file using the hybrid compression algorithm.
    Saves compressed data and metadata to an output file.
    """
    try:
        # Read the input file
        with open(input_file, 'r') as file:
            data = file.read()

        # Compress the data using the hybrid algorithm
        compressed_data, shannon_tree = hybrid_compress(data)

        # Save the compressed data and tree using pickle
        with open(output_file, 'wb') as file:
            pickle.dump((compressed_data, shannon_tree), file)

        print(f"File '{input_file}' compressed successfully to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred during file compression: {e}")
def decompress_file_hybrid(input_file, output_file):
    """
    Decompress a file that was compressed using the hybrid algorithm.
    Writes the decompressed data to the specified output file.
    """
    try:
        # Load compressed data and tree
        with open(input_file, 'rb') as file:
            compressed_data, shannon_tree = pickle.load(file)

        # Decompress the data
        decoded_data = hybrid_decompress(compressed_data, shannon_tree)

        # Write the decompressed data
        with open(output_file, 'w') as file:
            file.write(decoded_data)

        print(f"File '{input_file}' decompressed successfully to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except pickle.UnpicklingError:
        print(f"Error: The file '{input_file}' does not contain valid compressed data.")
    except Exception as e:
        print(f"An unexpected error occurred during decompression: {e}")
def decompress_file_hybrid(input_file, output_file):
    """
    Decompress a file that was compressed using the hybrid algorithm.
    Writes the decompressed data to the specified output file.
    """
    try:
        # Load compressed data and tree
        with open(input_file, 'rb') as file:
            compressed_data, shannon_tree = pickle.load(file)

        # Decompress the data
        decoded_data = hybrid_decompress(compressed_data, shannon_tree)

        # Write the decompressed data
        with open(output_file, 'w') as file:
            file.write(decoded_data)

        print(f"File '{input_file}' decompressed successfully to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except pickle.UnpicklingError:
        print(f"Error: The file '{input_file}' does not contain valid compressed data.")
    except Exception as e:
        print(f"An unexpected error occurred during decompression: {e}")


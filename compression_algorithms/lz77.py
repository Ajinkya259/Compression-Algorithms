import pickle

def lz77_compress(data, window_size=20):
    i = 0
    output = []
    while i < len(data):
        match = (0, 0, data[i])
        for j in range(max(0, i - window_size), i):
            length = 0
            while (i + length < len(data) and data[j + length] == data[i + length]):
                length += 1
            if length > match[1]:
                match = (i - j, length, data[i + length] if i + length < len(data) else '')
        i += match[1] + 1
        output.append(match)
    return output

def lz77_decompress(compressed):
    decompressed = []
    for distance, length, char in compressed:
        if distance == 0:
            decompressed.append(char)
        else:
            start = len(decompressed) - distance
            for i in range(length):
                decompressed.append(decompressed[start + i])
            decompressed.append(char)
    return ''.join(decompressed)


def compress_file_lz77(input_file, output_file):
    with open(input_file, 'r') as file:
        data = file.read()
    compressed_data = lz77_compress(data)
    with open(output_file, 'wb') as file:
        pickle.dump(compressed_data, file)

def decompress_file_lz77(input_file, output_file):
    try:
        with open(input_file, 'rb') as file:
            compressed_data = pickle.load(file)
        decoded_data = lz77_decompress(compressed_data)
        with open(output_file, 'w') as file:
            file.write(decoded_data)
        print(f"Successfully decompressed '{input_file}' to '{output_file}' using LZ77.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except pickle.UnpicklingError:
        print(f"Error: The file '{input_file}' does not contain valid compressed data.")
    except Exception as e:
        print(f"An unexpected error occurred during decompression: {str(e)}")
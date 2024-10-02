import pickle

def lzw_compress(data):
    dictionary = {chr(i): i for i in range(256)}
    w = ''
    compressed = []
    for c in data:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            compressed.append(dictionary[w])
            dictionary[wc] = len(dictionary)
            w = c
    if w:
        compressed.append(dictionary[w])
    return compressed

def lzw_decompress(compressed):
    dictionary = {i: chr(i) for i in range(256)}
    w = chr(compressed.pop(0))
    decompressed = [w]
    for k in compressed:
        entry = dictionary[k] if k in dictionary else w + w[0]
        decompressed.append(entry)
        dictionary[len(dictionary)] = w + entry[0]
        w = entry
    return ''.join(decompressed)

def compress_file_lzw(input_file, output_file):
    with open(input_file, 'r') as file:
        data = file.read()
    compressed_data = lzw_compress(data)
    with open(output_file, 'wb') as file:
        pickle.dump(compressed_data, file)

def decompress_file_lzw(input_file, output_file):
    try:
        with open(input_file, 'rb') as file:
            compressed_data = pickle.load(file)
        decoded_data = lzw_decompress(compressed_data)
        with open(output_file, 'w') as file:
            file.write(decoded_data)
        print(f"Successfully decompressed '{input_file}' to '{output_file}' using LZW.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except pickle.UnpicklingError:
        print(f"Error: The file '{input_file}' does not contain valid compressed data.")
    except Exception as e:
        print(f"An unexpected error occurred during decompression: {str(e)}")
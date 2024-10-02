from collections import Counter

class ShannonFanoNode:
    def __init__(self, symbols=None):
        self.symbols = symbols
        self.left = None
        self.right = None

def shannon_fano(symbols):
    if len(symbols) == 1:
        return [(symbols[0][0],'')]
    total = sum(symbol[1] for symbol in symbols)
    cumulative = 0
    for i, symbol in enumerate(symbols):
        cumulative += symbol[1]
        if cumulative >= total / 2:
            break
    left = shannon_fano(symbols[:i + 1])
    right = shannon_fano(symbols[i + 1:])
    return [(symbol[0], '0' + code) for symbol, code in left] + [(symbol[0], '1' + code) for symbol, code in right]

def build_shannon_fano_tree(data):
    freq = Counter(data)
    symbols = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    codes = shannon_fano(symbols)
    return {symbol: code for symbol, code in codes}

def encode_shannon_fano(data, tree):
    return ''.join(tree[symbol] for symbol in data)

def decode_shannon_fano(encoded, tree):
    reverse_tree = {code: symbol for symbol, code in tree.items()}
    code = ''
    decoded = ''
    for bit in encoded:
        code += bit
        if code in reverse_tree:
            decoded += reverse_tree[code]
            code = ''
    return decoded

def compress_shannon_fano(data):
    tree = build_shannon_fano_tree(data)
    encoded_data = encode_shannon_fano(data, tree)
    return encoded_data, tree

def decompress_shannon_fano(encoded_data, tree):
    return decode_shannon_fano(encoded_data, tree)

def compress_file_shannon_fano(input_file, output_file):
    with open(input_file, 'r') as file:
        data = file.read()
    encoded_data, tree = compress_shannon_fano(data)
    with open(output_file, 'w') as file:
        file.write(encoded_data)
    return tree

def decompress_file_shannon_fano(input_file, output_file, tree):
    with open(input_file, 'r') as file:
        encoded_data = file.read()
    decoded_data = decompress_shannon_fano(encoded_data, tree)
    with open(output_file, 'w') as file:
        file.write(decoded_data)

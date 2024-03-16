import sys
from collections import Counter

class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def huffman_encoding(data):
    if not data:
        return "", None

    if len(set(data)) == 1:
        char = data[0]
        return '0' * len(data), Node(char)

    freq = Counter(data)

    nodes = [Node(char, freq) for char, freq in freq.items()]
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)
        parent = Node(freq=left.freq + right.freq)
        parent.left = left
        parent.right = right
        nodes.append(parent)

    root = nodes[0]

    codes = {}
    def generate_codes(node, code=""):
        if node.char:
            codes[node.char] = code
        else:
            generate_codes(node.left, code + "0")
            generate_codes(node.right, code + "1")
    generate_codes(root)

    encoded_data = ''.join(codes[char] for char in data)

    return encoded_data, root

def huffman_decoding(data, tree):
    if not data or not tree:
        return ""

    decoded_data = ""
    current_node = tree

    for bit in data:
        if bit == "0":
            if current_node.left:
                current_node = current_node.left
        else:
            if current_node.right:
                current_node = current_node.right

        if current_node.char:
            decoded_data += current_node.char
            current_node = tree

    return decoded_data

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    # Test case 1: Empty String
    print ("# Test case 1: Empty String\n")
    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    if encoded_data:
        print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    else:
        print("The size of the encoded data is: 0\n")
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


    # Test case 2: Single character
    print ("# Test case 2: Single character\n")
    a_great_sentence = "a"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    if encoded_data:
        print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    else:
        print("The size of the encoded data is: 0\n")
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    # Test case 3: Repeated single character
    print ("# Test case 3: Repeated single character\n")
    a_great_sentence = "aaaaaaaaaaaa"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    if encoded_data:
        print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    else:
        print("The size of the encoded data is: 0\n")
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
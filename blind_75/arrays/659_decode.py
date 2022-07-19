class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def __init__(self):
        self.encoded_string = None

    def encode(self, strs):
        for s in strs:
            delimiter = str(len(s)) + "#"
            self.encoded_string += delimiter + s

        return self.encoded_string

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """

    def decode(self, str):
        output, i = [], 0
        while i < len(self.encoded_string):
            j = i
            while self.encoded_string[j] != "#":
                j += 1
            length = int(self.encoded_string[i:j])
            output.append(self.encoded_string[j + 1:j + 1 + length])
            i = j + 1 + length

        return output

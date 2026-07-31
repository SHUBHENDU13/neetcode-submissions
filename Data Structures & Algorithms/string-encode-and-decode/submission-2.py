class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            encoded.append(str(len(word)))
            encoded.append('*')
        encoded.append('#')
        input_string = ''.join(strs)
        encoded.append(input_string)
        encoded_string = ''.join(encoded)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        i = 0
        while s[i] != '#':
            i += 1
        phrase = s[i+1:]
        key = s[:i].split('*')
        decoded = []
        idx = 0
        for len_str in key:
            if len_str:
                word_length = int(len_str)
                word = phrase[idx : idx + word_length]
                decoded.append(word)
                idx += word_length
        return decoded

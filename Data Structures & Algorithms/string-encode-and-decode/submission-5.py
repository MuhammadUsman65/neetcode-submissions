class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":   # find the '#' separator
                j += 1
            length = int(s[i:j])  # read the length
            result.append(s[j+1 : j+1+length])  # read exactly that many chars
            i = j + 1 + length
        return result
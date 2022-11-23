class Solution:
    def isValid(self, s: str) -> bool:
        needed = []

        dict = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for p in s:
            if p in dict.keys():
                if not needed or needed[-1] != dict[p]:
                    return False
                needed.pop()
            else:
                needed.append(p)

        return len(needed) == 0

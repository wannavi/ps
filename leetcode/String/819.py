from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        pure = ''.join(
            [char if char.isalnum() else ' ' for char in paragraph.lower()])

        separated = [word for word in pure.split() if word not in banned]
        count = Counter(separated)

        return count.most_common(1)[0][0]

    def mostCommonWord1(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^[\w]', ' ', paragraph).lower().split()
                 if word not in banned]

        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]

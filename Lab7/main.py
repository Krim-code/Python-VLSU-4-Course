class KMP:
    def __init__(self, pattern):
        self.pattern = pattern
        self.lps = [0] * len(pattern)
        self._compute_lps()

    def _compute_lps(self):
        length = 0
        i = 1
        while i < len(self.pattern):
            if self.pattern[i] == self.pattern[length]:
                length += 1
                self.lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = self.lps[length-1]
                else:
                    self.lps[i] = 0
                    i += 1

    def search(self, text):
        m = len(self.pattern)
        n = len(text)
        i = 0
        j = 0
        indices = []
        while i < n:
            if self.pattern[j] == text[i]:
                i += 1
                j += 1
            if j == m:
                indices.append(i - j)
                j = self.lps[j-1]
            elif i < n and self.pattern[j] != text[i]:
                if j != 0:
                    j = self.lps[j-1]
                else:
                    i += 1
        return indices

class PatternChecker:
    def __init__(self, patterns, text):
        self.patterns = patterns
        self.text = text

    def check(self):
        matches = set()
        for pattern in self.patterns:
            kmp = KMP(pattern)
            indices = kmp.search(self.text)
            for index in indices:
                matches.add(self.text[index:index+len(pattern)])
        
        # Проверяем, есть ли несовпадающие подстроки
        return not matches.issubset(set(self.patterns))


if __name__  == "__main__":
    # Пример использования
    patterns = ["pattern1", "pattern2", "pattern3"]
    text = "This is a text with pattern1 and some other patterns."
    checker = PatternChecker(patterns, text)
    print(checker.check())  # Выведет True или False в зависимости от результата

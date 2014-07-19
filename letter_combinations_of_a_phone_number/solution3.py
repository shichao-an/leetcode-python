class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        cand = []
        res = []
        self.letter_combination_aux(0, digits, d, cand, res)
        return res

    def letter_combination_aux(self, i, digits, d, cand, res):
        if i == len(digits):
            res.append(''.join(cand))
        else:
            digit = digits[i]
            if digit in d:
                letters = d[digit]
                for letter in letters:
                    cand.append(letter)
                    self.letter_combination_aux(i + 1, digits, d, cand, res)
                    cand.pop()

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
        self.letter_combination_aux(digits, d, cand, res)
        return res

    def letter_combination_aux(self, digits, d, cand, res):
        if not digits:
            res.append(''.join(cand))
        else:
            digit = digits[0]
            if digit in d:
                letters = d[digit]
                for letter in letters:
                    cand.append(letter)
                    self.letter_combination_aux(digits[1:], d, cand, res)
                    cand.pop()

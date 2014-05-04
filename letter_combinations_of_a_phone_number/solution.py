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
        return self.combinations(digits, 0, d)

    def combinations(self, digits, i, d):
        if i == len(digits):
            return ['']
        else:
            res = []
            rest_combs = self.combinations(digits, i + 1, d)
            for comb in rest_combs:
                number = digits[i]
                letters = d[number]
                for letter in letters:
                    res.append(letter + comb)
            return res

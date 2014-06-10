class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        if not p:
            return not s
        if not s:
            return False
        return self.is_match_aux(s, p, 0, 0)

    def is_match_aux(self, s, p, si, pi):
        if pi == len(p):
            return si == len(s)
        # Next char is not *
        # pi may be the last char
        if pi < len(p) - 1 and p[pi + 1] != '*' or pi == len(p) - 1:
            assert p[pi] != '*'
            # si must be in bound
            is_cur_matched = si < len(s) and (p[pi] == s[si] or p[pi] == '.')
            is_next_matched = self.is_match_aux(s, p, si + 1, pi + 1)
            return is_cur_matched and is_next_matched
        # Next char is *
        while si < len(s) and pi < len(p) and (p[pi] == s[si] or p[pi] == '.'):
            if self.is_match_aux(s, p, si, pi + 2):
                return True
            si += 1
        return self.is_match_aux(s, p, si, pi + 2)


s = Solution()
print s.isMatch("aa", "a")
print s.isMatch("aa", "aa")
print s.isMatch("aaa", "aa")
print s.isMatch("aa", "a*")
print s.isMatch("aa", ".*")
print s.isMatch("ab", ".*")
print s.isMatch("aab", "c*a*b")

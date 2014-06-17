class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        ps = path.split('/')[1:]
        res = []
        for d in ps:
            if d == '..':
                if res:
                    res.pop()
            elif d == '.' or d == '':
                pass
            else:
                res.append(d)
        return '/' + '/'.join(res)

class Solution(object):
    def longest(self, s: str):
        j = []  # temp list
        c = 0  # temp combo
        f = 0  # current max combo
        for i in range(len(s)):
            if s[i] in j:
                if c > f:
                    f = c  # update max combo
                j.clear()
                j.append(s[i])  # reset temp list
                c = 1  # reset temp combo counts
            else:
                j.append(s[i])
                c = c + 1
        f = c
        return f


Solution.longest(self,"abcabc")



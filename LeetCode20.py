# Test program - Leetcode 20
# Trivial - How can you access the element(s) of a list?

class Solution:
    def isValid(self, s: str) -> bool:
        # initialization
        st = []
        ret = False
        # loop to add or remove elements or compare
        for c in range(len(s)):
            if s[c] == '(':
                st.append(')')
            elif s[c] == '{':
                st.append('}')
            elif s[c] == '[':
                st.append(']')
            else:
                if (len(st) == 0):
                    return False
                if st.pop() != s[c]:
                    return False
        return not len(st)
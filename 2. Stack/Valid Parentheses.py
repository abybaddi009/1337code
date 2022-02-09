def closing_bracket(c):
    if c == '{':
        return '}'
    if c == '(':
        return ')'
    if c == '[':
        return ']'

class Solution:
    def isValid(self, s: str) -> bool:
        stack = ['','']

        for c in s:
            if c in ['[', '(', '{']:
                stack.append(c)
            else:
                top = stack.pop()
                if closing_bracket(top) != c:
                    return False
        if len(stack) == 2:
            return True
        else:
            return False
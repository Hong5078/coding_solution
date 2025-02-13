"""
https://leetcode.com/problems/valid-parentheses/description/
"""


def is_valid(s: str) -> bool:
    stack = []

    # Stack appending phase
    for i in s:
        if i == "{":
            stack.append('}')
        elif i == "[":
            stack.append(']')
        elif i == "(":
            stack.append(')')

        # Checking phase
        else:
            # If in checking phase, but empty stack, return False
            if not stack:
                return False
            # If not the same pair parentheses, return False
            elif i != stack.pop():
                return False
    # If stack not empty after loop, return False
    if stack:
        return False

    return True


if __name__ == "__main__":
    list_1 = '{{[}]}'
    print(is_valid(list_1))

    list_2 = '(('
    print(is_valid(list_2))

    list_3 = ']'
    print(is_valid(list_3))
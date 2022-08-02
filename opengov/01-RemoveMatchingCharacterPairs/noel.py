from typing import *


def is_pair(l: int, r: int) -> bool:
    if l == "A" and r == "B":
        return True
    if l == "B" and r == "A":
        return True
    if l == "C" and r == "D":
        return True
    if l == "D" and r == "C":
        return True


def solution(A: List[int]) -> str:
    stack = []
    cursor = len(A) - 1

    while cursor >= 0:
        b = A[cursor]
        if len(stack) > 0:
            a = stack[-1]
            if is_pair(b, a):
                stack.pop()
            else:
                stack.append(b)
        else:
            stack.append(b)
        cursor -= 1

    stack.reverse()
    return "".join(stack)


# D A B C


assert solution("") == ""

result = solution("A")

print(result)
assert result == "A"

assert solution("AB") == ""

result = solution("ABC")
assert result == "C"

result = solution("ABCD")
assert result == ""

result = solution("CBACD")
assert result == "C"

result = solution("CABABD")
assert result == ""

result = solution("ACBDACB")

print(result)
assert result == "ACBDACB"

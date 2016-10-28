def _reduced_string(s):
    if not s:
        return "Empty String"
    letters = list()
    counts = list()

    last = ""
    counts_index = -1
    for ch in s:
        if last != ch:
            letters.append(ch)
            counts.append(1)
            counts_index += 1
            last = ch
        else:
            counts[counts_index] += 1

    ans = list()
    for i, val in enumerate(counts):
        ans.append(val % 2 * letters[i])

    ans = "".join(ans)
    if not ans:
        ans = "Empty String"
    changed = s != ans
    return ans, changed


def reduced_string(s):
    ans, changed = _reduced_string(s)
    while changed:
        ans, changed = _reduced_string(ans)
    return ans


def test_solution1():
    s = "aaabccddd"
    ans = "abd"

    assert ans == reduced_string(s)


def test_solution2():
    s = "baab"
    ans = "Empty String"

    assert ans == reduced_string(s)


def test_solution3():
    s = "aabbccdd"
    ans = "Empty String"

    assert ans == reduced_string(s)

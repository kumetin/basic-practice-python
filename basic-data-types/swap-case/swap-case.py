def swap_case(s):
    swapped: str = ''
    for c in s:
        if c.isupper():
            swapped += c.lower()
        elif c.islower():
            swapped += c.upper()
        else:
            swapped += c
    return swapped

if __name__ == '__main__':
    s = input()
    print(swap_case(s))
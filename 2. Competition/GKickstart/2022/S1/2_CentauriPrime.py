def get_ruler(kingdom):
    ruler = ''
    A = "AEIOUaeiou"
    N = "Yy"

    if kingdom[-1] in A:
        ruler = "Alice"
    elif kingdom[-1] in N:
        ruler = "nobody"
    else:
        ruler = "Bob"
        
    return ruler

def main():
    # Get the number of test cases
    T = int(input())
    for t in range(T):
        # Get the kingdom
        kingdom = input()
        print('Case #%d: %s is ruled by %s.' % (t + 1, kingdom, get_ruler(kingdom)))

if __name__ == '__main__':
    main()

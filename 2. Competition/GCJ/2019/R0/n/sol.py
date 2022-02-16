import sys

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    T = int(f.readline())
    for _T in xrange(T):
        N, B, F = map(int, f.readline().split())

        responses = []

        for round in range(4):
            msg = []
            for i in xrange(N):
                msg.append(chr(ord('0') + ((i & (1 << round)) >> round)))
            msg = ''.join(msg)
            print msg
            sys.stdout.flush()
            responses.append(f.readline().strip())

        prev = -1
        missed = []
        for i in xrange(N - B):
            idx = 0
            for round in range(4):
                idx += (ord(responses[round][i]) - ord('0')) << round

            while idx != (prev + 1) % 16:
                prev += 1
                missed.append(prev)
            prev += 1
        while N % 16 != (prev + 1) % 16:
            prev += 1
            missed.append(prev)

        print ' '.join(map(str, missed))
        sys.stdout.flush()
        f.readline()
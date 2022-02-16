import bisect

def h_index(n, citations):
    ans = []
    maxH = 0
    sArr = []

    for i, c in enumerate(citations):
        bisect.insort(sArr, c)

        for j in range(maxH, i + 1):
            if sArr[len(sArr) - j - 1] >= j + 1:
                maxH = j + 1
            else:
                break

        ans.append(maxH)
    return ans


if __name__ == '__main__':
    t = int(input())

    for test_case in range(1, t + 1):
        n = int(input())                      # The number of papers
        # The number of citations for each paper
        citations = map(int, input().split())
        h_index_scores = h_index(n, citations)
        print("Case #" + str(test_case) + ": " +
              ' '.join(map(str, h_index_scores)))

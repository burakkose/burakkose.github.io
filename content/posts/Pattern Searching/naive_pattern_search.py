def search(text, pattern):
    m, n = len(pattern), len(text)
    for i in range(n - m + 1):
        for j in range(m):
            if text[i + j] != pattern[j]:
                break
        if j + 1 == m:
            print(i)

if __name__ == '__main__':
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"
    search(txt, pat)

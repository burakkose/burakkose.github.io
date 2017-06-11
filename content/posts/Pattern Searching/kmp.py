def KMP_search(text, pattern):
    lps = compute_lps_array(pattern)
    m, n, j = len(pattern), len(text), 0
    i = 0  # text indeksi
    while i < n:
        if pattern[j] == text[i]:
            i, j = i + 1, j + 1
        if j == m:
            print(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            # j eşleşme sonrası eşleşmeme
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def compute_lps_array(pattern):
    lps = [0] * len(pattern)
    # len_sp = son en uzun prefix suffix uzunluğu
    len_sp, i, len_pattern = 0, 1, len(pattern)

    while i < len_pattern:
        if pattern[i] == pattern[len_sp]:
            len_sp += 1
            lps[i] = len_sp
            i += 1
        elif len_sp != 0:
            len_sp = lps[len_sp - 1]
        else:  # len_sp == 0
            lps[i] = 0
            i += 1

    return lps

if __name__ == '__main__':
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    KMP_search(text, pattern)

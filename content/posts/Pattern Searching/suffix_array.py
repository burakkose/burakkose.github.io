def build_suffix_array(text):
    return sorted(range(len(text)), key=lambda x: text[x:])


def search(text, pattern, suffs, l, r):
    if r < l:
        return -1

    mid = l + (r - l) // 2
    t = text[suffs[mid]:][:len(pattern)]

    if pattern == t:
        return suffs[mid]
    elif pattern > t:
        return search(text, pattern, suffs, mid + 1, r)
    else:
        return search(text, pattern, suffs, l, mid - 1)

if __name__ == '__main__':
    text = "banana"
    pattern = "anan"
    suffix_array = build_suffix_array(text)
    print(search(text, pattern, suffix_array, 0, len(text) - 1))

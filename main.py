def kmp_search(text, pat):
    lps = [0]*len(pat); j = 0
    for i in range(1, len(pat)):
        while j > 0 and pat[i] != pat[j]: j = lps[j-1]
        if pat[i] == pat[j]: j += 1; lps[i] = j
    hits, j = [], 0
    for i, ch in enumerate(text):
        while j > 0 and ch != pat[j]: j = lps[j-1]
        if ch == pat[j]: j += 1
        if j == len(pat): hits.append(i - len(pat) + 1); j = lps[j-1]
    return hits

if __name__ == "__main__":
    assert kmp_search("ababcabcabababd", "ababd") == [10]
    print("[PASS] 054_kmp_string_matcher")

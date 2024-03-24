def generate_anagrams(s):
    if len(s) <= 1:
        return [s]
    
    anagrams = []
    for i in range(len(s)):
        for perm in generate_anagrams(s[:i] + s[i+1:]):
            anagrams.append(s[i] + perm)
    
    return anagrams

# 예시 사용법
s = "abc"  # 예시 입력
anagrams = generate_anagrams(s)
print(anagrams)


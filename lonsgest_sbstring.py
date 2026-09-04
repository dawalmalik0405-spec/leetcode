c = "abcabcbb"

def lengthOfLongestSubstring(s):
    left = 0
    seen = set()
    max_length = 0

    for right in range(len(s)):
        current = s[right]

        while current in seen:
            seen.remove(s[left])
            left += 1

        seen.add(current)

        max_length = max(max_length, right - left + 1)

    return max_length


print(lengthOfLongestSubstring(c))
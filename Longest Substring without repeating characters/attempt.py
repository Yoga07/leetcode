def lengthOfLongestSubstring(s: str) -> int:
    seen = set()
    
    for idx in range(len(s)):
        char = s[idx]
        
        if char in seen:
            seen.clear()
        
        seen.add(char)
        print(f"Added {char} now:", seen)
                
    return len(seen)

lengthOfLongestSubstring("abcabcbb")
lengthOfLongestSubstring("bbbbb")
lengthOfLongestSubstring("pwwkew")

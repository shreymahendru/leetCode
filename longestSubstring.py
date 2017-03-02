def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        approach sliding windows
        """
        max_string = ""
        sub_string = ""
        start_index = 0
        end_index = 0
        char_set = set()
        while start_index < len(s) and end_index < len(s):
            if s[end_index] not in char_set:
                char_set.add(s[end_index])
                end_index = end_index +1
            else:
                char_set.remove(s[start_index])
                start_index = start_index + 1
            sub_string = s[start_index:end_index]
            if len(max_string) < len(sub_string):
                max_string = sub_string

        return max_string

print lengthOfLongestSubstring("aabcaeras")
print lengthOfLongestSubstring("abcabcbb")
print lengthOfLongestSubstring("bbbbb")
print lengthOfLongestSubstring("pwwkew")

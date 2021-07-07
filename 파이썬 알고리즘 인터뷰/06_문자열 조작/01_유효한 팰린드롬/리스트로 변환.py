# 리스트로 변환 (125. Valid Palindrome)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():  # isalnum(): 영문자, 숫자 여부를 판별하는 함수
                strs.append(char.lower())   # 영문자는 소문자로 변환해서 append

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop(-1):
                return False

        return True
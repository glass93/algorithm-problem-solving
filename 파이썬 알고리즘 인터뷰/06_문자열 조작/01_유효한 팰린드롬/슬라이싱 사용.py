# 슬라이싱 사용 (125. Valid Palindrome)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        S = s.lower()
        # 정규식으로 불필요한 문자 필터링
        # [^a-z0-9] a부터 z, 0부터 9를 제외한 문자만 매치
        S = re.sub('[^a-z0-9]', '', S)

        return S == S[::-1] # 슬라이싱
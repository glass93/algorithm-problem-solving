# 파이썬다운 방식 (344. Reverse String)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        # s[:] = s[::-1]
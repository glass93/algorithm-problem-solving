# 데크 자료형을 이용한 최적화 (125. Valid Palindrome)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 자료형 데크로 선언
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True

# 리스트로 변환.py에 비해서 풀이 속도가 5배 가까이 빠르다.
# 리스트의 pop(0)이 O(n)인 데 반해, 데크의 popleft()는 O(1)이기 때문이다.
# 각각 n번씩 반복하면, 리스트 구현은 O(n^2), 데크 구현은 O(n)으로 성능 차이가 크다.


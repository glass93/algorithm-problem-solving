# 람다와 +연산자를 이용 (937. Reorder Log Files)
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []

        # 문자로 구성된 로그와, 숫자로 구성된 로그를 나눈다.
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # 2개의 키를 람다 표현식으로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + digits
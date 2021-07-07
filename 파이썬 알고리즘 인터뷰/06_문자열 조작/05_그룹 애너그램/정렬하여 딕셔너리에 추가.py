# 정렬하여 딕셔너리에 추가 (49. Group Anagrams)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return anagrams.values()

# a = ['cde', 'cfc', 'abc']
#
# def fn(s):
#     return s[0], s[-1]
#
# print(sorted(a, key=fn))
# print(sorted(a, key=lambda s: (s[0], s[-1])))
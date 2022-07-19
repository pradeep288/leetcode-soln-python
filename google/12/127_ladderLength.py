import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)

        visit = set()
        q = [beginWord]
        res = 1
        while q:
            for i in range(len(q)):
                word = q.pop(0)
                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for nei_word in nei[pattern]:
                        if nei_word not in visit:
                            visit.add(nei_word)
                            q.append(nei_word)
            res+=1

        return 0

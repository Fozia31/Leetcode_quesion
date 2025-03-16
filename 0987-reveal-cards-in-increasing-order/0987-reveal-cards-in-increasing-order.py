class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        res = [0] * len(deck)
        que = deque(range(len(deck)))
        for n in deck:
            j = que.popleft()
            res[j] = n
            if que:
                que.append(que.popleft())

        return res
        
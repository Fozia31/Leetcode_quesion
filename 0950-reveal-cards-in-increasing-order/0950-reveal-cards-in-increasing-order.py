class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        queue = deque(range(len(deck)))
        res = [0]*len(deck)
        deck.sort()
        
        for card in deck:
            cur_card = queue.popleft()
            res[cur_card] = card

            if queue:
                cur_index = queue.popleft()
                queue.append(cur_index)

        return res
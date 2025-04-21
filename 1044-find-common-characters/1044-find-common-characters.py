class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        Count = Counter(words[0])

        for word in words[1:]:
            tmp_count = Counter(word)
            
            for key , value in Count.items():
                Count[key] = min(value , tmp_count[key])

        answer = []
        for key , value in Count.items():
            for _ in range(value):
                answer.append(key)
        
        return answer



            
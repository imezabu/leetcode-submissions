class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for word in strs:
            letter_vector = [0]*26
            for i in range(len(word)):
                val = ord(word[i].lower())-ord("a")
                letter_vector[val]+=1
            key=tuple(letter_vector)
            
            result[key].append(word)
        return list(result.values())

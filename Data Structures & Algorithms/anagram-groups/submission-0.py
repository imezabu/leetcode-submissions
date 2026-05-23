class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result={}
        for word in strs:
            letter_vector = [0]*26
            for i in range(len(word)):
                val = ord(word[i].lower())-ord("a")
                letter_vector[val]+=1
            key=tuple(letter_vector)
            if key not in result:
                result[key]=[]
            result[key].append(word)
        return list(result.values())

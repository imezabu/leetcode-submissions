class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs is None:
            return ""
        
        result= "".join(f"{len(w)}#{w}"for w in strs)
        return result
        
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1

            length = int(s[i:j])
            wordstart=j+1
            wordend=wordstart+length
            res.append(s[wordstart:wordend])
            i=wordend
        return res

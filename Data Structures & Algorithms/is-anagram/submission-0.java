class Solution {
    public boolean isAnagram(String s, String t) {
        if(s== null || t==null || s.length()!=t.length()){
            return false;
        }
        int[] buffer = new int[26];
        for(int k = 0; k< s.length(); k++){
            buffer[s.charAt(k)%26]++;
        }
        int[] buffer2 =  new int[26];
        for(int k = 0; k< t.length(); k++){
            buffer2[t.charAt(k)%26]++;
        }

        for(int k = 0; k< buffer.length; k++){
            if(buffer[k]!=buffer2[k]){
                return false;
            }
        }
        return true;
    }
}

    class Solution {
        private class Hash{
            int data;
            public Hash(int val){
                this.data=val;
            }
        }
        public boolean hasDuplicate(int[] nums) {
            Hash[] Hash = new Hash[2*nums.length];
            for(int k=0;k<nums.length; k++){
                int probeResult= insert(Hash, nums[k]);
                if (probeResult==-1){
                    System.err.println("Hashing algorithm critical failure");
                }
                if(probeResult==1){
                    return true;
                }
            }
            return false;
        }
        private int insert(Hash[] Hash, int key){
            //calculate hash step values for double hashing
            int m= Hash.length;
            int h1 =(key%m+m)%m;
            int h2=  1+((key%(m-1)+(m-1))%(m-1));
            //loop through table using hash steps to find value
            for(int i =0; i<m; i++){
                int index= (h1+i*h2)%m;
                //if hash index is not empty
                if(Hash[index]!=null){
                    //check if it is a repeat
                    if(Hash[index].data==key){
                        return 1;
                    }
                }
                //if hash is unique, then create new value
                else{
                    Hash[index]= new Hash(key);
                    return 0;
                }
            }
            //error checking in case table is too small;
            return -1;

        }
        
    }

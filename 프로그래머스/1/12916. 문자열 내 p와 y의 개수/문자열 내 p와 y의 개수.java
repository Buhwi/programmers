class Solution {
    boolean solution(String s) {
        s = s.toLowerCase();
        int num = 0;
        for(String temp : s.split("")) {
            if(temp.equals("p"))
                num++;
            if(temp.equals("y"))
                num--;
        }
        if(num == 0)
            return true;
        else
            return false;
    }
}
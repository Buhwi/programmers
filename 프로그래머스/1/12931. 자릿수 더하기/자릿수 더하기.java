import java.util.*;

public class Solution {
    public int solution(int n) {
        String num = Integer.toString(n);
        int answer = 0;
        for(String temp : num.split(""))
            answer += temp.charAt(0) - '0';
        return answer;
    }
}
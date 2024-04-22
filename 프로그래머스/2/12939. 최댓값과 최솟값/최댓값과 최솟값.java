class Solution {
    public String solution(String s) {
        String array[] = s.split(" ");
        int max = Integer.parseInt(array[0]);
        int min = Integer.parseInt(array[0]);
        
        for(int i = 0; i < array.length; i++){
            int temp = Integer.parseInt(array[i]);
            if(temp > max)
                max = temp;
            if(temp < min)
                min = temp;
        }
        return (Integer.toString(min) + " " + Integer.toString(max));
    }
}
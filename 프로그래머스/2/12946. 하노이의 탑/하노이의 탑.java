class Solution {
    int[][] answer;
    int m = 0;
    
    public int[][] solution(int n) {
        answer = new int[fux(n)][2];
        int A = 1;
        int B = 2;
        int C = 3;
        hanoi(n, A, C, B);
        
        return answer;
    }
    public void move(int n, int start, int end) {
        answer[m][0] = start;
        answer[m][1] = end;
        m++;
    }
    
    public void hanoi(int n, int A, int B, int C) {
        if(n == 1)
            move(n, A, B);
        else {
            hanoi(n-1, A, C, B);
            move(n, A, B);
            hanoi(n-1, C, B, A);
        }
    }
    
    public int fux(int m){
        int r = 1;
        for(int i = 0; i < m; i++){
            r *= 2;
        }
        return r - 1;
    }
}
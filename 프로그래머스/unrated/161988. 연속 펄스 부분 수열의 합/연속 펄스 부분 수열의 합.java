class Solution {
    public long solution(int[] sequence) {
        long answer = 0;
        int N = sequence.length;
        long[] sum = new long[N+1];
        long min = 0l;
        long max = 0l;
        
        
        for (int i=0;i<N;i++){
            if (i%2==0) sum[i+1] = sum[i] + sequence[i];
            else sum[i+1] = sum[i] - sequence[i];
            max = Math.max(max,sum[i+1]);
            min = Math.min(min,sum[i+1]);
        }
        return max-min;
    }
}
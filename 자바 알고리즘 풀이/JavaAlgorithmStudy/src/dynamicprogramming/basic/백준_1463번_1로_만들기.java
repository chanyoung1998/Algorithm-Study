package dynamicprogramming.basic;

import java.io.*;
import java.util.Arrays;

public class 백준_1463번_1로_만들기 {

    static int[] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        dp = new int[n+1];
        Arrays.fill(dp,-1);
        dp[1] = 0;
        for(int i = 2 ; i <= n ; i ++){
            dp[i] = dp[i-1] + 1;
            if( i % 2  == 0){
                dp[i] = Math.min(dp[i],dp[i/2] + 1);
            }
            if( i % 3 == 0){
                dp[i] = Math.min(dp[i],dp[i/3] + 1);
            }
        }

        f(n);

        bw.write(String.valueOf(dp[n]));

        br.close();
        bw.close();


    }


    private static int f(int n) {

        if (n == 1) return 0;
        if (dp[n] != -1) return dp[n];

        int result = f(n-1) + 1;
        if(n % 2 == 0){
            result = Math.min(result, f(n / 2) + 1);
        }
        if(n % 3 == 0){
            result = Math.min(result, f(n / 3) + 1);
        }
        dp[n] =result;
        return result;
    }


}

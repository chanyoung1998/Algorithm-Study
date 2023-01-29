package dynamicprogramming.basic;

import java.io.*;
import java.util.Arrays;
import java.util.stream.Stream;

public class 백준_1912번_연속합 {

    static Integer[] arr;
    static int[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        dp = new int[n];

        String line[] = br.readLine().split(" ");
        arr = Stream.of(line).mapToInt(Integer::parseInt).boxed().toArray(Integer[]::new);

        dp[0] = Integer.parseInt(line[0]); // 기저 사건

        for(int i = 1; i < n; i++){
            dp[i] = (dp[i - 1] + arr[i]) > arr[i] ? dp[i - 1] + arr[i] : arr[i];
        }

        bw.write(String.valueOf(Arrays.stream(dp).max().getAsInt()));

        br.close();
        bw.flush();

    }

}

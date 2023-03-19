public class Fibonacci{

    public static int[] count = new int[100];

    public static void main(String args[]) {
        int n = 10;

        System.out.println(fibonacci(n));

        int i = 0;
        for (int c : count) {
            if(i > n ) break;
            System.out.println("F("+i+++")"+"메소드 실행횟수:" + c);

        }
    }

    public static int fibonacci(int n) {
        count[n]++;
        if (n < 2) {
            return n;
        }
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}
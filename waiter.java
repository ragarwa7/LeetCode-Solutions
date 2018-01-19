import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int q = in.nextInt();
        int[] number = new int[n];
        for (int number_i = 0; number_i < n; number_i++) {
            number[number_i] = in.nextInt();
        }
        waiter(number, q);
    }

    private static void waiter(int[] number, int q) {
        List<Stack<Integer>> b_s = new ArrayList<>();
        Stack<Integer> temp_a = new Stack<>();
        Stack<Integer> temp_a1;
        Stack<Integer> temp_b;
        for (int i : number) {
            temp_a.push((Integer) i);
        }
        for (int i = 1; i <= q; i++) {
            int x = nthPrime(i);
            temp_a1 = new Stack<>();
            temp_b = new Stack<>();
            while (!temp_a.empty()) {
                Integer a = temp_a.pop();
                if (a % x == 0) {
                    temp_b.push(a);
                } else {
                    temp_a1.push(a);
                }
            }
            temp_a = temp_a1;
            b_s.add(temp_b);
        }
        b_s.add(temp_a);
        printB(b_s);
    }

    private static void printB(List<Stack<Integer>> b_s) {
        for (Stack<Integer> b : b_s) {
            while (!b.empty()) {
                System.out.println(b.pop());
            }
        }

    }

    private static int nthPrime(int n) {
        int candidate, count;
        for (candidate = 2, count = 0; count < n; ++candidate) {
            if (isPrime(candidate)) {
                ++count;
            }
        }
        return candidate - 1;
    }

    private static boolean isPrime(int num) {
        boolean isPrime = true;
        int temp;
        for (int i = 2; i <= num / 2; i++) {
            temp = num % i;
            if (temp == 0) {
                isPrime = false;
                break;
            }
        }
        return isPrime;
    }
}

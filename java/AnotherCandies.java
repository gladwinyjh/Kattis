import java.io.*;
import java.util.*;


public class AnotherCandies {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();
            long count = 0;

            for (int j = 0; j < n; j++) {
                count += sc.nextLong() % n; //Number of heaps
            }

            //Can each child get a heap?
            System.out.println(count % n == 0 ? "YES": "NO"); 
        }

    }
}
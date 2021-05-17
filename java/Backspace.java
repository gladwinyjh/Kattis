import java.io.*;
import java.util.*;


public class Backspace {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringBuilder sb = new StringBuilder();
 
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) != '<') {
                sb.append(str.charAt(i)); 
            }
            else if (i > 0) {
                sb.deleteCharAt(sb.length() - 1);
            }
        }

        System.out.print(sb.toString());
        
    }
}

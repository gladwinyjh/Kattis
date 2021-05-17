import java.io.*;
import java.util.*;


public class Zyxab {

    public static boolean checkRepeated(String str) {

        for (int i = 0; i < str.length(); i++) {
            for (int j = i+1; j < str.length(); j++) {
                if (str.charAt(i) == str.charAt(j)) {
                    return true; //Returns true is there are repeated characters in string
                }
            }
        }
        return false; 
    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        HashMap<String, Boolean> map = new HashMap<>();
        
        for (int i = 0; i < n; i++) {
            String name = sc.nextLine();

            map.put(name,checkRepeated(name));
        }

        
        if (map.containsKey("zyxab")) { //zyxab is one of the names
            System.out.println("zyxab");
        }
        else { 
            String best_name = "";
            int shortest = 21;

            for (String name : map.keySet()) {
                if ((map.get(name) == false) && (name.length() >= 5)) { //non-repeating, at least length 5
                    if (name.length() < shortest) { 
                        shortest = name.length();
                        best_name = name;
                    }
                    else if ((name.length() == shortest) && (name.compareTo(best_name) > 0)) { 
                        //Same length as shortest, but alphabetically larger than current best name
                        best_name = name;
                    }
                }
            }
            if (best_name.equals("")) { //No valid names
                System.out.println("neibb!");
            }
            else {
                System.out.println(best_name);
            }
        }
    }
}

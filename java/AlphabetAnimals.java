import java.io.*;
import java.util.*;


public class AlphabetAnimals {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String prev = sc.nextLine();

        Character c = prev.charAt(prev.length() - 1);

        int n = sc.nextInt();
        sc.nextLine();

        ArrayList<String> list = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            list.add(sc.nextLine());
        }

        boolean first = false;
        String firstName = " ";

        for (String name : list) {
            if (c == name.charAt(0)) { //Name found
                if (!first) {
                    first = true;
                    firstName = name; // Store first name
                }

                Character d = name.charAt(name.length()-1);

                boolean next = false;
                for (String name1: list) {//Traverse list again
                    if (d == name1.charAt(0) && name1 != name) { //Next person will have a valid name
                        next = true;
                        break;
                    }
                }
                
                if (!next) { //At least one name has been found and next person will have a valid name
                    System.out.println(name + "!");
                    System.exit(0); //terminate
                }
            }
        }
        if (first) { //If it reaches here, it means that next person will have a name
            System.out.println(firstName);
            System.exit(0); //terminate
        }
        else {
            System.out.println("?"); // No valid name found for you after going through all names:(
        }

    }
}
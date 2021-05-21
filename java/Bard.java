import java.io.*;
import java.util.*;

public class Bard {
    
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int e = sc.nextInt();
        sc.nextLine();

        HashMap<Integer, HashMap<Integer, Integer>> map = new HashMap<>();

        for (int i = 1; i < n+1; i++) {
            map.put(i,new HashMap<>());
        }

        int bardSongs = 0;

        for (int i = 0; i < e; i++) {
            String [] str = sc.nextLine().split(" ");
            Integer [] arr = new Integer[str.length-1];
            boolean bard = false;

            for (int j = 1; j < str.length; j++) {
                arr[j-1] = Integer.parseInt(str[j]);
            }

            List<Integer> intList = new ArrayList<>(Arrays.asList(arr));
            if (intList.contains(1)) {
                bard = true;
                bardSongs += 1;
            }

            if (bard) {
                for (int j = 0; j < arr.length; j++) {
                    map.get(arr[j]).put(bardSongs, 1);
                }
            }
            else {
                HashMap<Integer, Integer> map1 = new HashMap<>();
                
                for (int j = 0; j < arr.length; j++) {
                    map1.putAll(map.get(arr[j])); //Union sets, or get all the unique songs
                }

                for (int j = 0; j < arr.length; j++) {
                    map.get(arr[j]).putAll(map1);
                }
            }
        }

        for (int i = 1; i <= map.size(); i++) {

            //Songs only can originate from bard, so bard knows all the songs
            //If villager knows as many songs as bard, villager knows all the songs
            if (map.get(i).size() == map.get(1).size()) { 
                System.out.println(i);
            }
        }
    }
}

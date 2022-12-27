import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

class Result {

    /*
     * Complete the 'insertionSort1' function below.
     *
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. INTEGER_ARRAY arr
     */

    public static void insertionSort1(int n, List<Integer> arr) {
 
       boolean sorted=false;

        while(!sorted){
          for(int i=n-1;i>0;i--){
            int current=arr.get(i);
            int prev=arr.get(i-1);

            if(current<prev){
                arr.set(i,prev);
            
                for (Integer e : arr) {
            
            System.out.print(e);
            
            System.out.print(" ");
        }
        System.out.println();
                arr.set(i-1,current);
            }
            if(i==1){
                sorted=true;
            }
          }

        for (Integer e : arr) {
            
            System.out.print(e);
            
            System.out.print(" ");
        }
        System.out.println();
        }
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        String[] arrTemp = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        List<Integer> arr = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int arrItem = Integer.parseInt(arrTemp[i]);
            arr.add(arrItem);
        }

        Result.insertionSort1(n, arr);

        bufferedReader.close();
    }
}

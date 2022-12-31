import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

class Result {

    /*
     * Complete the 'countSwaps' function below.
     *
     * The function accepts INTEGER_ARRAY a as parameter.
     */

    public static void countSwaps(List<Integer> a) {
    // Write your code here
        int count=0;
for(int i=0;i<a.size()-1;i++){
 
    for(int j=a.size()-1;j>i;--j){
       
        if(a.get(j)<a.get(j-1)){
            int temp=a.get(j-1);
            a.set(j-1,a.get(j));
            a.set(j,temp);
            count++;
        }
    }
}
System.out.println("Array is sorted in " +count+ " swaps.");
System.out.println("First Element: "+a.get(0));
System.out.println("Last Element: "+a.get(a.size()-1));
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        String[] aTemp = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        List<Integer> a = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int aItem = Integer.parseInt(aTemp[i]);
            a.add(aItem);
        }

        Result.countSwaps(a);

        bufferedReader.close();
    }
}

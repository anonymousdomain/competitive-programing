import java.util.List;

class Insertion {

    /*
     * Complete the 'insertionSort1' function below.
     *
     * The function accepts following parameters:
     * 1. INTEGER n
     * 2. INTEGER_ARRAY arr
     */

    public static void insertionSort1(int n, List<Integer> arr) {

        boolean sorted = false;

        while (!sorted) {
            for (int i = n - 1; i > 0; i--) {
                int current = arr.get(i);
                int prev = arr.get(i - 1);

                if (current < prev) {
                    arr.set(i, prev);

                    for (Integer e : arr) {

                        System.out.print(e);

                        System.out.print(" ");
                    }
                    System.out.println();
                    arr.set(i - 1, current);
                }
                if (i == 1) {
                    sorted = true;
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

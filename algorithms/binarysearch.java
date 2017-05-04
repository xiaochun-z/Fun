import java.util.Arrays;

/**
 * Created by caden on 2017/5/4.
 */
public class SearchMain {
    public static void main(String[] args) {
        int[] seq = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int result = search(seq, 5, 0, seq.length);
        System.out.println(result);
        result = search2(seq, 5, 0, seq.length);
        System.out.println(result);
        result = Arrays.binarySearch(seq,0,seq.length,5);
        System.out.println(result);
    }


    public static int search(int[] seq, int v, int low, int high) {
        while (low <= high) {
            int mid = (low + high) / 2;
            if (v == seq[mid]) {
                return mid;
            } else if (v > seq[mid]) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return Integer.MIN_VALUE;
    }

    public static int search2(int[] seq, int v, int low, int high) {
        if (low > high) {
            return Integer.MIN_VALUE;
        }
        int mid = (low + high) / 2;
        if (v == seq[mid]) {
            return mid;
        } else if (v > seq[mid]) {
            return search2(seq, v, mid + 1, high);
        } else {
            return search2(seq, v, low, mid - 1);
        }
    }
}


/**
 * Created by caden on 2017/5/9.
 */
public class mergeSort {
    public static void main(String[] args) {
        int[] seq = {1, 2, 3, 7, 5, 2, 3, 3, 1};
        sort(seq, 0, seq.length - 1);
        for (int i : seq) {
            System.out.println(i);
        }
    }

    public static void sort(int[] seq, int left, int right) {
        if (left < right) {
            int middle = (left + right) / 2;
            sort(seq, left, middle);
            sort(seq, middle + 1, right);
            merge(seq, left, right);
        }
    }

    public static void merge(int[] seq, int l, int r) {
        int mid = (l + r) / 2;
        int i = l;
        int j = mid + 1;
        int count = 0;
        int temp[] = new int[r - l + 1];
        while (i <= mid && j <= r) {
            if (seq[i] < seq[j]) {
                temp[count++] = seq[i++];
            } else {
                temp[count++] = seq[j++];
            }
        }
        while (i <= mid) {
            temp[count++] = seq[i++];
        }
        while (j <= r) {
            temp[count++] = seq[j++];
        }
        count = 0;
        while (l <= r) {
            seq[l++] = temp[count++];
        }
    }
}

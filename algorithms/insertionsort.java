public class Main {

    public static void main(String[] args) {
        int[] seq = {1, 2, 3, 7, 5, 2, 3, 3, 1};
        sort(seq);
        for (int i : seq) {
            System.out.println(i);
        }
    }

    public static void sort(int[] seq) {
        for (int i, j = 1; j < seq.length; j++) {
            int key = seq[j];
            i = j - 1;
            while (i > 0 && seq[i] > key) {
                seq[i + 1] = seq[i];
                i = i - 1;
            }
            seq[i + 1] = key;
        }
    }
}

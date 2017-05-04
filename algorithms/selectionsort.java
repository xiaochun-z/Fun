public class SelectionSort
{
  public static void main(String[] args) {
   int[] seq = {1, 2, 3, 7, 5, 2, 3, 3, 1};
   sort(seq);
   for (int i : seq) {
     System.out.println(i);
   }
 } 

 public static int[] sort(int[] seq)
 {
   int n = seq.length;
   for(int j = 0; j < n - 1; j++){
     int smallest = j;
     for(int i = j + 1; i < n; i++){
       if(seq[i] < seq[smallest]){
         smallest = i;
       }
       if(smallest !=j) {
         int temp = seq[smallest];
         seq[smallest] = seq[j];
         seq[j] = temp;
       }
     }
   }
   return seq;
 }
}

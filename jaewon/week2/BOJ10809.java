import java.util.Arrays;
import java.util.Scanner;

public class BOJ10809 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String word = input.nextLine();
        
        int[] location = new int[26];
        Arrays.fill(location, -1);
        
        for (int i = 0; i < word.length(); i++) {
            int index = word.charAt(i) - 'a';
            if (location[index] == -1) {
                location[index] = i;
            }
        }
        
        for (int i = 0; i < location.length; i++) {
            System.out.print(location[i]);
            if (i < location.length - 1) {
                System.out.print(" ");
            }
        }
        System.out.println();
    }
}

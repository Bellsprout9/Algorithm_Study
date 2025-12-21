import java.util.Scanner;

public class BOJ2675 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int T = input.nextInt();
        
        for (int tc = 0; tc < T; tc++) {
            int R = input.nextInt();
            String S = input.next();
            
            for (char ch : S.toCharArray()) {
                for (int j = 0; j < R; j++) {
                    System.out.print(ch);
                }
            }
            System.out.println();
        }
    }
}

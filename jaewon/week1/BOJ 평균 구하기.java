import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    // 점수의 개수, 점수 배열 입력받기
    int num = sc.nextInt();
    int[] scores = new int[num];
    for (int i = 0; i < num; i++) {
      scores[i] = sc.nextInt();
    }

    // 점수의 최댓값 구하기
    int maxScore = scores[0];
    for (int i = 1; i < num; i++) {
      if (scores[i] > maxScore) {
        maxScore = scores[i];
      }
    }

    // 새로운 점수 합계 (형변환 필요)
    double sum = 0;
    for (int i = 0; i < num; i++) {
      sum += (double) scores[i] / maxScore * 100;
    }

    // 새로운 평균 출력
    System.out.println(sum / num);

    sc.close();
  }
}

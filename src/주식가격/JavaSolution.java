package 주식가격;

public class JavaSolution {
}

class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];

        for (int i = 0; i < prices.length; i++) {
            int hold = 0;
            for (int j = i+1; j < prices.length; j++) {
                hold++;
                if (prices[i] > prices[j]) {
                    break;
                }
            }
            answer[i] = hold;
        }

        return answer;
    }
}
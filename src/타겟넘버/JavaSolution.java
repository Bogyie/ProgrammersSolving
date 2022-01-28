package 타겟넘버;

import java.util.ArrayList;
import java.util.List;

public class JavaSolution {
        public int solution(int[] numbers, int target) {
            final List<ArrayList<Integer>> results =  new ArrayList<>() {{
                for (int i = 0; i <= numbers.length; i++) {
                    add(new ArrayList<>());
                }
            }};

            results.get(0).add(0);

            for (int index = 0; index < numbers.length; index++) {
                for (int beforeValue: results.get(index)) {
                    results.get(index + 1).add(beforeValue + numbers[index]);
                    results.get(index + 1).add(beforeValue - numbers[index]);
                }
            }

            int answer = 0;
            for (int result: results.get(results.size() - 1)) {
                if (result == target) {
                    answer++;
                }
            }

            return answer;
        }
    }
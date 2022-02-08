package 기능개발;

import java.util.ArrayList;

public class JavaSolution {
    protected int current_progress_num = 0;

    void work(int[] progresses, int[] speeds) {
        for (int i = 0; i < progresses.length; i++) {
            progresses[i] += speeds[i];
        }
    }

    int done(int[] progresses) {
        int done_progress_count = 0;

        while (progresses[current_progress_num] >= 100) {
            done_progress_count++;
            current_progress_num++;
            if (current_progress_num >= progresses.length) {
                break;
            }
        }
        return done_progress_count;
    }

    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> result = new ArrayList<>();
        int current_done_count;
        int done_progress_count = done(progresses);

        while (progresses.length > done_progress_count) {
            work(progresses, speeds);
            current_done_count = done(progresses);
            if (current_done_count > 0) {
                result.add(current_done_count);
                done_progress_count += current_done_count;

                if (done_progress_count >= progresses.length) {
                    break;
                }
            }
        }

        return result.stream().mapToInt(Integer::intValue).toArray();
    }
}
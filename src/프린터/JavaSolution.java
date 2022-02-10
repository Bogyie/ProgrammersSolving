package 프린터;

import java.util.*;


class Node {
    final int priority;
    final boolean isTarget;

    Node(int priority, boolean isTarget) {
        this.priority = priority;
        this.isTarget = isTarget;
    }
}


class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        Queue<Node> queue = new LinkedList<>() {{
            for (int i = 0; i < priorities.length; i++) {
                offer(new Node(priorities[i], i == location));
            }
        }};

        Arrays.sort(priorities);
        int index = priorities.length - 1;

        while (!queue.isEmpty()) {
            if (queue.peek().priority == priorities[index]) {
                if (queue.peek().isTarget) {
                    break;
                }
                queue.poll();
                index--;
                answer++;
            } else {
                queue.offer(queue.poll());
            }
        }

        return answer;
    }
}
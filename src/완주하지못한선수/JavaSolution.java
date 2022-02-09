package 완주하지못한선수;

import java.util.HashMap;
import java.util.Map;

public class JavaSolution {
    protected final HashMap<String, Integer> players = new HashMap<>();

    protected boolean isPlayer(String name) {
        return players.containsKey(name);
    }


    protected void start(String name) {
        if (isPlayer(name)) {
            players.replace(name, players.get(name) + 1);
        } else {
            players.put(name, 1);
        }
    }

    protected void finish(String name) {
        if (isPlayer(name)) {
            players.replace(name, players.get(name) - 1);
        }
    }

    public String solution(String[] participant, String[] completion) {
        String answer = "";

        for (String name: participant) {
            start(name);
        }

        for (String name: completion) {
            finish(name);
        }

        for (Map.Entry<String, Integer> player : players.entrySet()) {
            if (player.getValue() > 0) {
                answer = player.getKey();
                break;
            }
        }

        return answer;
    }
}
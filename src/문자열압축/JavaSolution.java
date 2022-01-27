package 문자열압축;

import java.util.ArrayList;
import java.util.Collections;


class JavaSolution {
    ArrayList<String> compressedStrings = new ArrayList<>();

    String StringCompress(String s, int length) {
        StringBuilder result = new StringBuilder();
        int compressCount = 1;
        int beginIndex = 0;
        int endIndex = length;
        String prev = "";
        String curr = s.substring(beginIndex, endIndex);

        while (endIndex + length <= s.length()) {
            beginIndex = endIndex;
            endIndex += length;

            prev = curr;
            curr = s.substring(beginIndex, endIndex);

            if (prev.equals(curr)) {
                compressCount++;
            } else {
                result.append(compressCount == 1 ? "" : compressCount);
                result.append(prev);
                compressCount = 1;
            }
        }

        if (compressCount > 1) {
            result.append(compressCount).append(prev);
            beginIndex += length;
        }

        result.append(s.substring(beginIndex));
        return result.toString();
    }

    public int solution(String s) {
        String currResult;
        ArrayList<Integer> compressedStringLengths = new ArrayList<>();

        for (int i = 1; i <= s.length(); i++) {
            currResult = StringCompress(s, i);
            compressedStrings.add(currResult);
            compressedStringLengths.add(currResult.length());
        }

        //System.out.println(compressedStrings);
        return Collections.min(compressedStringLengths);
    }
}
package 전화번호목록;


import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book);

        for (int i = 1; i < phone_book.length; i++) {
            if (startsWith(phone_book[i-1], phone_book[i])) {
                return false;
            }
        }
        return true;
    }

    protected boolean startsWith(String start, String other) {

        for (int i = 0; i < start.length(); i++) {
            if (start.charAt(i) != other.charAt(i)) {
                return false;
            }
        }
        return true;
    }
}
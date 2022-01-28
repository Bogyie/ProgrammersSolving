package 멀쩡한사각형;

import java.math.BigInteger;

public class JavaSolution {
    public long solution(int w, int h) {
        return (long) w * h - w - h + BigInteger.valueOf(w).gcd(BigInteger.valueOf(h)).longValue();
    }
}
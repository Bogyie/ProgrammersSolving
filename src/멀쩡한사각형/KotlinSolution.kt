package 멀쩡한사각형

import java.math.BigInteger as BigInt

class KotlinSolution {
    fun solution(w: Int, h: Int): Long {
        return w.toLong() * h - w - h + BigInt.valueOf(w.toLong()).gcd(BigInt.valueOf(h.toLong())).toLong()
    }
}
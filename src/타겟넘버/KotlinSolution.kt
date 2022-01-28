package 타겟넘버

import java.util.ArrayList

class KotlinSolution {
    fun solution(numbers: IntArray, target: Int): Int {
        val results: ArrayList<ArrayList<Int>> = object : ArrayList<ArrayList<Int>>() {
            init {
                for (i in 0..numbers.size) {
                    add(ArrayList())
                }
            }
        }
        results[0].add(0)
        for (index in numbers.indices) {
            for (beforeValue in results[index]) {
                results[index + 1].add(beforeValue + numbers[index])
                results[index + 1].add(beforeValue - numbers[index])
            }
        }
        var answer = 0
        for (result in results[results.size - 1]) {
            if (result == target) {
                answer++
            }
        }
        return answer
    }
}
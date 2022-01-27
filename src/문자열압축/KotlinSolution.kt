package 문자열압축

import java.util.*


internal class KotlinSolution {
    private var compressedStrings = ArrayList<String>()

    private fun stringCompress(s: String, length: Int): String {
        val result = StringBuilder()
        var compressCount = 1
        var beginIndex = 0
        var endIndex = length
        var prev = ""
        var curr = s.substring(beginIndex, endIndex)
        while (endIndex + length <= s.length) {
            beginIndex = endIndex
            endIndex += length
            prev = curr
            curr = s.substring(beginIndex, endIndex)
            if (prev == curr) {
                compressCount++
            } else {
                result.append(if (compressCount == 1) "" else compressCount)
                result.append(prev)
                compressCount = 1
            }
        }
        if (compressCount > 1) {
            result.append(compressCount.toString() + prev)
            beginIndex += length
        }
        result.append(s.substring(beginIndex))
        return result.toString()
    }

    fun solution(s: String): Int {
        var currResult: String
        val compressedStringLengths = ArrayList<Int>()
        for (i in 1..s.length) {
            currResult = stringCompress(s, i)
            compressedStrings.add(currResult)
            compressedStringLengths.add(currResult.length)
        }

        //System.out.println(compressedStrings);
        return Collections.min(compressedStringLengths)
    }
}
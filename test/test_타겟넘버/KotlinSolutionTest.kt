package test_타겟넘버

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource
import 타겟넘버.KotlinSolution
import java.util.stream.Stream


@TestInstance(TestInstance.Lifecycle.PER_CLASS)
internal class KotlinSolutionTest {

    @ParameterizedTest
    @MethodSource("defaultTestCase")
    fun solution(numbers: IntArray, target: Int, result: Int) {
        val javaSolution = KotlinSolution()
        assertEquals(javaSolution.solution(numbers, target), result)
    }

    private fun defaultTestCase(): Stream<Arguments?>? {
        return Stream.of(
            Arguments.of(intArrayOf(1, 1, 1, 1, 1), 3, 5),
            Arguments.of(intArrayOf(4, 1, 2, 1), 4, 2)
        )
    }
}
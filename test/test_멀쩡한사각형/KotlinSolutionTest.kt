package test_멀쩡한사각형

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource
import 멀쩡한사각형.KotlinSolution
import java.util.stream.Stream


@TestInstance(TestInstance.Lifecycle.PER_CLASS)
internal class KotlinSolutionTest {

    @ParameterizedTest
    @MethodSource("defaultTestCase")
    fun solution(W: Int, H: Int, result: Int) {
        val javaSolution = KotlinSolution()
        assertEquals(javaSolution.solution(W, H), result)
    }

    private fun defaultTestCase(): Stream<Arguments?>? {
        return Stream.of(
            Arguments.of(8, 12, 80)
        )
    }
}
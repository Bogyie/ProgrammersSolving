package TestTemplate

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource
import SolutionTemplate.KotlinSolution
import java.util.stream.Stream


@TestInstance(TestInstance.Lifecycle.PER_CLASS)
internal class KotlinSolutionTest {

    @ParameterizedTest
    @MethodSource("defaultTestCase")
    fun solution(s: String?, result: Int) {
        val javaSolution = KotlinSolution()
        assertEquals(javaSolution.solution(), 7)
    }

    private fun defaultTestCase(): Stream<Arguments?>? {
        return Stream.of(
            Arguments.of("aabbaccc", 7)
        )
    }
}
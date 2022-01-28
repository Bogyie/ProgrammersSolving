package test_오픈채팅방

import org.junit.jupiter.api.Assertions.assertArrayEquals
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.TestInstance
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource
import 오픈채팅방.KotlinSolution
import java.util.stream.Stream


@TestInstance(TestInstance.Lifecycle.PER_CLASS)
internal class KotlinSolutionTest {

    @ParameterizedTest
    @MethodSource("defaultTestCase")
    fun solution(record: Array<String>, result: Array<String>) {
        val javaSolution = KotlinSolution()
        assertArrayEquals(javaSolution.solution(record), result)
    }

    private fun defaultTestCase(): Stream<Arguments?>? {
        return Stream.of(
            Arguments.of(
                arrayOf("Enter uid1234 Muzi",
                        "Enter uid4567 Prodo",
                        "Leave uid1234",
                        "Enter uid1234 Prodo",
                        "Change uid4567 Ryan"),

                arrayOf("Prodo님이 들어왔습니다.",
                        "Ryan님이 들어왔습니다.",
                        "Prodo님이 나갔습니다.",
                        "Prodo님이 들어왔습니다.")
            )
        )
    }
}
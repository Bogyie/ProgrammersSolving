package test_문자열압축;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;
import 문자열압축.JavaSolution;

import java.util.stream.Stream;
import static org.junit.jupiter.api.Assertions.*;

class JavaSolutionTest {

    @ParameterizedTest
    @MethodSource("defaultTestCase")
    void solution(String s, int result) {
        JavaSolution javaSolution = new JavaSolution();
        assertEquals(javaSolution.solution("aabbaccc"), 7);
    }

    private static Stream<Arguments> defaultTestCase() {
        return Stream.of(
                Arguments.of("aabbaccc", 7),
                Arguments.of("ababcdcdababcdcd", 9),
                Arguments.of("abcabcdede", 8),
                Arguments.of("abcabcabcabcdededededede", 14),
                Arguments.of("xababcdcdababcdcd", 17)
        );
    }

}
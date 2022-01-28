package TestTemplate;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;
import SolutionTemplate.JavaSolution;

import java.util.stream.Stream;

class JavaSolutionTest {

    @ParameterizedTest
    @MethodSource("defaultTestCase")
    void solution(String s, int result) {
        JavaSolution javaSolution = new JavaSolution();
        assertEquals(javaSolution.solution(), 7);
    }

    private static Stream<Arguments> defaultTestCase() {
        return Stream.of(
                Arguments.of("aabbaccc", 7)
        );
    }

}
package test_기능개발;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;
import 기능개발.JavaSolution;

import java.util.stream.Stream;


class JavaSolutionTest {

    @ParameterizedTest
    @MethodSource("defaultTestCase")
    void solution(int[] progresses, int[] speeds, int[] result) {
        JavaSolution javaSolution = new JavaSolution();
        assertArrayEquals(javaSolution.solution(progresses, speeds), result);
    }

    private static Stream<Arguments> defaultTestCase() {
        return Stream.of(
                Arguments.of(new int[]{93, 30, 55}, new int[]{1, 30, 5}, new int[]{2, 1}),
                Arguments.of(new int[]{95, 90, 99, 99, 80, 99}, new int[]{1, 1, 1, 1, 1, 1}, new int[]{1, 3, 2})
        );
    }

}
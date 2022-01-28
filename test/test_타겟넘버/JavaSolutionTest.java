package test_타겟넘버;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;
import 타겟넘버.JavaSolution;

import java.util.stream.Stream;


class JavaSolutionTest {

    @ParameterizedTest
    @MethodSource("defaultTestCase")
    void solution(int[] numbers, int target, int result) {
        JavaSolution javaSolution = new JavaSolution();
        assertEquals(javaSolution.solution(numbers, target), result);
    }

    private static Stream<Arguments> defaultTestCase() {
        return Stream.of(
                Arguments.of(new int[]{1, 1, 1, 1, 1}, 3, 5),
                Arguments.of(new int[]{4, 1, 2, 1}, 4, 2)
        );
    }

}
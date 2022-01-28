package test_멀쩡한사각형;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;
import 멀쩡한사각형.JavaSolution;

import java.util.stream.Stream;


class JavaSolutionTest {

    @ParameterizedTest
    @MethodSource("defaultTestCase")
    void solution(int W, int H, int result) {
        JavaSolution javaSolution = new JavaSolution();
        assertEquals(javaSolution.solution(W, H), result);
    }

    private static Stream<Arguments> defaultTestCase() {
        return Stream.of(
                Arguments.of(8, 12, 80)
        );
    }

}
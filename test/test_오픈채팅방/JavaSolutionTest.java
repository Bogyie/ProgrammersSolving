package test_오픈채팅방;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;
import 오픈채팅방.JavaSolution;

import java.util.stream.Stream;


class JavaSolutionTest {

    @ParameterizedTest
    @MethodSource("defaultTestCase")
    void solution(String[] record, String[] result) {
        JavaSolution javaSolution = new JavaSolution();
        assertArrayEquals(javaSolution.solution(record), result);
    }

    private static Stream<Arguments> defaultTestCase() {
        return Stream.of(
                Arguments.of(new String[]{"Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"},
                        new String[]{"Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."})
        );
    }

}
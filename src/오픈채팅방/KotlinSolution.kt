package 오픈채팅방

class KotlinSolution {
    fun solution(record: Array<String>): Array<String> {
        val answer = mutableListOf<Array<String>>()
        val nickname = hashMapOf<String, String>()

        for (chatLog in record.map { it.split(" ") }) {
            when {
                chatLog[0] == "Enter" -> {
                    answer.add(arrayOf(chatLog[1], "님이 들어왔습니다."))
                    nickname[chatLog[1]] = chatLog[2]
                }
                chatLog[0] == "Leave" -> {
                    answer.add(arrayOf(chatLog[1], "님이 나갔습니다."))
                }
                chatLog[0] == "Change" -> {
                    nickname[chatLog[1]] = chatLog[2]
                }
            }
        }
        return answer.map { nickname[it[0]] + it[1] }.toTypedArray()
    }
}
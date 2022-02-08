from collections import defaultdict
from dataclasses import dataclass
from functools import singledispatchmethod


@dataclass
class Leave:
    user_id: str


@dataclass
class Enter(Leave):
    nickname: str


@dataclass
class Change(Enter):
    pass


@dataclass
class ChattingLogs:
    users = defaultdict(str)
    chat_log = []

    @singledispatchmethod
    def action(self, action):
        raise NotImplementedError

    @action.register
    def _(self, action: Enter):
        self.chat_log.append((action.user_id, "님이 들어왔습니다."))
        self.users[action.user_id] = action.nickname

    @action.register
    def _(self, action: Leave):
        self.chat_log.append((action.user_id, "님이 나갔습니다."))

    @action.register
    def _(self, action: Change):
        self.users[action.user_id] = action.nickname

    def __iter__(self):
        return map(lambda chat: self.users[chat[0]] + chat[1], self.chat_log)


def solution(record):
    chat = ChattingLogs()
    for action, *message in map(str.split, record):
        if action == "Enter":
            chat.action(Enter(user_id=message[0], nickname=message[1]))
            continue
        if action == "Leave":
            chat.action(Leave(user_id=message[0]))
            continue
        if action == "Change":
            chat.action(Change(user_id=message[0], nickname=message[1]))
            continue
    return list(chat.__iter__())

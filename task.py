def check_relation(net, first, second):
    all_know = {}
    for i in net:
        all_know.setdefault(i[0], []).append(i[1])
        all_know.setdefault(i[1], []).append(i[0])

    checked = []

    def recursion(friend_list):
        if second in friend_list:
            return True
        for fried in friend_list:
            if fried in checked:
                continue
            checked.append(fried)
            result = recursion(all_know.get(fried))
            if result:
                return True
            else:
                continue

    return recursion(all_know.get(first)) or False


if __name__ == '__main__':
    net = (
    ("Ваня", "Лёша"), ("Лёша", "Катя"),
    ("Ваня", "Катя"), ("Вова", "Катя"),
    ("Лёша", "Лена"), ("Оля", "Петя"),
    ("Стёпа", "Оля"), ("Оля", "Настя"),
    ("Настя", "Дима"), ("Дима", "Маша")
    )

    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True
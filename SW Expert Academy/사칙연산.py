def solution():
    N = int(input())
    node_connect_list = [[] for _ in range(N + 1)]
    node_value_list = [0 for _ in range(N + 1)]
    data_init(N, node_connect_list, node_value_list)
    return calculate_node(1, node_connect_list, node_value_list)


def data_init(N, node_connect_list, node_value_list):
    for _ in range(N):
        user_input = input().split()
        node_index = int(user_input[0])
        node_value = user_input[1]
        node_value_list[node_index] = node_value
        if len(user_input) != 2:
            node_connect_list[node_index].append(user_input[2])
            node_connect_list[node_index].append(user_input[3])


def calculate_node(idx, node_connect_list, node_value_list):
    if not len(node_connect_list[idx]):
        return node_value_list[idx]

    operator = node_value_list[idx]
    first_child_index = int(node_connect_list[idx][0])
    second_child_index = int(node_connect_list[idx][1])

    first_child_value = calculate_node(first_child_index, node_connect_list, node_value_list)
    second_child_value = calculate_node(second_child_index, node_connect_list, node_value_list)

    node_value_list[idx] = calulate(first_child_value, operator, second_child_value)

    return node_value_list[idx]


def calulate(value1, operator, value2):
    value1 = int(value1)
    value2 = int(value2)
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 // value2
    print('error')


test_case = 10
for tc in range(test_case):
    answer = solution()
    print('#{} {}'.format(tc + 1, answer))
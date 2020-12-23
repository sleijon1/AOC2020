from collections import deque
expressions = open("input.txt").read().replace(' ', '').splitlines()


def run_op(x, y, op):
    if x is None:
        return y
    if y is None:
        return x
    if op == '*':
        return y*x
    if op == '+':
        return y+x


def evaluate(str_expr):
    queue = deque([])
    index = 0
    curr_op = None
    result = None
    while index < len(str_expr):
        if str_expr[index] == '(':
            # new parenthesis, add to q
            queue.append([None, curr_op])
        elif str_expr[index] in ('+', '*'):
            if not queue:
                curr_op = str_expr[index]
            else:
                queue[-1][1] = str_expr[index]
        else:
            if queue:
                # we currently have at least one
                # expression that is in parenthesis
                queue_res, operation = queue[-1]
                if str_expr[index] == ')':
                    if len(queue) == 1:
                        # only par in queue, add to result
                        result = run_op(result, queue_res, curr_op)
                    else:
                        queue[-2][0] = run_op(queue[-2][0], queue_res, queue[-2][1])
                    queue.pop()
                else:
                    queue[-1][0] = run_op(
                        queue[-1][0], int(str_expr[index]), operation)
            else:
                # no parenthesis, just add to expression
                result = run_op(result, int(str_expr[index]), curr_op)

        index += 1

    return result


def add_parenthesis(expression: str) -> str:
    """ add parenthesis to prioritize addition """
    add_index = [i for i, val in enumerate(expression) if val == '+']
    exp_list = list(expression)
    for i, _ in enumerate(add_index):
        add_index = [i for i, val in enumerate(exp_list) if val == '+']
        # backwards
        index = add_index[i]
        opening = 0
        while index > 0:
            index -= 1
            if exp_list[index] == ')':
                opening += 1
            elif exp_list[index] == '(':
                opening -= 1
            elif exp_list[index] in ('+', '*'):
                continue
            if opening == 0:
                exp_list.insert(index, '(')
                break
                index = add_index[i]
        add_index = [i for i, val in enumerate(exp_list) if val == '+']
        index = add_index[i]
        opening = 0
        # forwards
        while index > 0:
            index += 1
            if exp_list[index] == '(':
                opening += 1
            elif exp_list[index] == ')':
                opening -= 1
            elif exp_list[index] in ('+', '*'):
                continue
            if opening == 0:
                exp_list.insert(index+1, ')')
                break
    return ''.join(exp_list)

expression_sum_1 = expression_sum_2 = 0
for expression in expressions:
    expression_sum_1 += (evaluate(expression))
    expression_sum_2 += (evaluate(add_parenthesis(expression)))

print(f"Solution part 1: {expression_sum_1}")
print(f"Solution part 1: {expression_sum_2}")

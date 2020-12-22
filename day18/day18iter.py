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


expression_sum = 0
for expression in expressions:
    expression_sum += (evaluate(expression))

print(f"Solution part 1: {expression_sum}")

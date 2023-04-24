# function to convert infix expression to postfix expression
def infix_to_postfix(expression):
    operator_precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output_queue = []
    operator_stack = []
    for token in expression.split():
        if token.isnumeric():
            output_queue.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            operator_stack.pop()
        else:
            while (operator_stack and operator_stack[-1] != '(' 
                   and operator_precedence.get(token, 0) <= operator_precedence.get(operator_stack[-1], 0)):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
    while operator_stack:
        output_queue.append(operator_stack.pop())
    return ' '.join(output_queue)


# function to evaluate postfix expression
def evaluate_postfix(expression):
    values = []
    for token in expression.split():
        if token.isnumeric():
            values.append(int(token))
        else:
            right = values.pop()
            left = values.pop()
            if token == '+':
                result = left + right
            elif token == '-':
                result = left - right
            elif token == '*':
                result = left * right
            elif token == '/':
                result = left / right
            elif token == '^':
                result = left ** right
            values.append(result)
    return values[0]


# main program
infix_expression = input("Enter an infix expression: ")
postfix_expression = infix_to_postfix(infix_expression)
print("Postfix expression:", postfix_expression)
result = evaluate_postfix(postfix_expression)
print("Result:", result)

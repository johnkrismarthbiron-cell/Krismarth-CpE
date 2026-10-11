import re


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            raise IndexError('pop from empty stack')
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        return self.top.value if self.top is not None else None


def convert_infix_to_postfix(expression):
    token_pattern = re.compile(r'\d+(?:\.\d*)?|\.\d+|[A-Za-z_]\w*|[()+*/^-]')
    tokens = []
    position = 0
    for match in token_pattern.finditer(expression):
        if expression[position:match.start()].strip():
            raise ValueError
        tokens.append(match.group())
        position = match.end()
    if expression[position:].strip() or not tokens:
        raise ValueError

    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operators = LinkedStack()
    output = []
    expects_operand = True

    for token in tokens:
        if token[0].isalnum() or token[0] == '_':
            if not expects_operand:
                raise ValueError
            output.append(token)
            expects_operand = False
        elif token == '(':
            if not expects_operand:
                raise ValueError
            operators.push(token)
        elif token == ')':
            if expects_operand:
                raise ValueError
            while operators.peek() is not None and operators.peek() != '(':
                output.append(operators.pop())
            if operators.peek() is None:
                raise ValueError
            operators.pop()
            expects_operand = False
        else:
            if expects_operand:
                raise ValueError
            while operators.peek() in precedence and (
                precedence[operators.peek()] > precedence[token]
                or (precedence[operators.peek()] == precedence[token] and token != '^')
            ):
                output.append(operators.pop())
            operators.push(token)
            expects_operand = True

    if expects_operand:
        raise ValueError
    while operators.peek() is not None:
        operator = operators.pop()
        if operator == '(':
            raise ValueError
        output.append(operator)
    return ' '.join(output)
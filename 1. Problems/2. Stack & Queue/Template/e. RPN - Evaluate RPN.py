# Evaluate Reverse Polish Notation (RPN) Expressions

'''
- Compute the arithmetic expression string (in RPN).
- Example:
"1,1,+,-2,x" -> "(1+1)x-2" -> "-4"
"3,4,+,2,x,1,+" -> "(3+4)x2+1" -> 15
'''
# O(N) time
def evaluate(expression: str) -> int:

    intermediate_results: List[int] = []
    delimiter = ','
    operators = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        '/': lambda y, x: x // y
    }

    for token in expression.split(delimiter):
        if token in operators:
            intermediate_results.append(operators[token](
                intermediate_results.pop(), intermediate_results.pop()))
        else:  # token is a number.
            intermediate_results.append(int(token))
    return intermediate_results[-1]

# Generate Strings of Matched Parens

'''
- Given an input number
- Generate all strings with that number of pairs of parens (parenthesis)
'''

# O((2k)!/((k!(k+1)!) time
def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    def directed_generate_balanced_parentheses(num_left_parens_needed,
                                               num_right_parens_needed,
                                               valid_prefix,
                                               result=[]):
        if num_left_parens_needed > 0:  # Able to insert '('.
            directed_generate_balanced_parentheses(num_left_parens_needed - 1,
                                                   num_right_parens_needed,
                                                   valid_prefix + '(')
        if num_left_parens_needed < num_right_parens_needed:
            # Able to insert ')'.
            directed_generate_balanced_parentheses(num_left_parens_needed,
                                                   num_right_parens_needed - 1,
                                                   valid_prefix + ')')
        if not num_right_parens_needed:
            result.append(valid_prefix)
        return result

    return directed_generate_balanced_parentheses(num_pairs,
                                                  num_pairs,
                                                  valid_prefix='')


def generate_balanced_parentheses_pythonic(num_pairs, num_left_open=0):
    if not num_pairs:
        return [')' * num_left_open]
    if not num_left_open:
        return [
            '(' + p for p in generate_balanced_parentheses_pythonic(
                num_pairs - 1, num_left_open + 1)
        ]
    else:
        return ([
            '(' + p for p in generate_balanced_parentheses_pythonic(
                num_pairs - 1, num_left_open + 1)
        ] + [
            ')' + p for p in generate_balanced_parentheses_pythonic(
                num_pairs - 1, num_left_open - 1)
        ])

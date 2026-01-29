letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"

""" 
TODO:
    implement solving for final operation = multiplication
    brackets
"""


def solve(func: str, n: int):
    tab = table(n)
    ans = []
    temp_list = []
    is_negated = False
    mult = func.replace(' ', '')
    mult = mult.replace('*', '')
    mult = mult.upper()
    mult = mult.replace('_', '!')
    mult = mult.replace('NOT', '!')
    mult = mult.split('+')
    for m in mult:
        temp_list = []
        for var in m:
            if var == '!':
                is_negated = True
                continue
            if is_negated:
                temp_list.append(negation(get_truth_list(var, tab)))
                is_negated = False
            else:
                temp_list.append(get_truth_list(var, tab))
        m = m.replace('!', '')
        if len(m) < 2:
            ans.append(temp_list[0])
            continue
        ans.append(bool_mult(temp_list, tab))
    if len(mult) < 2:
        return print_table(tab, ans[0])
    return print_table(tab, bool_add(ans, tab))
    
        

def table(n: int) -> list:
    # returns a list of rows based on the number of variables (n)
    contents = []
    cur_row = []
    for row in range(2 ** n):  # 2^n is the amount of rows in the table
        for var in range(1, n + 1):  # loop through the amount of given variables
            x = n + 1 - var  # flip value of 'var'; first value is n + 1, last is 1
            if row % (2 ** x) < (2 ** x) / 2:  # determines if variable is 0 or 1, based on current row and variable weight
                cur_row.append('0')
            else:
                cur_row.append('1')
        contents.append(cur_row)  # adds current row to main list
        cur_row = []  # clears the temporary list for next iteration
    return contents


def bool_add(variables: list, b_table: list) -> list:
    answer = []
    if len(variables) == 2:
        for a, b in zip(variables[0], variables[1]):
            if bool(int(a)) or bool(int(b)):
                answer.append(1)
            else:
                answer.append(0)
        return answer
    for a, b in zip(variables[0], variables[1]):
            if bool(int(a)) or bool(int(b)):
                answer.append(1)
            else:
                answer.append(0)
    variables.pop(0)
    variables.pop(1)
    variables.insert(0, answer)
    return bool_add(variables, b_table)


def bool_mult(variables: list, b_table: list) -> list:
    answer = []
    if len(variables) == 2:
        for a, b in zip(variables[0], variables[1]):
            if bool(int(a)) and bool(int(b)):
                answer.append(1)
            else:
                answer.append(0)
        return answer
    for a, b in zip(variables[0], variables[1]):
            if bool(int(a)) and bool(int(b)):
                answer.append(1)
            else:
                answer.append(0)
    variables.pop(0)
    variables.pop(1)
    variables.insert(0, answer)
    return bool_mult(variables, b_table)


def get_truth_list(n: str, reference: list) -> list:
    answer = []
    c = int(letters.index(n) / 2 + 1)
    for x in reference:
        i = 0
        for y in x:
            if i == c - 1:
                answer.append(y)
                i += 1
            else:
                i += 1
                continue
    return answer


def print_table(a: list, y: list = []) -> str:
    # takes the inputted table list and unpacks it into a more readable form
    if not y:
        y = ['a'] * len(a)
    result = f'{letters[:len(a[0]) * 2 - 1]} | Y\n{"-" * (len(a[0]) * 2 + 3)}'
    for row, i in zip(a, y):
        row.append('|')
        row.append(str(i))
        result = f'{result}\n{" ".join(row)}'  # removes the square brackets and starts a new line after every row
    return result


def negation(l: list) -> list:
    answer = []
    for item in l:
        answer. append(int(not bool(int(item))))
    return answer


print(solve('!A + b', 2))

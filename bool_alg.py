letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"


def solve(func: str = ''):
    # combine everything to return whole table with answer for given function (func)

    # make the string with function uniform for next operations
    mult = func.replace(' ', '')
    mult = mult.replace('*', '')
    mult = mult.upper()
    mult = mult.replace('_', '!')
    mult = mult.replace('NOT', '!')

    # get number of unique variables in function and set it as n
    n_vars = mult.replace('+', '')
    n_vars = n_vars.replace('!', '')
    n = len(set(n_vars))

    tab = table(n)
    ans = []
    is_negated = False
    if func.isdigit():  # if no function given, return table for n variables
        return print_table(a=table(int(func)))

    for var in n_vars:
        try:
            if letters.index(var) / 2 + 1 > n:
                return 'Please enter variables in alphabetic order beginning with "A".'
        except ValueError:
            return 'Invalid character.'

    mult = mult.split('+')  # split into multiplications

    for m in mult:
        temp_list = []  # clear the temporary list used for multiplication
        for var in m:
            if var == '!':  # set next variable to be negated
                is_negated = True
                continue
            if is_negated:  # negate variable
                temp_list.append(negation(get_truth_list(var, tab)))
                is_negated = False
            else:  # append normal variable
                temp_list.append(get_truth_list(var, tab))
        m = m.replace('!', '')  # get rid of negation
        if len(m) < 2:  # if length less than two (no multiplication needed), return single variable
            ans.append(temp_list[0])
            continue
        ans.append(bool_mult(temp_list, tab))  # multiply the values and append to answer list
    if len(mult) < 2:  # if length less than two (no addition needed), return single variable
        return print_table(tab, ans[0])
    return print_table(tab, bool_add(ans, tab))  # add contents of answer list


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
    # use 'or' operator to add two lists
    # works same as multiplication
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
    variables.pop(0)
    variables.insert(0, answer)
    return bool_add(variables, b_table)


def bool_mult(variables: list, b_table: list) -> list:
    # use 'and' operator to multiply two lists
    answer = []
    if len(variables) == 2:  # if there are two variables, multiply them
        for a, b in zip(variables[0], variables[1]):
            if bool(int(a)) and bool(int(b)):  # give result of multiplication
                answer.append(1)
            else:
                answer.append(0)
        return answer
    for a, b in zip(variables[0], variables[1]):  # if there are more than two variables, multiply first two and use recursion to multiply result with next item until solved
        if bool(int(a)) and bool(int(b)):
            answer.append(1)
        else:
            answer.append(0)
    # remove first two (already multiplied) variables
    variables.pop(0)
    variables.pop(0)
    variables.insert(0, answer)  # add result to index 0 of variables
    return bool_mult(variables, b_table)


def get_truth_list(n: str, reference: list) -> list:
    # returns list of values for given variable based on table
    answer = []
    c = int(letters.index(n) / 2 + 1)  # position number of variable
    for x in reference:
        i = 0
        for y in x:
            if i == c - 1:  # only append for right column
                answer.append(y)
                i += 1
                break
            else:
                i += 1
                continue
    return answer


def print_table(a: list, y=None) -> str:
    # takes the inputted table list and unpacks it into a more readable form
    if y is None:
        y = [' '] * len(a)  # if function not present, add spaces in its place
    result = f'{letters[:len(a[0]) * 2 - 1]} | Y\n{"-" * (len(a[0]) * 2 + 3)}'
    for row, i in zip(a, y):
        # loop through both the table and answer
        row.append('|')
        row.append(str(i))
        result = f'{result}\n{" ".join(row)}'  # removes the square brackets and starts a new line after every row
    return result


def negation(li: list) -> list:
    # takes a list of values and returns opposite values
    answer = []
    for item in li:
        answer.append(int(not bool(int(item))))  # convert item of list to bool, change it to opposite and convert back to number
    return answer


while True:
    print(solve(input('Enter function: Y = ')))

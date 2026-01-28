letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"


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
    addends = []
    answer = []
    for var in variables:
        addends.append(get_truth_list(int(letters.index(var) / 2 + 1), b_table))
    for a, b in zip(addends[0], addends[1]):
        if bool(int(a)) or bool(int(b)):
            answer.append(1)
        else:
            answer.append(0)
    return answer


def bool_mult(variables: list, b_table: list) -> list:
    multiplicants = []
    answer = []
    for var in variables:
        multiplicants.append(get_truth_list(int(letters.index(var) / 2 + 1), b_table))
    for a, b in zip(multiplicants[0], multiplicants[1]):
        if bool(int(a)) and bool(int(b)):
            answer.append(1)
        else:
            answer.append(0)
    return answer    


def get_truth_list(n: int, reference: list) -> list:
    answer = []
    for x in reference:
        i = 0
        for y in x:
            if i == n - 1:
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
    for row, i in zip(a, range(len(a) + 1)):
        row.append('|')
        row.append(str(y[i]))
        result = f'{result}\n{" ".join(row)}'  # removes the square brackets and starts a new line after every row
    return result


print(print_table(table(2), bool_add(['A', 'B'], table(2))))

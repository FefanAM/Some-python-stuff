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


def print_table(a: list) -> str:
    # takes the inputted table list and unpacks it into a more readable form
    result = ""
    for row in a:
        result = f'{result}\n{" ".join(row)}'  # removes the square brackets and starts a new line after every row
    return result


print(print_table(table(3)))

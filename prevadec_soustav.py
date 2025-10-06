from tkinter import *
root = Tk()
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def convertToLetter(num):
    if num > 9:
        dif = num - 10
        return chr(65 + dif)
    else:
        return num


def convertToNumber(let):
    if let in numbers:
        return let
    else:
        return ord(let) - 55


def binarize(z, r):
    m = []
    while z != 0:
        m.insert(0, convertToLetter(z % r))
        z = z // r
    return "".join(map(str, m))


def tens(z, r):
    res = 0
    z = str(z)
    z = ''.join(reversed(z))
    i = 0
    for x in z:
        res += int(convertToNumber(x)) * r ** i
        i += 1
    return res


def convert(num, radix, resultRadix):
    return binarize(tens(num, radix), resultRadix)


def clicked():
    result = convert(numberInput.get(), int(enteredRdInput.get()), int(wantedRdInput.get()))
    answer.configure(text="Your number is: " + result)


def clearall():
    numberInput.delete(0, END)
    enteredRdInput.delete(0, END)
    wantedRdInput.delete(0, END)
    answer.configure(text="")


root.title("Převaděč soustav")
root.geometry('260x170')
enteredNumber = Label(root, text="Number:")
numberInput = Entry(root, width=20)
enteredRadix = Label(root, text="Radix of number:")
enteredRdInput = Entry(root, width=20)
wantedRadix = Label(root, text="Designated radix:")
wantedRdInput = Entry(root, width=20)
calculate = Button(root, text="Calculate", command=clicked)
clear = Button(root, text="Clear all", command=clearall)
answer = Label(root, text="")
enteredNumber.grid(column=0, row=0, padx=4)
numberInput.grid(column=1, row=0, pady=10)
enteredRadix.grid(column=0, row=2, padx=4)
enteredRdInput.grid(column=1, row=2)
wantedRadix.grid(column=0, row=3, padx=4)
wantedRdInput.grid(column=1, row=3, pady=10)
calculate.grid(row=4, column=0, padx=4)
clear.grid(row=4, column=1)
answer.grid(row=6, columnspan=2, pady=10, padx=4)

root.mainloop()

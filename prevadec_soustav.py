from tkinter import *
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def convert_to_letter(num):
    if num > 9:
        dif = num - 10
        return chr(65 + dif)
    else:
        return num


def convert_to_number(let):
    let = let.upper()
    if let in numbers:
        return let
    else:
        return ord(let) - 55


def binarize(z, r):
    m = []
    while z != 0:
        m.insert(0, convert_to_letter(z % r))
        z = z // r
    return "".join(map(str, m))


def tens(z, r):
    res = 0
    z = str(z)
    z = ''.join(reversed(z))
    i = 0
    for x in z:
        res += int(convert_to_number(x)) * r ** i
        i += 1
    return res


def convert(num, radix, result_radix):
    for i in num:
        if int(convert_to_number(i)) >= radix or result_radix == 1:
            return "input error"
    return binarize(tens(num, radix), result_radix)


def clicked():
    if numberInput.get() == "" or enteredRdInput.get() == "" or wantedRdInput.get() == "":
        return
    else:
        result = convert(numberInput.get(), int(enteredRdInput.get()), int(wantedRdInput.get()))
        answer.configure(text="Your answer is: " + result)


def clear_all():
    numberInput.delete(0, END)
    enteredRdInput.delete(0, END)
    wantedRdInput.delete(0, END)
    answer.configure(text="")


def move_app(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')


root = Tk()
root.configure(background="black", bd=0)
root.geometry('260x170')
# Create custom titlebar and close button + window moving
root.overrideredirect(True)
title_bar = Frame(root, background="black", bd=0)
title_bar.pack(expand=True, fill=X)
title_bar.bind("<B1-Motion>", move_app)
title_label = Label(title_bar, text="  Převaděč", background="black", fg="white", font="arial, 10")
title_label.pack(side=LEFT)
close_btn = Button(title_bar, text="x ", command=root.quit, background="black", fg="white", bd=0, font="arial, 15")
close_btn.pack(side=RIGHT)
# Entered number label + entry
numberFrame = Frame(root, background="#313336")
enteredNumber = Label(numberFrame, text="Number:", background="#313336", fg="white")
numberInput = Entry(numberFrame, width=20, background="#608279", fg="white")
numberFrame.pack(side=TOP, expand=True, fill=BOTH)
enteredNumber.pack(side=LEFT, expand=True, fill=X)
numberInput.pack(side=LEFT, expand=True, fill=X)
# Radix of number label + entry
r1frame = Frame(root, background="#313336")
enteredRadix = Label(r1frame, text="Radix of number:", background="#313336", fg="white")
enteredRdInput = Entry(r1frame, width=20, background="#608279", fg="white")
r1frame.pack(side=TOP, expand=True, fill=BOTH)
enteredRadix.pack(side=LEFT, expand=True, fill=X)
enteredRdInput.pack(side=LEFT, expand=True, fill=X)
# Second radix label + entry
r2frame = Frame(root, background="#313336")
wantedRadix = Label(r2frame, text="Designated radix:", background="#313336", fg="white")
wantedRdInput = Entry(r2frame, width=20, background="#608279", fg="white")
r2frame.pack(side=TOP, expand=True, fill=BOTH)
wantedRadix.pack(side=LEFT, expand=True, fill=X)
wantedRdInput.pack(side=LEFT, expand=True, fill=X)
# Buttons
buttonsFrame = Frame(root, background="#313336")
calculate = Button(buttonsFrame, text="Calculate", command=clicked, background="#608279", fg="white")
clear = Button(buttonsFrame, text="Clear all", command=clear_all, background="#608279", fg="white")
buttonsFrame.pack(side=TOP, expand=True, fill=BOTH)
calculate.pack(side=LEFT, expand=True, fill=X)
clear.pack(side=LEFT, expand=True, fill=X)
# Part where answer is displayed
answer = Label(root, text="", fg="white", background="#313336")
answer.pack(side=TOP, expand=True, fill=BOTH)

root.mainloop()


def isIntger(entr):
    isInt = True
    num = 0
    try:
        int(entr.get())
        entr.config(highlightthickness=0, bg="white")
        num = int(entr.get())
        isInt = True
        if num<=0:
            entr.config(highlightthickness=2, highlightbackground="red",
                        bg="red", highlightcolor="red")
            num = 0
            isInt = False
    except ValueError:
        print("in except")
        if not entr.get():
            num = 0
            isInt = True
        else:
            entr.config(highlightthickness=2, highlightbackground="red",
                        bg="red", highlightcolor="red")
            isInt = False

    return isInt, num


def isFloat(entr):
    isfloat = True
    num = None
    try:
        float(entr.get())
        entr.config(highlightthickness=0, bg="white")
        isfloat = True
        num = float(entr.get())
    except ValueError:
        if not entr.get():
            num = 0
            isfloat = True
        else:
            entr.config(highlightthickness=2, highlightbackground="red",
                        bg="red", highlightcolor="red")
            isfloat = False

    return isfloat, num

from tkinter import ttk as tk
from tkinter import *
from tkinter import messagebox
import sys, os

third_field_exists = False
all_fields = False
decimal_result = 0

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def Calculate():
    """ Calculates the result of adding fractions """
    global fraction_1_num, fraction_1_denom, fraction_2_num, fraction_2_denom, decimal_result
    length = 2
    if third_field_exists:
        if all_fields: length = 4
        else: length = 3
    result = 0, 0
    match length:
        case 2:
            resarr = [fraction_1_num.get(), fraction_1_denom.get(), fraction_2_num.get(), fraction_2_denom.get()]
            for i in resarr:
                if not isint(i):
                    messagebox.showerror(title='Ошибка', message='Некорректный ввод значений!')
                    break
            else:
                result = AddUpFractions(int(resarr[0]), int(resarr[1]), int(resarr[2]), int(resarr[3]))
        case 3:
            resarr = [fraction_1_num.get(), fraction_1_denom.get(), fraction_2_num.get(), fraction_2_denom.get(), fraction_3_num.get(), fraction_3_denom.get()]
            for i in resarr:
                if not isint(i):
                    messagebox.showerror(title='Ошибка', message='Некорректный ввод значений!')
                    break
            else:
                tmp = AddUpFractions(int(resarr[0]), int(resarr[1]), int(resarr[2]), int(resarr[3]))
                result = AddUpFractions(tmp[0], tmp[1], int(resarr[4]), int(resarr[5]))
        case 4:
            resarr = [fraction_1_num.get(), fraction_1_denom.get(), fraction_2_num.get(), fraction_2_denom.get(), fraction_3_num.get(), fraction_3_denom.get(), fraction_4_num.get(), fraction_4_denom.get()]
            for i in resarr:
                if not isint(i):
                    messagebox.showerror(title='Ошибка', message='Некорректный ввод значений!')
                    break
            else:
                tmp1 = AddUpFractions(int(resarr[0]), int(resarr[1]), int(resarr[2]), int(resarr[3]))
                tmp2 = AddUpFractions(tmp1[0], tmp1[1], int(resarr[4]), int(resarr[5]))
                result = AddUpFractions(tmp2[0], tmp2[1], int(resarr[6]), int(resarr[7]))
    answer_num.config(text=result[0])
    answer_denom.config(text=result[1])
    decimal_result = round(int(result[0]) / int(result[1]), 9)
    decimal_answer.config(text=decimal_result)
    
    
    
    
    
def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
def reset():
    global third_field_exists, all_fields, fraction_3, fraction_3_num, fraction_3_denom, fraction_3_label, fraction_3_minus, fraction_4, fraction_4_num, fraction_4_denom, fraction_4_label, fraction_4_minus
    third_field_exists, all_fields = False, False
    fraction_3.pack_forget()
    fraction_3_label.pack_forget()
    fraction_3_num.pack_forget()
    fraction_3_minus.pack_forget()
    fraction_3_denom.pack_forget()
    fraction_4.pack_forget()
    fraction_4_label.pack_forget()
    fraction_4_num.pack_forget()
    fraction_4_minus.pack_forget()
    fraction_4_denom.pack_forget()
    add_button.grid(row=0, column = 2)
    fraction_1_num.delete(0, END)
    fraction_1_denom.delete(0, END)
    fraction_2_num.delete(0, END)
    fraction_2_denom.delete(0, END)
    fraction_3_num.delete(0, END)
    fraction_3_denom.delete(0, END)
    fraction_4_num.delete(0, END)
    fraction_4_denom.delete(0, END)
    answer_num.config(text=0)
    answer_denom.config(text=0)
    fraction_1_num.focus()
def AddField():
    global third_field_exists, all_fields, fraction_3, fraction_3_num, fraction_3_denom, fraction_3_label, fraction_3_minus, fraction_4, fraction_4_num, fraction_4_denom, fraction_4_label, fraction_4_minus, add_button
    if not all_fields:
        if not third_field_exists:
            fraction_3.grid(row=0, column = 2)
            fraction_3_label.pack(ipadx=10, ipady=10, side=TOP)
            fraction_3_num.pack(padx=5, pady=5)
            fraction_3_minus.pack(ipadx=10, ipady=10, side=TOP)
            fraction_3_denom.pack(padx=5, pady=5)
            add_button.grid(row=0, column = 3)
            third_field_exists = True
        else:
            fraction_4.grid(row=0, column = 3)
            fraction_4_label.pack(ipadx=10, ipady=10, side=TOP)
            fraction_4_num.pack(padx=5, pady=5)
            fraction_4_minus.pack(ipadx=10, ipady=10, side=TOP)
            fraction_4_denom.pack(padx=5, pady=5)
            add_button.grid_forget()
            all_fields = True
    
def AddUpFractions(num1, denom1, num2, denom2):
    global answer_num, answer_denom
    NOK = FindSmallestJointMultiple(denom1, denom2)
    dop1 = NOK // denom1
    dop2 = NOK // denom2
    result = FractionReduction(num1 * dop1 + num2 * dop2, denom1 * dop1)
    return result

def FindSmallestJointMultiple(m, n):
    return abs(m * n) // Eucledean(m, n)

def FractionReduction(numerator, denominator):
    divider = Eucledean(numerator, denominator)
    if divider > 1:
        return FractionReduction(numerator // divider, denominator // divider)
    return numerator, denominator

def Eucledean(M, N):
    m = abs(M)
    n = abs(N)
    if m == 0 or n == 0:
        return abs(m - n)
    else:
        if m > n:
            return Eucledean(m % n, n)
        return Eucledean(n % m, m)

def switch_focus(event):
    global third_field_exists, all_fields
    match str(event.widget):
        case '.!frame.!entry':
            fraction_1_denom.focus()
        case '.!frame.!entry2':
            fraction_2_num.focus()
        case '.!frame2.!entry':
            fraction_2_denom.focus()
        case '.!frame2.!entry2':
            if third_field_exists:
                fraction_3_num.focus()
            else:
                Calculate()
        case '.!frame3.!entry':
            fraction_3_denom.focus()
        case '.!frame3.!entry2':
            if all_fields:
                fraction_4_num.focus()
            else:
                Calculate()
        case '.!frame4.!entry':
            fraction_4_denom.focus()
        case '.!frame4.!entry2':
            Calculate()
        case default:
            print('в плане где ты еще поля ввода нашел')

def copy():
    global decimal_result
    root.clipboard_append(decimal_result)
root = Tk()
root.title("Сложение дробей")
root.config(bg='azure3')
root.iconbitmap('icon.ico')
root.geometry('830x600+80+80')
root.resizable(False, False)

(fraction_1 := Frame(root, bg='azure3')).grid(row=0, column = 0)
Label(fraction_1, text='Первая дробь:', bg='azure3').pack(ipadx=10, ipady=10, side=TOP)
(fraction_1_num := Entry(fraction_1)).pack(padx=5, pady=5)
Label(fraction_1, text='-------------------------', bg='azure3').pack(ipadx=10, ipady=10, side=TOP)
(fraction_1_denom := Entry(fraction_1)).pack(padx=5, pady=5)
fraction_1_num.bind("<Return>", switch_focus)
fraction_1_denom.bind("<Return>", switch_focus)

(fraction_2 := Frame(root, bg='azure3')).grid(row=0, column = 1)
Label(fraction_2, text='Вторая дробь:', bg='azure3').pack(ipadx=10, ipady=10, side=TOP)
(fraction_2_num := Entry(fraction_2)).pack(padx=5, pady=5)
Label(fraction_2, text='-------------------------', bg='azure3').pack(ipadx=10, ipady=10, side=TOP)
(fraction_2_denom := Entry(fraction_2)).pack(padx=5, pady=5)
fraction_2_num.bind("<Return>", switch_focus)
fraction_2_denom.bind("<Return>", switch_focus)

fraction_3 = Frame(root, bg='azure3')
fraction_3_label = Label(fraction_3, text='Третья дробь:', bg='azure3')
fraction_3_num = Entry(fraction_3)
fraction_3_minus = Label(fraction_3, text='-------------------------', bg='azure3')
fraction_3_denom = Entry(fraction_3)
fraction_3_num.bind("<Return>", switch_focus)
fraction_3_denom.bind("<Return>", switch_focus)

fraction_4 = Frame(root, bg='azure3')
fraction_4_label = Label(fraction_4, text='Четвертая дробь:', bg='azure3')
fraction_4_num = Entry(fraction_4)
fraction_4_minus = Label(fraction_4, text='-------------------------', bg='azure3')
fraction_4_denom = Entry(fraction_4)
fraction_4_num.bind("<Return>", switch_focus)
fraction_4_denom.bind("<Return>", switch_focus)
fraction_1_num.focus()

(answer := Frame(root, bg='azure3')).grid(row=0, column = 4)
Label(answer, text='Ответ:', bg='azure3').pack(ipadx=10, ipady=10, side=TOP)
(answer_num := Label(answer, text=0, bg='azure3')).pack(ipadx=10, ipady=10, side=TOP)
Label(answer, text='--------', bg='azure3').pack(ipadx=10, ipady=10, side=TOP)
(answer_denom := Label(answer, text=0, bg='azure3')).pack(ipadx=10, ipady=10, side=TOP)
(decimal_answer := Label(root, text=0, bg='azure3')).grid(row=1, column = 4)
copy_image = PhotoImage(file = "copy.png")
(copy_button := Button(root, text='Копировать', bg='darkgray', relief=GROOVE, command=copy, bd=8, image=copy_image, compound=TOP)).grid(row=2, column = 4)


(add_button := Button(root, text='+', bg='darkgray', relief=GROOVE, bd=8, width=8, command=AddField)).grid(row=0, column = 2)
Button(root, text='Рассчитать', bg='darkgray', relief=GROOVE, bd=8, width=28, command=Calculate).grid(row=1, column = 2)
Button(root, text='Сброс', bg='darkgray', relief=GROOVE, bd=8, width=28, command=reset).grid(row=1, column = 3)
root.mainloop()
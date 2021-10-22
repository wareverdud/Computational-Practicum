from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import first_page
import second_page
import third_page
from main import Main, MainUpdated
import exceptions

program = Main()
program3 = MainUpdated()

app = Tk()
app.title('Differential Equations')

notebook = ttk.Notebook(app)

tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)
notebook.add(tab1, text='Page 1')
notebook.add(tab2, text='Page 2')
notebook.add(tab3, text='Page 3')
notebook.pack(expand=True, fill='both')

e = BooleanVar(master=tab1, value=True)
ie = BooleanVar(master=tab1, value=True)
rk = BooleanVar(master=tab1, value=True)
ex = BooleanVar(master=tab1, value=True)

e_3 = BooleanVar(master=tab3, value=True)
ie_3 = BooleanVar(master=tab3, value=True)
rk_3 = BooleanVar(master=tab3, value=True)

first_page.run(program)
second_page.run(program)
third_page.run(program3)

picture1 = PhotoImage(file='figure1.png')
graph1 = Label(tab1, image=picture1)
graph1.pack()

picture2 = PhotoImage(file='figure2.png')
graph2 = Label(tab2, image=picture2)
graph2.pack()

picture3 = PhotoImage(file='figure3.png')
graph3 = Label(tab3, image=picture3)
graph3.pack()


def update():
    global graph1
    global picture1
    picture1 = PhotoImage(file='figure1.png')
    graph1.config(image=picture1)

    global graph2
    global picture2
    picture2 = PhotoImage(file='figure2.png')
    graph2.config(image=picture2)


def catch_disc(function):
    def wrapper():
        try:
            function()
        except ZeroDivisionError:
            messagebox.showinfo(title='Error', message='Suddenly division by zero')
        except exceptions.Solution as exc:
            messagebox.showinfo(title='Error', message=f'Given interval has a discontinuity at point {exc.x}\nTry '
                                                       f'another interval')
        except exceptions.Constant:
            messagebox.showinfo(title='Error', message='Constant cannot be computer\nTry another initial values')
        except exceptions.Derivative:
            messagebox.showinfo(title='Error', message='Derivative cannot be computed')
        except exceptions.Step:
            messagebox.showinfo(title='Error', message='Step is >= 1\nTry greater number of steps')
    return wrapper


@catch_disc
def change_N():
    # temp_N = int(entry_N.get())
    # program.
    program.N = int(entry_N.get())
    first_page.run(program)
    second_page.run(program)
    update()


@catch_disc
def change_x0():
    program.x0 = float(entry_x0.get())
    program3.x0 = float(entry_x0.get())
    first_page.run(program)
    second_page.run(program)
    update()


@catch_disc
def change_y0():
    program.y0 = float(entry_y0.get())
    program3.y0 = float(entry_y0.get())
    first_page.run(program)
    second_page.run(program)
    update()


@catch_disc
def change_X():
    program.X = float(entry_X.get())
    program3.X = float(entry_X.get())
    first_page.run(program)
    second_page.run(program)
    update()


@catch_disc
def euler():
    program.e = e.get()
    first_page.run(program)
    second_page.run(program)
    update()


@catch_disc
def ieuler():
    program.ie = ie.get()
    first_page.run(program)
    second_page.run(program)
    update()


@catch_disc
def rungekutta():
    program.rk = rk.get()
    first_page.run(program)
    second_page.run(program)
    update()


@catch_disc
def exact():
    program.ex = ex.get()
    first_page.run(program)
    second_page.run(program)
    update()


entry_N = Entry(tab1)
entry_N.pack(side=LEFT)
submit_N = Button(tab1, text='Change N', command=change_N)
submit_N.pack(side=LEFT)

entry_x0 = Entry(tab1)
entry_x0.pack(side=LEFT)
submit_x0 = Button(tab1, text='Change x0', command=change_x0)
submit_x0.pack(side=LEFT)

entry_y0 = Entry(tab1)
entry_y0.pack(side=LEFT)
submit_y0 = Button(tab1, text='Change y0', command=change_y0)
submit_y0.pack(side=LEFT)

entry_X = Entry(tab1)
entry_X.pack(side=LEFT)
submit_X = Button(tab1, text='Change X', command=change_X)
submit_X.pack(side=LEFT)

enable_euler = Checkbutton(tab1, text='Euler Method', variable=e, offvalue=False, onvalue=True, command=euler)
enable_euler.pack(side=RIGHT)
enable_improved = Checkbutton(tab1, text='Improved Euler Method', variable=ie, offvalue=False, onvalue=True,
                              command=ieuler)
enable_improved.pack(side=RIGHT)
enable_rk = Checkbutton(tab1, text='Runge-Kutta Method', variable=rk, offvalue=False, onvalue=True, command=rungekutta)
enable_rk.pack(side=RIGHT)
enable_exact = Checkbutton(tab1, text='Exact', variable=ex, offvalue=False, onvalue=True, command=exact)
enable_exact.pack(side=RIGHT)


@catch_disc
def update_3():
    global graph3
    global picture3
    picture3 = PhotoImage(file='figure3.png')
    graph3.config(image=picture3)


@catch_disc
def change_n0():
    program3.n0 = int(entry_n0.get())
    third_page.run(program3)
    update_3()


@catch_disc
def change_n():
    program3.n_final = int(entry_n.get())
    third_page.run(program3)
    update_3()


@catch_disc
def euler_3():
    program3.e = e_3.get()
    third_page.run(program3)
    update_3()


@catch_disc
def ieuler_3():
    program3.ie = ie_3.get()
    third_page.run(program3)
    update_3()


@catch_disc
def rungekutta_3():
    program3.rk = rk_3.get()
    third_page.run(program3)
    update_3()


entry_n0 = Entry(tab3)
entry_n0.pack(side=LEFT)
submit_n0 = Button(tab3, text='Change n0', command=change_n0)
submit_n0.pack(side=LEFT)

entry_n = Entry(tab3)
entry_n.pack(side=LEFT)
submit_n = Button(tab3, text='Change N', command=change_n)
submit_n.pack(side=LEFT)

enable_euler_3 = Checkbutton(tab3, text='Euler Method', variable=e_3, offvalue=False, onvalue=True, command=euler_3)
enable_euler_3.pack(side=RIGHT)
enable_improved_3 = Checkbutton(tab3, text='Improved Euler Method', variable=ie_3, offvalue=False, onvalue=True,
                                command=ieuler_3)
enable_improved_3.pack(side=RIGHT)
enable_rk_3 = Checkbutton(tab3, text='Runge-Kutta Method', variable=rk_3, offvalue=False, onvalue=True,
                          command=rungekutta_3)
enable_rk_3.pack(side=RIGHT)

app.mainloop()

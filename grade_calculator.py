import tkinter as tk
from tkinter.ttk import *
from tkinter import *


def calculate():
    gpa_points = 0
    result = ""
    q1 = combo1.get()
    q2 = combo2.get()
    q3 = combo3.get()
    grades = [q1, q2, q3]
    if q3 == "None":
        length = 2
        f = 14
    else:
        length = 3
        f = 32
    for i in range(0, length):
        a = 0
        if grades[i] == "A+":
            a += 24
        elif grades[i] == "A":
            a += 22
        elif grades[i] == "A-":
            a += 20
        elif grades[i] == "B+":
            a += 18
        elif grades[i] == "B":
            a += 16
        elif grades[i] == "B-":
            a += 14
        elif grades[i] == "C+":
            a += 12
        elif grades[i] == "C":
            a += 10
        elif grades[i] == "C-":
            a += 8
        elif grades[i] == "D+":
            a += 6
        elif grades[i] == "D":
            a += 4
        elif grades[i] == "D-":
            a += 2
        if i == 2:
            a = a / 2
        gpa_points += a

    if q3 == "None":
        gpa = gpa_points / 4
        if gpa == 12:
            result = "You need at least an A- for an A+\n" \
                     "or a C for an A"
        elif gpa == 11.5:
            result = "You need an A+ for an A+\n" \
                     "or a B- for an A"
        elif gpa == 11:
            result = "You need at least a B+ for an A\n" \
                     "or a C- for an A-"
        elif gpa == 10.5:
            result = "You need at least an A for an A\n" \
                     "or a C+ for an A- "
        elif gpa == 10:
            result = "You need at least a B for an A-\n" \
                     "or a D+ for a B+"
        elif gpa == 9.5:
            result = "You need at least an A- for an A-\n" \
                     "or a C for a B+"
        elif gpa == 9:
            result = "You need an A+ for an A-,\n" \
                     "a B- for a B+, or a D for a B"
        elif gpa == 8.5:
            result = "You need at least a B+ for a B+\n" \
                     "or a C- for a B"
        elif gpa == 8:
            result = "You need at least an A for a B+,\n" \
                     "a C+ for a B, or a D- for a B-"
        elif gpa == 7.5:
            result = "You need at least a B for a B\n" \
                     "or a D+ for a B-"
        elif gpa == 7:
            result = "You need at least an A- for a B\n" \
                     "or a C for a B-"
        elif gpa == 6.5:
            result = "You need at an A+ for a B,\n" \
                     "a B- for a B-, or a D for a C"
        elif gpa == 6:
            result = "You need at least a B+ for a B-\n" \
                     "or a C- for a C+"
        elif gpa == 5.5:
            result = "You need at least C+ for a C+\n" \
                     "or a D- for a C"
        elif gpa == 5:
            result = "You need at least B for a C+\n" \
                     "or a D+ for a C"
        elif gpa == 4.5:
            result = "You need at least a C for a C"
        elif gpa == 4:
            result = "You need at least a B- for a C\n " \
                     "or a D- for a C-"
        elif gpa == 3.5:
            result = "You need at least a B+ for a C\n" \
                     "or at least a C- for a C-"
        elif gpa == 3:
            result = "You need at least an A for a C,\n" \
                     "a C+ for a C-, or a D- for a D+"
        elif gpa == 2.5:
            result = "You need at least a D+ for a D+\n" \
                     "for a B for a C-"
        elif gpa == 2:
            result = "You need at least a C for a D+"
        elif gpa == 1.5:
            result = "You need at least a B- for a D+\n" \
                     "or a D for a D"
        elif gpa == 1:
            result = "You need at least an A- for a D+\n" \
                     "or a C- for a D"
        elif gpa == .5:
            result = "You need at least a A for a D\n" \
                     "or a D- for a D-"
        else:
            result = "You need at least a D+ for a D-"

    else:
        gpa = gpa_points / 5
        if gpa >= 11.5:
            result = "A+"
        elif gpa >= 10.5:
            result = "A"
        elif gpa >= 9.5:
            result = "A-"
        elif gpa >= 8.5:
            result = "B+"
        elif gpa >= 7.5:
            result = "B"
        elif gpa >= 6.5:
            result = "B-"
        elif gpa >= 5.5:
            result = "C+"
        elif gpa >= 4.5:
            result = "C"
        elif gpa >= 3.5:
            result = "C-"
        elif gpa >= 2.5:
            result = "D+"
        elif gpa >= 1.5:
            result = "D"
        elif gpa >= .5:
            result = "D-"

    the_result = Label(lower_frame, text="", font=('Arial Gothic', f), bg='white')
    the_result.place(relheight=1, relwidth=1)
    the_result['text'] = result


def calculator():
    try:
        gpa = gpa_entry.get()
        credits = credits_entry.get()
        number_weighted_classes = weighted.get()
        g1 = combor1.get()
        g2 = combor2.get()
        g3 = combor3.get()
        g4 = combor4.get()
        g5 = combor5.get()
        g6 = combor6.get()
        g7 = combor7.get()
        if g7 == "None":
            new_credits = 6
            length = 6
            if number_weighted_classes == '7':
                raise Exception("Only 6 classes selected")
        else:
            new_credits = 7
            length = 7
        gpa_points = float(gpa) * float(credits) + float(number_weighted_classes)
        grades = [g1, g2, g3, g4, g5, g6, g7]
        for i in range(0, length):
            if grades[i] == "A+":
                gpa_points += 4.3
            elif grades[i] == "A":
                gpa_points += 4
            elif grades[i] == "A-":
                gpa_points += 3.7
            elif grades[i] == "B+":
                gpa_points += 3.3
            elif grades[i] == "B":
                gpa_points += 3
            elif grades[i] == "B-":
                gpa_points += 2.7
            elif grades[i] == "C+":
                gpa_points += 2.3
            elif grades[i] == "C":
                gpa_points += 2
            elif grades[i] == "C-":
                gpa_points += 1.7
            elif grades[i] == "D+":
                gpa_points += 1.3
            elif grades[i] == "D":
                gpa_points += 1
            elif grades[i] == "D-":
                gpa_points += .7
        new_gpa = gpa_points / (float(credits) + float(new_credits))
        result = str(new_gpa)[:6]
    except:
        result = "Invalid input"

    the_result = Label(result_frame, text="", font=('Arial Gothic', 14, "bold"), bg='white')
    the_result.place(relheight=1, relwidth=1)
    the_result['text'] = result


root = tk.Tk()
root.title("Semester Grade Calculator")

canvas = tk.Canvas(root, height=500, width=750)
canvas.pack()
background = tk.Frame(root, bg='#376334')
background.place(relx=0, rely=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#376334')
frame.place(relx=0, relwidth=.5, relheight=.6)
frame_right = tk.Frame(root, bg='#376334')
frame_right.place(relx=.5, relwidth=.5, relheight=.8)
title_frame = tk.Frame(root, bg='black')
title_frame.place(relx=0, relwidth=1, relheight=.15)
lower_frame = tk.Frame(root, bg='white')
lower_frame.place(relx=.05, rely=.52, relwidth=.40, relheight=.40)
result_frame = tk.Frame(root, bg='white')
result_frame.place(relx=.59, rely=.82, relwidth=.31, relheight=.1)


header = tk.Label(title_frame, text="Use the calculator to test different\n"
                              "Final Exam score scenarios.", font=('Arial Gothic', 12, 'bold'), fg='white', bg='black')
header.place(relx=.06, rely=.25)
header2 = tk.Label(title_frame, text="You can also calculate your future GPA", font=('Arial Gothic', 12, 'bold'), fg='white', bg='black')
header2.place(relx=.53, rely=.3)

quarter1Label1 = tk.Label(frame, text="   Quarter 1 Grade", font=('Arial Gothic', 10, 'bold'), bg='#376334', fg='white')
quarter1Label1.place(relx=.11, rely=.28, relwidth=.5)
quarter1Label2 = tk.Label(frame, text="   Quarter 2 Grade", font=('Arial Gothic', 10, 'bold'), bg='#376334', fg='white')
quarter1Label2.place(relx=.11, rely=.42, relwidth=.5)
fina1ExamLabel = tk.Label(frame, text="Final Exam Grade", font=('Arial Gothic', 10, 'bold'), bg='#376334', fg='white')
fina1ExamLabel.place(relx=.11, rely=.55, relwidth=.5)

finalExamNoteLabel = Label(frame, text="If None, the Calculator displays\nthe score that you would need. ",
                           font=('Arial Gothic', 10, 'bold'), bg='#376334', fg='white')
finalExamNoteLabel.place(rely=.68, relwidth=.75)

calculateButton = Button(frame, text="Calculate", font=('Arial Gothic', 10, "bold"), bg='white', command=calculate)
calculateButton.place(relx=.67, rely=.69, relwidth=.21, relheight=.11)

combo1 = Combobox(frame, font=('Arial Gothic', 10))
combo1['values'] = ("A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F")
combo1.current(0)  # sets the selected item
combo1.place(relx=.55, rely=.28, relwidth=.3, relheight=.08)
combo2 = Combobox(frame, font=('Arial Gothic', 10))
combo2['values'] = ("A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F")
combo2.current(0)  # sets the selected item
combo2.place(relx=.55, rely=.42, relwidth=.3, relheight=.08)
combo3 = Combobox(frame, font=('Arial Gothic', 10))
combo3['values'] = ("None", "A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F")
combo3.current(0)  # sets the selected item
combo3.place(relx=.55, rely=.55, relwidth=.3, relheight=.08)

cumulative_gpa = tk.Label(frame_right, text="   Cumulative GPA", font=('Arial Gothic', 10, 'bold'), bg='#376334', fg='white')
cumulative_gpa.place(rely=.2, relwidth=.5)
credits = tk.Label(frame_right, text="       Total Credits", font=('Arial Gothic', 10, 'bold'), bg='#376334', fg='white')
credits.place(rely=.3, relwidth=.5)
weighted_classes = tk.Label(frame_right, text="Weighted Classes", font=('Arial Gothic', 10, 'bold'), bg='#376334', fg='white')
weighted_classes.place(rely=.4, relwidth=.5)
results = tk.Label(frame_right, text="               Grades", font=('Arial Gothic', 10, 'bold'), bg='#376334', fg='white')
results.place(rely=.5, relwidth=.5)

gpa_entry = Entry(frame_right)
gpa_entry.place(relx=.5, rely=.2, relwidth=.3, relheight=.06)
credits_entry = Entry(frame_right)
credits_entry.place(relx=.5, rely=.3, relwidth=.3, relheight=.06)
weighted = Combobox(frame_right, font=('Arial Gothic', 10))
weighted['values'] = ("0", "1", "2", "3", "4", "5", "6", "7")
weighted.place(relx=.5, rely=.4, relwidth=.3, relheight=.06)

combor1 = Combobox(frame_right, font=('Arial Gothic', 10))
combor1['values'] = ("A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F")
combor1.current(0)  # sets the selected item
combor1.place(relx=.5, rely=.5, relwidth=.3, relheight=.06)
combor2 = Combobox(frame_right, font=('Arial Gothic', 10))
combor2['values'] = ("A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F")
combor2.current(0)  # sets the selected item
combor2.place(relx=.5, rely=.56, relwidth=.3, relheight=.06)
combor3 = Combobox(frame_right, font=('Arial Gothic', 10))
combor3['values'] = ("A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F")
combor3.current(0)  # sets the selected item
combor3.place(relx=.5, rely=.62, relwidth=.3, relheight=.06)
combor4 = Combobox(frame_right, font=('Arial Gothic', 10))
combor4['values'] = ("A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F")
combor4.current(0)  # sets the selected item
combor4.place(relx=.5, rely=.68, relwidth=.3, relheight=.06)
combor5 = Combobox(frame_right, font=('Arial Gothic', 10))
combor5['values'] = ("A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F")
combor5.current(0)  # sets the selected item
combor5.place(relx=.5, rely=.74, relwidth=.3, relheight=.06)
combor6 = Combobox(frame_right, font=('Arial Gothic', 10))
combor6['values'] = ("A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F")
combor6.current(0)  # sets the selected item
combor6.place(relx=.5, rely=.8, relwidth=.3, relheight=.06)
combor7 = Combobox(frame_right, font=('Arial Gothic', 10))
combor7['values'] = ("None", "A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F")
combor7.current(0)  # sets the selected item
combor7.place(relx=.5, rely=.86, relwidth=.3, relheight=.06)

calculateButton = Button(frame_right, text="Calculate", font=('Arial Gothic', 10, "bold"), bg='white', command=calculator)
calculateButton.place(relx=.18, rely=.84, relwidth=.25, relheight=.08)

root.mainloop()

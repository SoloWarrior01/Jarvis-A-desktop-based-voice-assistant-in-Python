import calendar
import datetime
import sys
import tkinter as tk
import csv

child = None
root1 = None


class Calendar:
    week_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    def __init__(self, parent):
        self.parent = parent
        self.cal = calendar.TextCalendar(calendar.SUNDAY)
        self.year = datetime.date.today().year
        self.month = datetime.date.today().month
        self.wid = []
        self.day_selected = datetime.date.today().day
        self.month_selected = self.month
        self.year_selected = self.year
        self.day_name = self.week_day[datetime.date.today().weekday()]
        self.new_event = tk.StringVar()
        self.setup(self.year, self.month)

    def event(self):
        with open('D:\Python\#JARVIS\JARVIS    version - 6.3.4\intents\eventsincalender.csv', 'r') as f:
            data = csv.reader(f)
            for i in list(data):
                if i == []:
                    pass

                elif (i[0] == str(self.day_selected)) and (i[1] == str(self.month_selected)):
                    return i[2]

                else:
                    pass
            return '                                                      '

    def button_pushed(self):
        self.new_event = self.new_event_entry.get()
        self.write_event(self.new_event)
        self.clear()
        self.setup(self.year, self.month)

    def write_event(self, event):
        if (event is not None) or (event != ''):
            f = open('D:\Python\#JARVIS\JARVIS    version - 6.3.4\intents\eventsincalender.csv', 'r')
            data = list(csv.reader(f))
            for i in data:
                if len(i) != 0:
                    if (i[0] == str(self.day_selected)) and (i[1] == str(self.month_selected)):
                        data.remove(i)
                else:
                    pass
            data.append([str(self.day_selected), str(self.month_selected), event])

            for i in data:
                if i == []:
                    data.remove(i)
            f.close()

            f = open('D:\Python\#JARVIS\JARVIS    version - 6.3.4\intents\eventsincalender.csv', 'w')
            write = csv.writer(f)
            for i in data:
                write.writerow(i)
            f.close()
        else:
            return

    def clear(self):
        for w in self.wid[:]:
            w.grid_forget()
            self.wid.remove(w)

    def go_prev(self):
        if self.month > 1:
            self.month -= 1
        else:
            self.month = 12
            self.year -= 1

        self.clear()
        self.setup(self.year, self.month)

    def go_next(self):
        if self.month < 12:
            self.month += 1
        else:
            self.month = 1
            self.year += 1

        self.clear()
        self.setup(self.year, self.month)

    def selection(self, day, name):
        self.day_selected = day
        self.month_selected = self.month
        self.year_selected = self.year
        self.day_name = name

        self.clear()
        self.setup(self.year, self.month)

    def setup(self, y, m):

        self.clear()
        lel = tk.Label(self.parent, height=2, bg='black', fg='sky blue', text='    ')
        lel.grid(row=0, column=0)
        left = tk.Button(self.parent, text='<', bg='black', fg='sky blue', font='bold', command=self.go_prev)
        self.wid.append(left)
        left.grid(row=0, column=3)

        header = tk.Label(self.parent, height=2, bg='black', fg='sky blue', font=('Copperplate Gothic Bold', 15),
                          text='{}   {}'.format(calendar.month_name[m].upper(), str(y)))
        self.wid.append(header)
        header.grid(row=0, column=4, columnspan=5)

        right = tk.Button(self.parent, text='>', bg='black', fg='sky blue', font='bold', command=self.go_next)
        self.wid.append(right)
        right.grid(row=0, column=9)

        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        for num, name in enumerate(days):
            t = tk.Label(self.parent, bg='black', fg='sky blue', font=('showcard gothic', 10), text=name[:3])
            self.wid.append(t)
            t.grid(row=1, column=num + 3)

        for w, week in enumerate(self.cal.monthdayscalendar(y, m), 2):
            for d, day in enumerate(week):
                d += 3
                if day:
                    b = tk.Button(self.parent, width=3, foreground='sky blue', background='black', text=day,
                                  font=('arial black', 10, 'bold'),
                                  command=lambda day=day: self.selection(day, calendar.day_name[(day - 1) % 7]))
                    self.wid.append(b)
                    b.grid(row=w, column=d)

        sel = tk.Label(self.parent, height=2, bg='black', fg='sky blue', font=('algerian', 12),
                       text='Today - {} {} {} {}'.format(
                           self.day_name, calendar.month_name[self.month_selected], self.day_selected,
                           self.year_selected))
        self.wid.append(sel)
        sel.grid(row=8, column=1, columnspan=10)

        label_space1 = tk.Label(self.parent, text='', bg='black', fg='sky blue', font=('georgia', 3, 'bold'))
        label_space1.grid(row=9, column=1, columnspan=10)

        label_event_today = tk.Label(self.parent, text='Event Today-', bg='black', fg='sky blue',
                                     font=('MAGNETO', 15, 'underline'))
        label_event_today.grid(row=10, column=1, columnspan=10, sticky='w')
        label_event = tk.Label(self.parent, text=self.event().upper(), bg='black', fg='sky blue',
                               font=('Copperplate Gothic Bold', 13, 'bold'))
        label_event.grid(row=11, column=1, columnspan=10)

        label_space2 = tk.Label(self.parent, text='', bg='black', fg='sky blue', font=('georgia', 3, 'bold'))
        label_space2.grid(row=12, column=1, columnspan=10)

        label_add_event = tk.Label(self.parent, text='Add Event-', bg='black', fg='sky blue',
                                   font=('MAGNETO', 15, 'underline'))  # anchor='w', justify='left')
        label_add_event.grid(row=13, column=1, columnspan=10, sticky='w')

        self.new_event_entry = tk.Entry(self.parent, width=30)
        self.new_event_entry.grid(row=14, column=1, columnspan=10)

        label_space3 = tk.Label(self.parent, text='', bg='black', fg='sky blue', font=('georgia', 5, 'bold'))
        label_space3.grid(row=15, column=1, columnspan=10)

        add_event = tk.Button(self.parent, width=10, text='ADD EVENT', bg='black', fg='sky blue',
                              font=('showcard gothic', 12),
                              command=self.button_pushed)
        add_event.grid(row=16, column=1, columnspan=10)


if __name__ == '__main__':
    child = tk.Tk()
    child.title('Calender')
    child.resizable(0, 0)
    child.iconbitmap('schedule.ico')
    child.geometry('300x500')
    child.configure(background='black')
    cal = Calendar(child)
    child.mainloop()

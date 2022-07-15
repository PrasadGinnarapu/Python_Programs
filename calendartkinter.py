import tkinter as tk
from datetime import datetime
import calendar
window = tk.Tk()
window.title("Calendar")
window.resizable(width=True, height=True)

year = 2022
text_calendar1 = calendar.TextCalendar(calendar.MONDAY).formatmonth(year, 1)
text_calendar2 = calendar.TextCalendar(calendar.MONDAY).formatmonth(year, 2)
text_calendar3 = calendar.TextCalendar(calendar.MONDAY).formatmonth(year, 3)
text_calendar4 = calendar.TextCalendar(calendar.MONDAY).formatmonth(year, 4)
text_calendar5 = calendar.TextCalendar(calendar.MONDAY).formatmonth(year, 5)
text_calendar6 = calendar.TextCalendar(calendar.MONDAY).formatmonth(year, 6)
text_calendar7 = calendar.TextCalendar(calendar.MONDAY).formatmonth(year, 7)
text_calendar8 = calendar.TextCalendar(calendar.MONDAY).formatmonth(year, 8)
text_calendar9 = calendar.TextCalendar(calendar.MONDAY).formatmonth(year, 9)
text_calendar10 = calendar.TextCalendar(calendar.MONDAY).formatmonth(year, 10)
text_calendar11 = calendar.TextCalendar(calendar.MONDAY).formatmonth(year, 11)
text_calendar12 = calendar.TextCalendar(calendar.MONDAY).formatmonth(year, 12)

jan = tk.Label(window, text=text_calendar1, font="TkFixedFont", justify=tk.LEFT, fg="white",
bg="black")
feb = tk.Label(window, text=text_calendar2, font="TkFixedFont", justify=tk.LEFT, fg="white",
bg="black")
march = tk.Label(window, text=text_calendar3, font="TkFixedFont", justify=tk.LEFT, fg="white",
bg="black")
april = tk.Label(window, text=text_calendar4, font="TkFixedFont", justify=tk.LEFT, fg="white",
bg="black")
may = tk.Label(window, text=text_calendar5, font="TkFixedFont", justify=tk.LEFT, fg="white",
bg="black")

june = tk.Label(window, text=text_calendar6, font="TkFixedFont", justify=tk.LEFT, fg="white",
bg="black")

july = tk.Label(window, text=text_calendar7, font="TkFixedFont", justify=tk.LEFT, fg="white",
bg="black")

august = tk.Label(window, text=text_calendar8, font="TkFixedFont", justify=tk.LEFT, fg="white",
bg="black")

september = tk.Label(window, text=text_calendar9, font="TkFixedFont", justify=tk.LEFT, fg="white",
bg="black")

october = tk.Label(window, text=text_calendar10, font="TkFixedFont", justify=tk.LEFT, fg="white",
bg="black")

november = tk.Label(window, text=text_calendar11, font="TkFixedFont", justify=tk.LEFT, fg="white",
bg="black")

december = tk.Label(window, text=text_calendar12, font="TkFixedFont", justify=tk.LEFT, fg="white",
bg="black")


jan.grid(row=0, column=1)
feb.grid(row=0, column=2, padx=10)
march.grid(row=0, column=3, padx=10)
april.grid(row=0, column=4, padx=10)
may.grid(row=1, column=1, padx=10,pady=10)
june.grid(row=1, column=2, padx=10,pady=10)
july.grid(row=1, column=3, padx=10,pady=10)
august.grid(row=1, column=4, padx=10,pady=10)
september.grid(row=2, column=1, padx=10,pady=10)
october.grid(row=2, column=2, padx=10,pady=10)
november.grid(row=2, column=3, padx=10,pady=10)
december.grid(row=2, column=4, padx=10,pady=10)


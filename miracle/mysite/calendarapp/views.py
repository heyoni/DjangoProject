from django.shortcuts import render
import calendar
from calendar import HTMLCalendar


# 해야할것: class로 만들 수 있으면 만들고, s를 html단에 넘겨주기

# Create your views here.
def CalendarView(request, year, month):
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    cal = HTMLCalendar().formatmonth(year, month_number)
    return render(request, 'calendarapp/calendar.html',{
                                            'year': year,
                                            'month': month,
                                            'month_number':month_number,
                                            'cal' : cal,
                                            })

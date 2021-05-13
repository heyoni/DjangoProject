from django.shortcuts import render
import calendar


# 해야할것: class로 만들 수 있으면 만들고, s를 html단에 넘겨주기

# Create your views here.
def CalendarView(request):
    htmlCalendar = calendar.HTMLCalendar(calendar.SUNDAY)
    s = htmlCalendar.formatmonth(2021,5)



    return render(request, 'calendarapp/calendar.html', {'s':s})


# class CalendarView()
# 

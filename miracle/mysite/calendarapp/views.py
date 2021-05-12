from django.shortcuts import render

# Create your views here.
def CalendarView(request):
    import calendar
    c = calendar.TextCalendar(calendar.SUNDAY)
    s = c.formatmonth(2021,5)


    return render(request, 'calendarapp/calendar.html')

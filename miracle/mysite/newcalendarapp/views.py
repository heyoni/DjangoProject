from django.shortcuts import render, redirect, get_object_or_404, reverse
import datetime
from .models import CalendarModel
from routineapp.models import Routine
import calendar
from .calendar import Calendar
from django.utils.safestring import mark_safe
from .forms import CalendarModelForm
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView, ListView



def calendarView(request):
    today = get_date(request.GET.get('month'))
    prev_month_var = prev_month(today)
    next_month_var = next_month(today)

    cal = Calendar(today.year, today.month)
    html_cal = cal.formatmonth(withyear=True)
    result_cal = mark_safe(html_cal+'</table>')

    context = {'calendar' : result_cal, 'prev_month' : prev_month_var, 'next_month' : next_month_var}

    return render(request, 'calendarapp/calendar.html', context)

#현재 달력을 보고 있는 시점의 시간을 반환
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime.date(year, month, day=1)
    return datetime.datetime.today()

#현재 달력의 이전 달 URL 반환
def prev_month(day):
    first = day.replace(day=1)
    prev_month = first - datetime.timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

#현재 달력의 다음 달 URL 반환
def next_month(day):
    days_in_month = calendar.monthrange(day.year, day.month)[1]
    last = day.replace(day=days_in_month)
    next_month = last + datetime.timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

#새로운 Event의 등록 혹은 수정
def event(request, event_id=None):
    if event_id:
        instance = get_object_or_404(CalendarModel, pk=event_id)
    else:
        instance = CalendarModel()
    
    # 루틴이 있는지 확인
    isRoutinein = Routine.objects.filter
    
    form = CalendarModelForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return redirect('/calendar/')
    return render(request, 'calendarapp/input.html', {'form': form, 'isRoutinein':isRoutinein, 'pk':event_id})

    
class calendarDeleteView(DeleteView):
    model = CalendarModel
    context_object_name = 'target_calendar'
    template_name = 'calendarapp/delete.html'
    success_url = reverse_lazy('calendarapp:calendar')


# class calendarUpdateView(UpdateView):
#     model = CalendarModel
#     context_object_name = 'target_calendar'
#     template_name = 'calendarapp/update.html'


#     def get_success_url(self):
#         return reverse('calendarapp:detail',kwargs={'pk':self.object.pk})
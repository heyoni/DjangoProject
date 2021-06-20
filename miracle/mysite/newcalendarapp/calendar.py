from .models import CalendarModel
from calendar import HTMLCalendar, day_abbr, month_name
import inspect


class ArrowCalendar(HTMLCalendar):
    def __init__(self, firstweekday):
        HTMLCalendar.__init__(self, firstweekday)

    def formatmonthname(year, month, withyear=True):
        if withyear:
            s = '%s %s' % (month_name[month], year)
        else:
            s = '%s' % month_name[month]
        return f'<th colspan="7" class="month text-center font-weight-bolder">%s</th>' %s



class Calendar(HTMLCalendar):
	count = 0

	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()
		self.count = 0

	# '일'을 td 태그로 변환하고 이벤트를 '일'순으로 필터
	def formatday(self, day, events):
		self.count += 1
		events_per_day = events.filter(start_time__day=day)
		d = ''

		# color 색 순서 정해주기 
		for event in events_per_day:
			print(event)
			if str(event).split(',')[1] == 'red':
				d += f'<li style="display:flex;order:1;"> {event.get_html_url} </li>'
			elif str(event).split(',')[1] == 'orange':
				d += f'<li style="display:flex;order:2;"> {event.get_html_url} </li>'
			elif str(event).split(',')[1] == 'yellow':
				d += f'<li style="display:flex;order:3;"> {event.get_html_url} </li>'
			elif str(event).split(',')[1] == 'green':
				d += f'<li style="display:flex;order:4;"> {event.get_html_url} </li>'
			elif str(event).split(',')[1] == 'blue':
				d += f'<li style="display:flex;order:5;"> {event.get_html_url} </li>'
			elif str(event).split(',')[1] == 'navy':
				d += f'<li style="display:flex;order:6;"> {event.get_html_url} </li>'
			elif str(event).split(',')[1] == 'purple':
				d += f'<li style="display:flex;order:7;"> {event.get_html_url} </li>'
			elif str(event).split(',')[1] == 'black':
				d += f'<li style="display:flex;order:8;"> {event.get_html_url} </li>'


		if day != 0:
			# 토, 일요일 색 바꿔주기
			if self.count % 7 == 6:
				return f"<td class='container col-1'><span style='color:blue'>{day}</span><ul class='event_line' style='display:flex;flex-wrap: wrap;'> {d} </ul></td>"
			elif self.count % 7 == 0:
				return f"<td class='container col-1'><span style='color:red'>{day}</span><ul class='event_line' style='display:flex;flex-wrap: wrap;'> {d} </ul></td>"
			else:
				return f"<td class='container col-1'><span>{day}</span><ul class='event_line' style='display:flex;flex-wrap: wrap;'> {d} </ul></td>"

		return '<td></td>'

	def formatweekheader(self):
		s = ''.join(self.formatweekday(i) for i in self.iterweekdays())

		return '<tr style="text-align:center; font-weight:bold">%s</tr>' % s


	# '주'를 tr 태그로 변환
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr class="week" style="height:140px"> {week} </tr>'

	# '월'을 테이블 태그로 변환
	# 각 '월'과 '연'으로 이벤트 필터
	def formatmonth(self, withyear=True):
		events = CalendarModel.objects.filter(start_time__year=self.year, start_time__month=self.month)

		cal = f'<table class="table table-bordered container">\n'
		cal += f'{ArrowCalendar.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		# print(inspect.getsource(self.formatweekday))
		# print(cal)

		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal


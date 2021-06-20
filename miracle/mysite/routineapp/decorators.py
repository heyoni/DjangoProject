from django.http import HttpResponseForbidden
from routineapp.models import Routine

def routine_ownership_required(func):
    def decorated(request, *args, **kwargs):
        routine = Routine.objects.get(pk=kwargs['pk'])

        # 실행하면 writer가 없다고 에러남 ->로그인으로 바꿀까?
        if not routine.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated
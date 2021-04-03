from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

# 사용자가 맞는지 확인하고 접근가능한 정보를 보여줌
def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if not user == request.user:
            return HttpResponseForbidden()

    return decorated
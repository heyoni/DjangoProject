from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'modify_dt')
    # 필터 사이드바 넣기 : modify_dt 컬럼을 사용하는 것을 보여줌
    list_filter = ('modify_dt',)
    search_fields = ('title', 'content')
    # slug는 title을 이용하여 미리 채워지도록 해줌.
    prepopulated_fields = {'slug':('title',)}

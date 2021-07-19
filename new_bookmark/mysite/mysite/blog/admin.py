from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # taggablemanager 클래스는 list_display에 직접 등록할수 없어서 메서드를 이용하여 등록해줌 -> tag_list 메서드가 맨 아래에 있음다
    list_display = ('id', 'title', 'modify_dt', 'tag_list')
    # 필터 사이드바 넣기 : modify_dt 컬럼을 사용하는 것을 보여줌
    list_filter = ('modify_dt',)
    search_fields = ('title', 'content')
    # slug는 title을 이용하여 미리 채워지도록 해줌.
    prepopulated_fields = {'slug':('title',)}

    # post 레코드 리스트를 가져온다.
    # post와 tag는 many to many 관계이므로 tag테이블의 관련 레코드를 한 번의 쿼리로 미리 가져옴 -> 쿼리를 줄이는 방법은 prefetch_related를 사용한다.
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    # 태그의 값들을 연결하여 보여줌
    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())

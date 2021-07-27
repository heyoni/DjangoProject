from django.contrib import admin
from photo.models import Album, Photo

# StackedInline은 세로형식으로 보여줌 가로는 TabularInline
class PhotoInline(admin.StackedInline):
    # 추가로 보여주는 필드는 photo
    model = Photo
    # 이미 존재하는 객체 외에 추가로 입력할 수 있는 Photo 테이블 객체의 수는 2개
    extra = 2


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    # 앨범 객체 수정 화면을 보여줄 때 PhotoInline 클래스에서 정의해준 내용을 같이 보여줌
    inlines = (PhotoInline,)
    list_display = ('id','name','description')


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id','title','upload_dt')
    

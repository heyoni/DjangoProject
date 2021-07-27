# 커스텀 필드 : 장고의 기본 필드 외에 사용자가 직접 작성하여 만드는 필드
# 파일명은 마음대로 지어도 됨.
# 여기서는 ImageField 클래스를 상속받아 작성함
import os
from PIL import Image
from django.db.models.fields.files import ImageField, ImageFieldFile


class ThumbnailImageFieldFile(ImageFieldFile):
    # 썸네일 이미지 파일명 만들어주기
    def _add_thumb(self, s):
        parts = s.split('.')
        parts.insert(-1, 'thumb')
        if parts[-1].lower() not in ('jpeg', 'jpg'):
            parts[-1] = 'jpg'
        return '.'.join(parts)

    # 이미지를 처리하는 경로 제공하기
    @property
    def thumb_path(self):
        return self._add_thumb(self.path)

    # 이미지를 처리하는 url 속성 제공하기
    @property
    def thumb_url(self):
        return self._add_thumb(self.url)

    # 파일 시스템에 파일을 저장하고 생성하는 메서드
    def save(self, name, content, save=True):
        # 원본이미지 저장하기(부모 클래스의 save 메서드 이용)
        super().save(name, content, save)

        img = Image.open(self.path)
        # 사이즈 지정해주기
        size = (self.field.thumb_width, self.field.thumb_height)
        img.thumbnail(size)
        # 썸네일 뒷배경 만들어주기 : 만들고 합침
        background = Image.new('RGB', size, (255, 255, 255))
        box = (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2 ))
        background.paste(img, box)
        # thumb_path에 원본 이미지 저장해줌
        background.save(self.thumb_path, 'JPEG')

    # 삭제시 원본이미지와 썸네일까지 삭제
    def delete(self, save=True):
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super().delete(save)


class ThumbnailImageField(ImageField):
    # 새로운 filefield 클래스를 정의할 때는 그에 상응하는 file 처리 클래스를 attr_class에 지정해줘야함
    attr_class = ThumbnailImageFieldFile

    def __init__(self, verdose_name=None, thumb_width=128, thumb_height=128, **kwargs):
        self.thumb_width, self.thumb_height = thumb_width, thumb_height
        super().__init__(verdose_name, **kwargs)
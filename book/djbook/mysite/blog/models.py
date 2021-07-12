from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    # 제목의 별칭, 폼화면에서 레이블로 사용되는 문구
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text')
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE',auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE',auto_now=True)


    # 필드속성 이외에 필요한 파라미터가 있을 경우 meta 내부 클래스로 정의한다.
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        # 이 항목을 지정하지 않으면 테이블명은 blog_post가 됨(앱명_모델클래스명)
        db_table = 'blog_posts'
        # 내림차순을 정렬한다.
        ordering = ('-modify_dt',)


    def __str__(self):
        return self.title

    # 이 메소드가 정의된 객체를 지칭하는 URL반환
    def get_absolute_url(self):
        return reverse('blog:post_detail',args=(self.slug,))

    def get_previous(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()
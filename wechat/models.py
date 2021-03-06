from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class WechatUser(models.Model):
    openid = models.CharField(max_length=50, default='')
    unionid = models.CharField(max_length=50, default='')
    name = models.CharField(max_length=50, default='')
    owner = models.ForeignKey('auth.User', related_name='wechatuser', on_delete=models.CASCADE)
    highlighted = models.TextField()
    title = models.CharField(max_length=100, blank=True, default='')
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    code = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(WechatUser, self).save(*args, **kwargs)


class Comment(models.Model):
    email = models.EmailField(max_length=50, default='')
    content = models.CharField(max_length=100, default='')
    created = models.DateTimeField(auto_now_add=True)

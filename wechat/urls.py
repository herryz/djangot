from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from wechat import views

import views

urlpatterns = [
    url(r'^wechats/$', views.WechatList.as_view()),
    url(r'^wechats/(?P<pk>[0-9]+)/$', views.WechatDetail.as_view()),

    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
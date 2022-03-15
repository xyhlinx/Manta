from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import re_path, include
from member.views import TagList, MemberDetail, UserList


app_name = 'member'

urlpatterns = [
    re_path(r'^tag/$', TagList.as_view(), name='tag_list'),
    re_path(r'^$', UserList.as_view(), name='user_list'),
    re_path(r'^tag/(?P<pk>[^/]+)/$', MemberDetail.as_view(), name='member_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

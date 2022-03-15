from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import re_path
from member.views import TagListCreate, TagDetail, UserList, GroupList


app_name = 'member'

urlpatterns = [
    re_path(r'^tag/$', TagListCreate.as_view(), name='tag_list_create'),
    re_path(r'^$', UserList.as_view(), name='user_list'),
    re_path(r'^group/$', GroupList.as_view(), name='group_list'),
    re_path(r'^tag/(?P<pk>[^/]+)/$', TagDetail.as_view(), name='tag_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

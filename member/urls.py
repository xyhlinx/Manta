from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import re_path, include
from member.views import MemberList


app_name = 'member'

urlpatterns = [
    re_path(r'^$', MemberList.as_view(), name='member_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

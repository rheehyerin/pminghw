from django.conf import settings
from django.conf.urls import url
from posting_hw import views

app_name = "posting"
urlpatterns = [
    url(r'^post_list/$', views.post_list, name='post_list'),
    url(r'^post_detail/(?P<pk>\d+)$', views.post_detail, name='post_detail'),
    url(r'^post_write/$', views.post_write, name='post_write'),
]
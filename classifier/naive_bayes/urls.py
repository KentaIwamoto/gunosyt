from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.hello_world, name='hello_world'),
    # url(r'^template/$', views.hello_template, name='hello_template'),  # 追加する
    # url(r'^if/$', views.hello_if, name='hello_if'), # 追加する
    # url(r'^get/$', views.hello_get_query, name='hello_get_query'), # 追加する
    # url(r'^time/$',views.time, name='time'),
    url(r'^result/$',views.result, name='result'),
    url(r'^$',views.urlform, name='urlform'),

]

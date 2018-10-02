from django.conf.urls import url
from . import views


urlpatterns= [
    url(r'^$', views.review_list, name = 'review_list'),
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name = 'review_detail'),
    url(r'^wine$', views.wine_list, name = 'wine_list'),
    url(r'^wine/(?P<wine_id>[0-9]+)$', views.wine_detail, name
        ='wine_detail'),
]
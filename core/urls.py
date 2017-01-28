from django.conf.urls import url

from core import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.PostingDetailView.as_view(), name='detail'),
    url(r'^create/$', views.PostingCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/update/$', views.PostingUpdateView.as_view(),
        name='update'),
]

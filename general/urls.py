from django.conf.urls import url

from general.views import SearchView

urlpatterns = [
    url(r'^search/$', SearchView.as_view(), name='search'),
]

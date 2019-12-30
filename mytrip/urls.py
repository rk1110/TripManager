from mytrip.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
	url(r'^home/$', home),
	url(r'^login/$', login),
	url(r'^auth/$', auth_view),
	url(r'^create/$', create),
	url(r'^logout/$', logout),
	url(r'^signup/$', signup),
	url(r'^event/$', event),
]
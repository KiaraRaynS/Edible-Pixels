from django.conf.urls import url
from django.contrib import admin
from appcatcafe.views import IndexView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='indexview'),
]

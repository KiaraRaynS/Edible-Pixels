from django.conf.urls import url
from django.contrib import admin
from appcatcafe.views import IndexView
# Drinks
from appcatcafe.views import CatuccinoView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='indexview'),
    url(r'^drinks/catuccino/$', CatuccinoView.as_view(), name='catuccinoview'),
]

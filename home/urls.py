from django.conf.url import url
from home import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]

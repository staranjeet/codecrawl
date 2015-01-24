from django.conf.urls import patterns,url
from codecal import views

urlpatterns = patterns('codecal.views',
    (r'^$', 'index'),
  
)
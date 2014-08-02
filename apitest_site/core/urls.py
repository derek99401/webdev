from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^test$', views.TestView.as_view()),
    url(r'^upload$', views.FileUploadView.as_view()),
)

from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('makeanorder', views.MakeAnOrderView.as_view(), name='makeanorder_page'),
    path('makeanorder/thanks', views.ThanksView.as_view(), name='thanks_page'),
    path('about', views.AboutView.as_view(), name='about_page'),
]

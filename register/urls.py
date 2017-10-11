from django.conf.urls import url
from register import views

app_name = 'register'
urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.user_login,name='user_login'),
    url(r'^userpage/$',views.view,name='userpage'),
]

from django.conf.urls import include,url
from django.contrib import admin
from TechSprinkle import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^logout/', views.logout_user, name='logout'),
    url(r'^authenticate/',views.authenticateUser,name='authenticate'),
    url(r'^blog/',include('BlogPost.urls')),
    url(r'^$', views.loginPage, name='login'),
    # url(r'^.*', views.handle404, name = 'handle404'),
]

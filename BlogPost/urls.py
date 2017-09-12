from django.conf.urls import url
from BlogPost import views

urlpatterns = [
    url(r'^list/',views.home,name='home'),
    url(r'^getPosts/', views.getPosts, name='getPosts'),
    url(r'^savePost/',views.savePost,name='savePost'),
    url(r'^editPost/',views.editPost,name='editPost'),
    # url(r'^addComment/',views.addComment,name='addComment'),
    url(r'^deletePost/', views.deletePost, name='deletePost'),

]

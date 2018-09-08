from django.conf.urls import url, include
from . import views

urlpatterns= [
    url(r'^games/sadari/$', views.enter_sadari, name='enter_sadari'),
    url(r'^etc/community/$', views.enter_community, name='enter_community'),
    url(r'^etc/community/post/(?P<pk>\d+)/$', views.community_post_detail, name='community_post_detail'),
    url(r'^etc/community/post/new/$', views.community_post_new, name='community_post_new'),
    url(r'^etc/community/post/(?P<pk>\d+)/edit/$', views.community_post_edit, name='community_post_edit'),



    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^member_info/$', views.member_info, name='member_info'),

    #url(r'^member_info_edit/$', views.member_info, name='member_info'),
    url(r'^$', views.Login, name='login'),
    url(r'^post/$', views.post_new, name='post_new'),
    url(r'^home/$', views.home, name='home'),

    url(r'^my_profile', views.my_profile, name='my_profile'),
    url(r'^profile/(?P<pk>\d+)/$', views.profile, name='profile'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^following/(?P<pk>\d+)/$', views.following, name='following'),
    url(r'^member_info_edit/(?P<pk>\d+)/$', views.member_info_edit, name='member_info_edit'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^friends_recommend/$', views.friends_recommend, name='friends_recommend'),


    #url(r'^following/$', views.following, name='following'),
        ]

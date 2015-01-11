from django.conf.urls import patterns, url
from app import views

urlpatterns = patterns('',
	url('^$', views.home_page),
	url('^login/', views.login_page),
	url('^verify/', views.verify),
	url('^logout/', views.logout_page),

	url('^edit/', views.edit_page),
	url('^bookmark_up/(?P<bookmark_id>\d+)', views.bookmark_up),
	url('^bookmark_down/(?P<bookmark_id>\d+)', views.bookmark_down),
	url('^random_glyphicon/(?P<bookmark_id>\d+)', views.random_glyphicon),

	url('^category_up/(?P<category_id>\d+)', views.category_up),
	url('^category_down/(?P<category_id>\d+)', views.category_down),
	url('^category_left/(?P<category_id>\d+)', views.category_left),
	url('^category_right/(?P<category_id>\d+)', views.category_right),
	
	url('^random_color/(?P<category_id>\d+)', views.random_color),
	)
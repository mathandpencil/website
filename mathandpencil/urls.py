from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = patterns('',
	(r'^blog/', 			include('apps.blog.urls')),
	(r'^uploads', 			include('apps.uploads.urls')),
	
	url(r'^$', 								'apps.static.views.index',			name='index'),
	url(r'^about$', 						'apps.static.views.about',			name='about'),
	url(r'^blog$', 							'apps.static.views.blog',			name='blog'),
	url(r'^capabilities$',				 	'apps.static.views.capabilities',	name='capabilities'),
	url(r'^clients$',				 		'apps.static.views.clients',		name='clients'),
	url(r'^contact$', 						'apps.static.views.contact',		name='contact'),
	url(r'^login$', 						'apps.static.views.login',			name='login'),
	url(r'^projects$', 						'apps.static.views.projects',		name='projects'),
	url(r'^team$', 							'apps.static.views.team',			name='team'),
	url(r'^test$', 							'apps.static.views.test',			name='test'),
	
	url(r'^projects/fetcher$', 				'apps.static.views.projects_4',		name='projects_4'),
	url(r'^projects/dukemail$', 			'apps.static.views.projects_3',		name='projects_3'),
	url(r'^projects/employii$', 			'apps.static.views.projects_2',		name='projects_2'),
	url(r'^projects/socialq$', 				'apps.static.views.projects_1',		name='projects_1'),
	
	url(r'^branding/business-cards$', 		'apps.static.views.branding_1',		name='branding_1'),
	url(r'^branding/identity-packages$',	'apps.static.views.branding_2',		name='branding_2'),
	
	(r'^demo/',								include('apps.demo.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
    )
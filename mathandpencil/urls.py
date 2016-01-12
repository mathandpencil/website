from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = patterns('',
	
	url(r'^$', 								'apps.core.views.index',			name='index'),
	url(r'^about$', 						'apps.core.views.about',			name='about'),
	url(r'^capabilities$',				 	'apps.core.views.capabilities',	name='capabilities'),
	url(r'^clients$',				 		'apps.core.views.clients',		name='clients'),
	url(r'^contact$', 						'apps.core.views.contact',		name='contact'),
	url(r'^projects$', 						'apps.core.views.projects',		name='projects'),
	url(r'^team$', 							'apps.core.views.team',			name='team'),
	url(r'^test$', 							'apps.core.views.test',			name='test'),
	
	url(r'^projects/fetcher$', 				'apps.core.views.projects_4',		name='projects_4'),
	url(r'^projects/dukemail$', 			'apps.core.views.projects_3',		name='projects_3'),
	url(r'^projects/employii$', 			'apps.core.views.projects_2',		name='projects_2'),
	url(r'^projects/socialq$', 				'apps.core.views.projects_1',		name='projects_1'),
	
	url(r'^branding/business-cards$', 		'apps.core.views.branding_1',		name='branding_1'),
	url(r'^branding/identity-packages$',	'apps.core.views.branding_2',		name='branding_2'),
	)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^core/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
    )
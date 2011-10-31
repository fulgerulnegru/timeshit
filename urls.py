from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'timeshit.controllers.users.dashboard', name='ts__dashboard'),

    url(r'^about/$', 'timeshit.controllers.users.about', name='ts__about'),
    url(r'^clients/$', 'timeshit.controllers.clients.index', name='ts__clients'),
    url(r'^clients/new/$', 'timeshit.controllers.clients.new', name='ts__new_client'),
    url(r'^clients/create/$', 'timeshit.controllers.clients.create', name='ts__create_client'),
    url(r'^clients/(?P<client_id>\d+)/$', 'timeshit.controllers.clients.show', name='ts__show_client'),
    url(r'^clients/(?P<client_id>\d+)/edit/$', 'timeshit.controllers.clients.edit', name='ts__edit_client'),
    url(r'^clients/(?P<client_id>\d+)/update/$', 'timeshit.controllers.clients.update', name='ts__update_client'),
    url(r'^clients/(?P<client_id>\d+)/delete/$', 'timeshit.controllers.clients.delete', name='ts__delete_client'),
 
    url(r'^projects/$', 'timeshit.controllers.projects.index', name='ts__projects'),
    url(r'^projects/new/$', 'timeshit.controllers.projects.new', name='ts__new_project'),
    url(r'^projects/create/$', 'timeshit.controllers.projects.create', name='ts__create_project'),
    url(r'^projects/(?P<project_id>\d+)/$', 'timeshit.controllers.projects.show', name='ts__show_project'),
    url(r'^projects/(?P<project_id>\d+)/edit/$', 'timeshit.controllers.projects.edit', name='ts__edit_project'),
    url(r'^projects/(?P<project_id>\d+)/update/$', 'timeshit.controllers.projects.update', name='ts__update_project'),
    url(r'^projects/(?P<project_id>\d+)/delete/$', 'timeshit.controllers.projects.delete', name='ts__delete_project'),
 
    url(r'^tasks/$', 'timeshit.controllers.tasks.index', name='ts__tasks'),
    url(r'^tasks/new/$', 'timeshit.controllers.tasks.new', name='ts__new_task'),
    url(r'^tasks/create/$', 'timeshit.controllers.tasks.create', name='ts__create_task'),
    url(r'^tasks/(?P<task_id>\d+)/$', 'timeshit.controllers.tasks.show', name='ts__show_task'),
    url(r'^tasks/(?P<task_id>\d+)/edit/$', 'timeshit.controllers.tasks.edit', name='ts__edit_task'),
    url(r'^tasks/(?P<task_id>\d+)/update/$', 'timeshit.controllers.tasks.update', name='ts__update_task'),
    url(r'^tasks/(?P<task_id>\d+)/delete/$', 'timeshit.controllers.tasks.delete', name='ts__delete_task'),
 
    url(r'^records/start/', 'timeshit.controllers.records.start', name='ts__start'),
    url(r'^records/stop/', 'timeshit.controllers.records.stop', name='ts__stop'),

    url(r'^auth/register/$', 'timeshit.controllers.users.register', name='register'),
    url(r'^auth/login/$', 'timeshit.controllers.users.login', name='login'),
    url(r'^auth/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
)

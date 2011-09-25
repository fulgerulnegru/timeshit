from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'timeshit.controllers.users.dashboard', name='ts__dashboard'),

    url(r'^clients/$', 'timeshit.controllers.clients.index', name='ts__clients'),
    url(r'^clients/new/$', 'timeshit.controllers.clients.new', name='ts__new_client'),
    url(r'^clients/(?P<client_id>\d+)/$', 'timeshit.controllers.clients.show', name='ts__show_client'),
    url(r'^clients/(?P<client_id>\d+)/edit/$', 'timeshit.controllers.clients.edit', name='ts__edit_client'),
    url(r'^clients/(?P<client_id>\d+)/delete/$', 'timeshit.controllers.clients.delete', name='ts__delete_client'),

    url(r'^auth/login/$', 'timeshit.controllers.users.login', name='login'),
    url(r'^auth/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
)

from django.conf.urls import url, include
from project import views

urlpatterns = [
    url(r'^new_project', views.new_project, name='new_project'),
    url(r'^(?P<pk>\w{8}-\w{4}-\w{4}-\w{4}-\w{12})', views.project_detail, name='project_detail'),
    # url(r'^(?P<pk>\w{8}-\w{4}-\w{4}-\w{4}-\w{12})/device', include('device.urls')),
    url(r'', views.project, name='project'),
]
from django.conf.urls import url, include
from device import views

urlpatterns = [
    url(r'^new_device', views.new_device, name='new_device'),
    url(r'^(?P<pk>\w{8}-\w{4}-\w{4}-\w{4}-\w{12})', views.device_detail, name='device_detail'),
    # url(r'^(?P<pk>\w{8}-\w{4}-\w{4}-\w{4}-\w{12})/device', include('device.urls')),
    url(r'', views.device, name='device'),
]
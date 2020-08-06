from django.urls import path, include
from .views import service_list, service_detals, add_service
from contact.views import send_massage
from .api import service_provider_api , ServiceProviderDetail, ServiceDetail, service_provider_api_id

app_name = 'serviceProvider'

urlpatterns = [
    path('', service_list, name='sercive_list'),
    path('<int:id>', service_detals, name='service_detail'),
    path('add', add_service, name='add_service'),
    path('contact', send_massage, name='contact'),

    # api
    path('api/list', service_provider_api, name='api'),
    path('api/list/<int:id>', service_provider_api_id, name='api_service_detail'),

    ## class Based view
    path('api/v2/list', ServiceProviderDetail.as_view(), name='classBased'),
    path('api/v2/list/<int:id>', ServiceDetail.as_view(), name='class'),

]
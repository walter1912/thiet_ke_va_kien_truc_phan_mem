from django.urls import path, include
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'users', UserList)
# router.register(r'users/(?P<pk>\d+)', UserDetail)

urlpatterns = [
    # path('', include(router.urls)),
    path('', views.UserList.as_view(),name='user-list'),
    path('<int:pk>', views.UserDetail.as_view(),name='user-detail'),

]

from django.conf.urls import url,include
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
router=DefaultRouter()
router.register('Student-Details',views.StudViewSet,base_name='students')
urlpatterns=[
    path('',include(router.urls))
]
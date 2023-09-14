from django.urls import path
from website import views

urlpatterns = [
    path('' , views.home , name = 'home'),
    path('logout/',views.logout_user , name='logout'),
    path('register/', views.register_user , name='register'),
    path('recordData/',views.record_data , name='record_data'),
    path('update_record/<uuid:pk>', views.update_record , name='update_record'),
    path('delete_record/<uuid:pk>', views.delete_data , name='delete_record')
]

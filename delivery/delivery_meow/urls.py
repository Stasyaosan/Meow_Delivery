from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('reg', reg),
    path('suc/<str:token>', suc_user),
    path('logout', logout),
    path('update', update),
    path('ajax_load_address', ajax_load_address),
    path('add_order', add_order),
]

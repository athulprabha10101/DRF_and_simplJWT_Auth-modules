from django.urls import path
from .views import *

urlpatterns = [
    # path('',home),
    # path('post_student/', post_student),
    # path('update_student/<int:id>/', update_student),
    # path('modify_student/<int:id>/', modify_student),
    # path('get_book/', get_book),
    path('student/',StudentAPI.as_view()),
    path('register/', Registeruser.as_view())
]

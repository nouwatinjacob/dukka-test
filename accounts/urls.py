from django.urls import path, include
from .views import RegisterView, LoginView, LogoutView

api = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

urlpatterns = [
    path('api/v1/', include(api)),
]
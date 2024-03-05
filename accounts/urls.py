from django.urls import path, include
from .views import RegisterView, LoginView, LogoutView, UserRetrieve
from rest_framework_simplejwt import views as jwt_views

api = [
    path('account/', UserRetrieve.as_view(), name='user_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ="token_obtain_pair"),
]

urlpatterns = [
    path('api/v1/', include(api)),
]
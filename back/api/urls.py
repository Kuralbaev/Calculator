from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from api.controller.ArithmeticController import ArithmeticController

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('arithmetic', ArithmeticController.as_view(), name='ArithmeticController')
]

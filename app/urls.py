from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from companies import views as views_companies

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token-auth/', obtain_jwt_token),
    path('token-refresh/', refresh_jwt_token),
    path('token-verify/', verify_jwt_token),
    path('companies/', views_companies.CompanyListAPIView.as_view(), name='companies-list'),
]

from django.urls import path, include, re_path
from dj_rest_auth.registration.views import ConfirmEmailView, VerifyEmailView
from django.http import HttpResponse

urlpatterns = [
    path(
        'registration/account-confirm-email/<str:key>/',
        ConfirmEmailView.as_view(),
    ),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path("", include("dj_rest_auth.urls")),
    
]
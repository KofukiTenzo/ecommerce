from django.urls import path, include, re_path
from allauth.account.views import ConfirmEmailView

urlpatterns = [
    re_path(
        "registration/account-confirm-email/(?P<key>[-:\w]+)/$",
        ConfirmEmailView.as_view(),
        name="account_confirm_email",
    ),
    
    path("", include("dj_rest_auth.urls")),
    path('registration/', include('dj_rest_auth.registration.urls'))
]
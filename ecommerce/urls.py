from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('products/', include('products.urls')),
    path('users/', include('users.urls')),
    
    path('admin/', admin.site.urls),
    # path("users/auth/", include("dj_rest_auth.urls")),
    # path('users/auth/registration/', include('dj_rest_auth.registration.urls'))
]

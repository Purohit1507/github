from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: HttpResponseRedirect('/fc/order/')),  # Redirect root to the order page
    path('fc/', include('FC.urls')),
]

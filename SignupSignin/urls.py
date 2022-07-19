from django.urls import include, path

urlpatterns = [
    path('', include('server.urls')),
    path('register/', include('server.urls')),
    path('login/', include('server.urls')),
    path('admin/', include('server.urls')),
    path('logout/', include('server.urls'))
]
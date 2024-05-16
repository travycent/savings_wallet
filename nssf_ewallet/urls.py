"""
URL configuration for nssf_ewallet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    #Profiles APIs
    path('api/', include('profiles.urls')),
    #Savings APIs
    path('api/', include('saving.urls')),
    ## API DOCS
    # Download API DOC YML
    path('api/docs/', SpectacularAPIView.as_view(), name='schema'),
    # UI view for DOC:
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui')

]
#A function to change the default Text in the DJango Admin Portal
def change_admin_default_settings():
    admin.site.site_header = 'YolloSave Portal'# default: "Django Administration"
    admin.site.index_title = 'Features area'   # default: "Site administration"
    admin.site.site_title = 'YolloSave Portal' # default: "Django site admin"
change_admin_default_settings()

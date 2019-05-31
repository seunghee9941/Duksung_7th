"""dsWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
import apply.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addetail/<int:apply_id>/', apply.views.addetail, name="addetail"),
    path('form/', apply.views.form, name='form'), # 지원하기
    path('adview/', apply.views.adview, name='adview'),
    path('form/save/', apply.views.save, name='save'),
    path('form/submit/', apply.views.submit, name='submit'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from python_lessons.views import UserFormView, index, LogUser
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^python_lessons/', include('python_lessons.urls')),
    url(r'^registration/$', UserFormView.as_view(), name='registration'),
    url(r'^login/$', LogUser.as_view(), name='login'),
    url(r'^$', index, name='index')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

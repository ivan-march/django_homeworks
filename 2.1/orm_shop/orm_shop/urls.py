from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from main.views import cars_list_view, car_details_view, sales_by_car


urlpatterns = [
    path('', RedirectView.as_view(url='/cars/'), name='index'),
    path('admin/', admin.site.urls),
    path('cars/', cars_list_view, name='list'),
    path('cars/<int:car_id>/', car_details_view, name='details'),
    path('cars/<int:car_id>/sales/', sales_by_car, name='sales')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

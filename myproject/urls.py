from django.contrib import admin
from django.urls import path, include
from task1 import views  # Импорт представлений из task1

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка
    path('', views.main_page, name='home'),  # Главная страница
    path('platform/', include([
        path('', views.main_page, name='main'),  # Главная страница платформы
        path('store/', views.store_page, name='store'),  # Магазин
        path('cart/', views.cart_page, name='cart'),  # Корзина
        path('news/', views.news_view, name='news'),  # Добавляем путь для новостей
    ])),
    path('signup/html/', views.sign_up_by_html, name='sign_up_by_html'),  # Регистрация через HTML формы
    path('signup/django/', views.sign_up_by_django, name='sign_up_by_django'),  # Регистрация через Django формы
]


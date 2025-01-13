from django.shortcuts import render
from .models import Game  # Подключаем модель Game
from .forms import UserRegister
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import News

# Главная страница
def main_page(request):
    return render(request, 'fourth_task/main.html')

# Магазин
def store_page(request):
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    context = {'games': games}
    return render(request, 'fourth_task/store.html', context)

# Корзина
def cart_page(request):
    return render(request, 'fourth_task/cart.html')

# Список уже существующих пользователей
users = ["Vasya", "Petya", "Masha"]


def sign_up_by_django(request):
    info = {}  # Контекст для шаблона
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # Проверка на существующего пользователя
            existing_users = Buyer.objects.all()  # QuerySet всех пользователей
            if any(user.name == username for user in existing_users):
                info['error'] = "Пользователь уже существует"
            elif password != repeat_password:
                info['error'] = "Пароли не совпадают"
            elif age < 18:
                info['error'] = "Вы должны быть старше 18"
            else:
                # Добавление пользователя в базу данных
                Buyer.objects.create(name=username, age=age, password=password)
                return render(
                    request,
                    'fifth_task/registration_page.html',
                    {'message': f"Приветствуем, {username}!"}
                )
        else:
            info['error'] = "Проверьте корректность данных"
    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if username in users:
            info['error'] = "Пользователь уже существует"
        elif password != repeat_password:
            info['error'] = "Пароли не совпадают"
        elif int(age) < 18:
            info['error'] = "Вы должны быть старше 18"
        else:
            users.append(username)
            return render(request, 'fifth_task/registration_page.html', {'message': f"Приветствуем, {username}!"})

    return render(request, 'fifth_task/registration_page.html', info)


def store_page(request):
    # QuerySet для получения всех записей из таблицы Game
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'fourth_task/store.html', context)


def news_view(request):
    news_list = News.objects.all().order_by('-date')  # Сортируем по дате (сначала новые)
    paginator = Paginator(news_list, 5)  # Показ 5 новостей на странице

    page_number = request.GET.get('page')  # Получаем номер текущей страницы из параметров запроса
    news = paginator.get_page(page_number)  # Получаем страницу

    context = {'news': news}
    return render(request, 'news.html', context)
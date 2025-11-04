from articles.models import Article
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


def archive(request):
    return render(request, "archive.html", {"posts": Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, "article.html", {"post": post})
    except Article.DoesNotExist:
        raise Http404


def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {"text": request.POST["text"], "title": request.POST["title"]}
            # в словаре form будет храниться информация, введенная пользователем
            if form["text"] and form["title"]:
                # проверка на уникальность названия
                if Article.objects.filter(title=form["title"]).exists():
                    form["errors"] = "Статья с таким названием уже существует"
                    return render(request, "create_post.html", {"form": form})

                # если поля заполнены без ошибок и название уникально
                article = Article.objects.create(
                    text=form["text"], title=form["title"], author=request.user
                )
                return redirect("get_article", article_id=article.id)
            else:
                # если введенные данные некорректны
                form["errors"] = "Не все поля заполнены"
                return render(request, "create_post.html", {"form": form})
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, "create_post.html", {})
    else:
        raise Http404


def register(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()
        password_confirm = request.POST.get("password_confirm", "").strip()

        # Проверка на пустые поля
        if not username or not email or not password or not password_confirm:
            error_message = "Все поля должны быть заполнены"
            return render(
                request,
                "register.html",
                {"error": error_message, "username": username, "email": email},
            )

        # Проверка на совпадение паролей
        if password != password_confirm:
            error_message = "Пароли не совпадают"
            return render(
                request,
                "register.html",
                {"error": error_message, "username": username, "email": email},
            )

        # Проверка уникальности имени пользователя
        try:
            User.objects.get(username=username)
            error_message = "Пользователь с таким именем уже существует"
            return render(
                request,
                "register.html",
                {"error": error_message, "username": username, "email": email},
            )
        except User.DoesNotExist:
            # Проверка уникальности email
            if User.objects.filter(email=email).exists():
                error_message = "Пользователь с таким email уже зарегистрирован"
                return render(
                    request,
                    "register.html",
                    {"error": error_message, "username": username, "email": email},
                )

            # Создание нового пользователя
            User.objects.create_user(username, email, password)
            messages.success(
                request, "Регистрация прошла успешно! Теперь вы можете войти."
            )
            return redirect("login")

    return render(request, "register.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        # Проверка на пустые поля
        if not username or not password:
            error_message = "Все поля должны быть заполнены"
            return render(
                request, "login.html", {"error": error_message, "username": username}
            )

        # Аутентификация пользователя
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Проверка активности пользователя
            if user.is_active:
                login(request, user)
                messages.success(request, f"Добро пожаловать, {user.username}!")
                return redirect("/")
            else:
                error_message = "Ваш аккаунт деактивирован"
                return render(
                    request,
                    "login.html",
                    {"error": error_message, "username": username},
                )
        else:
            # Неверные учетные данные
            error_message = "Неверное имя пользователя или пароль"
            return render(
                request, "login.html", {"error": error_message, "username": username}
            )

    return render(request, "login.html")


def hello_world(request):
    return render(request, "helloworld.html")


def classmates(request):
    return render(request, "classmates.html")

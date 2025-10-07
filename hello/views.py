from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render


# def index(request):
#     header = "Данные пользователя"  # обычная переменная
#     langs = ["Python", "Java", "C#"]  # список
#     user = {"name": "Tom", "age": 23}  # словарь
#     address = ("Абрикосовая", 23, 45)  # кортеж
#
#     data = {"header": header, "langs": langs, "user": user, "address": address}
#     return render(request, "index.html", context=data)



# from django.shortcuts import render
# from django.http import HttpResponse
#
#
# def index(request):
#     return render(request, "index.html")
#
#
# def postuser(request):
#     # получаем из строки запроса имя пользователя
#     name = request.POST.get("name", "Undefined")
#     age = request.POST.get("age", 1)
#     langs = request.POST.getlist("languages", ["python"])
#
#     return HttpResponse(f"""
#                 <div>Name: {name}  Age: {age}<div>
#                 <div>Languages: {langs}</div>
#             """)
# from django.shortcuts import render
# from django.http import HttpResponse
#
#
# def index(request):
#     return render(request, "index.html")
#
#
# def postuser(request):
#     # получаем из данных запроса POST отправленные через форму данные
#     name = request.POST.get("name", "Undefined")
#     age = request.POST.get("age", 1)
#     return HttpResponse(f"<h2>Name: {name}  Age: {age}</h2>")
# def index(request):
#     return render(request, "index.html")


# def index(request):
#     return render(request, "index.html", context={"site": "METANIT.COM"})
from django.shortcuts import render
# from .forms import UserForm
# from django.shortcuts import render
# from django.http import HttpResponse
#
#
# def index(request):
#     userform = UserForm()
#     return render(request, "index.html", {"form": userform})
# ;
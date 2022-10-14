from django.shortcuts import redirect, render
from .models import Review

# Create your views here.


def index(request):
    All_Review = Review.objects.all()
    context = {
        "a": All_Review,
    }
    return render(request, "articles/index.html", context)


def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    movie_name = request.GET.get("movie_name")
    grade = request.GET.get("grade")
    Review.objects.create(
        title=title,
        content=content,
        movie_name=movie_name,
        grade=grade,
    )
    return redirect("articles:index")


def edit(request, pk):
    d = Review.objects.get(pk=pk)

    title = request.GET.get("title")
    content = request.GET.get("content")
    movie_name = request.GET.get("movie_name")
    grade = request.GET.get("grade")

    d.title = title
    d.content = content
    d.movie_name = movie_name
    d.grade = grade

    d.save()
    return redirect("articles:index")


def new(request):
    return render(request, "articles/new.html")


def detail(request, pk):
    d = Review.objects.get(pk=pk)
    context = {
        "b": d,
    }
    return render(request, "articles/index.html", context)


def delete(request, pk):
    d = Review.objects.get(pk=pk).delete()
    return redirect("articles:index")


def update(request, pk):
    d = Review.objects.get(pk=pk)
    context = {
        "d": d 
    }
    return render(request, "articles/new.html", context)


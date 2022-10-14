from django.shortcuts import redirect, render
from .models import Review
from .forms import ppp


# Create your views here.


def index(request):
    All_Review = Review.objects.all()
    form = ppp()
    context = {
        "a": All_Review,
        "form": form,
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


def edit(request, pk):  # 영화 데이터 수정 후 db저장
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


def detail(request, pk):  # 영화 자세히보기 (디테일페이지 idex if 분기)
    d = Review.objects.get(pk=pk)
    context = {
        "b": d,
    }
    return render(request, "articles/index.html", context)


def delete(request, pk):
    d = Review.objects.get(pk=pk).delete()
    return redirect("articles:index")


def update(request, pk):  # 영화 데이터 (수정 할 값 넣는 함수 )
    d = Review.objects.get(pk=pk)
    context = {"d": d}
    return render(request, "articles/edit.html", context)

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.http import Http404


def curpost(request, slug_link):
    info = get_object_or_404(Post, slug=slug_link)
    content = {"post": info}
    return render(request, 'Posts/detailpost.html', content)


def forum_blog(request, name):
    posts = Post.objects.filter(forum__name__iexact=name)
    if not posts.exists():
        raise Http404("Forum Does Not Exist")
    recent = Post.objects.all().order_by('id')[::-1][:5]
    forum_name = name
    banner = posts[0].category.banner
    context = {
        "posts": posts,
        "recent": recent,
        "forum_name": forum_name,
        "banner": banner
    }
    return render(request, 'Posts/template.html', context)


def sagar(request):
    context = {
        "posts": Post.objects.filter(forum__name__iexact="Sagar"),
        "recent": Post.objects.all().order_by('id')[::-1][:5]
    }
    return render(request, 'Posts/Sagar.html', context)


def vasundhara(request):
    context = {
        "posts": Post.objects.filter(forum__name__contains="Vasundhara"),
        "recent": Post.objects.all().order_by('id')[::-1][:5]
    }
    return render(request, 'Posts/Vasundhara.html', context)


def srishti(request):
    context = {
        "posts": Post.objects.filter(forum__name__contains="Srishti"),
        "recent": Post.objects.all().order_by('id')[::-1][:5]
    }
    return render(request, 'Posts/Srishti.html', context)


def himgiri(request):
    context = {
        "posts": Post.objects.filter(forum__name__contains="Himgiri"),
        "recent": Post.objects.all().order_by('id')[::-1][:5]
    }
    return render(request, 'Posts/Himgiri.html', context)


def school(request):
    context = {
        "posts": Post.objects.filter(forum__name__contains="School"),
        "recent": Post.objects.all().order_by('id')[::-1][:5]
    }
    return render(request, 'Posts/School.html', context)


def amun(request):
    context = {
        "posts": Post.objects.filter(forum__name__contains="AMUN"),
        "recent": Post.objects.all().order_by('id')[::-1][:5]
    }
    return render(request, 'Posts/AMUN.html', context)


def societies(request):
    context = {
        "posts": Post.objects.filter(forum__name__contains="Societies"),
        "recent": Post.objects.all().order_by('id')[::-1][:5]
    }
    return render(request, 'Posts/Societies.html', context)


def environment(request):
    context = {
        "posts": Post.objects.filter(forum__name__contains="Environment"),
        "recent": Post.objects.all().order_by('id')[::-1][:5]
    }
    return render(request, 'Posts/Environment.html', context)


def socialinitiatives(request):
    context = {
        "posts": Post.objects.filter(forum__name__contains="SocialInitiatives"),
        "recent": Post.objects.all().order_by('id')[::-1][:5]
    }
    return render(request, 'Posts/Social Initiatives.html', context)


def sports(request):
    context = {
        "posts": Post.objects.filter(forum__name__contains="Sports"),
        "recent": Post.objects.all().order_by('id')[::-1][:5]
    }
    return render(request, 'Posts/Sports.html', context)


def roundsquare(request):
    context = {
        "posts": Post.objects.filter(forum__name__contains="RoundSquare"),
        "recent": Post.objects.all().order_by('id')[::-1][:5]
    }
    return render(request, 'Posts/RoundSquare.html', context)


def edboard(request):
    context = {
        "posts": Post.objects.filter(forum__name__contains="EdBoard"),
        "recent": Post.objects.all().order_by('id')[::-1][:5]
    }
    return render(request, 'Posts/EdBoard.html', context)

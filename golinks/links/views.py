from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def index(request):
    context = {
        'link': "google.com",
    }
    return render(request, "links/index.html", context)


def forward(request, short_link):
    # TODO: Get long link from short link
    long_link = "https://google.com"
    return redirect(long_link, pernament=True)


def edit(request, short_link):
    return HttpResponse(short_link)
    # return render(request, 'links/edit.html')


def set_link(requets, short_link):
    return HttpResponse(short_link)


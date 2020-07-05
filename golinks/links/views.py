from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Link

# Create your views here.
def index(request):
    context = {
        'link_list': Link.objects.all(),
    }
    return render(request, "links/index.html", context)


def forward(request, short_link):
    try:
        link = Link.objects.get(short_link=short_link)
        return redirect(link.long_link, pernament=True)
    except Link.DoesNotExist:
        return redirect(f'{short_link}/edit', pernament=False)
        return HttpResponse(short_link)


def edit(request, short_link):
    return HttpResponse(short_link)
    # return render(request, 'links/edit.html')


def set_link(requets, short_link):
    return HttpResponse(short_link)


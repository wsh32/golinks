from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import PermissionDenied

from .models import Link

# Create your views here.
def index_view(request):
    context = {
        'link_list': Link.objects.all().order_by('short_link'),
    }
    return render(request, "links/index.html", context)


def forward_view(request, short_link):
    try:
        link = Link.objects.get(short_link=short_link)
        return redirect(link.long_link, pernament=True)
    except Link.DoesNotExist:
        return redirect(f'{short_link}/edit', pernament=False)
        return HttpResponse(short_link)


def edit_view(request, short_link):
    long_link = "#!"
    link_owner = None
    try:
        link = Link.objects.get(short_link=short_link)
        long_link = link.long_link
        link_owner = link.owner
    except Link.DoesNotExist:
        None

    context = {
        'short_link': short_link,
        'long_link': long_link,
    }

    if link_owner is None or link_owner == request.user:
        return render(request, 'links/edit.html', context)
    else:
        raise PermissionDenied


def set_link_view(request, short_link):
    if 'long_link' not in request.POST.keys():
        return HttpResponse("No link provided")

    user = None  # null user means public link (editable by anyone)
    if request.user.is_authenticated:
        user = request.user

    # By default, links are set to public. If the 'anonymous' tag in the POST
    # data is set to anything except for 'true', it will become a private link.
    # Private links are defined as visible to everyone but only editable by the
    # user who created it
    anonymous = True
    if 'anonymous' in request.POST.keys() and request.user.is_authenticated:
        anonymous = (request.POST['anonymous'] == 'true')

    long_link = request.POST['long_link']
    try:
        link = Link.objects.get(short_link=short_link)
        # Must have permissions
        if link.owner is None or link.owner == user:
            link.long_link = long_link
            link.save()
        else:
            raise PermissionDenied
    except Link.DoesNotExist:
        link = Link(short_link=short_link, long_link=long_link, owner=user)
        link.save()

    return redirect(long_link, pernament=True)


def login_view(request):
    return render(request, "links/login.html")


def logout_view(request):
    logout(request)
    return redirect('index')


def auth_view(request):
    if 'username' not in request.POST or 'password' not in request.POST:
        return HttpResponse("Missing username or password")
    username = request.POST['username']
    password = request.POST['password']
    return redirect('index')


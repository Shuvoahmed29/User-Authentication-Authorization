from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def admin(request):
    user = request.user
    if user.is_superuser:
        return render(request, 'admin.html')
    else:
        return HttpResponse("Unauthorized access")

@login_required
def editor(request):
    user = request.user
    if user.groups.filter(name="editor").exists():
        return render(request, 'editor.html')
    else:
        return HttpResponse("Editor Unauthorized access")

@login_required
def author(request):
    user = request.user
    if user.groups.filter(name="author").exists():
        return render(request, 'author.html')
    else:
        return HttpResponse("Author Unauthorized access")
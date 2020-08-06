from django.shortcuts import render

# Create your views here.


def comments_user(request):

    return render(request, 'comments/form.html', {})
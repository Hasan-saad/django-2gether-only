# from multiprocessing.reduction import register
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.shortcuts import render, redirect,  get_object_or_404
from django.urls import reverse
from .models import *
from django.core.paginator import Paginator
from .form import ReservationProblem, AddService, CommentForm
from .filters import ServicProviderFilter
from accounts.models import Profile
from accounts.forms import UserForm,ProfileForm


def service_list(request):
    service_list = ServicProvider.objects.filter(Vacancy__lte=0).delete()
    service_list = ServicProvider.objects.all()
    
    if request.user.is_authenticated:
        profile_detals = Profile.objects.get(user=request.user)
    

    filter = ServicProviderFilter(request.GET, queryset=service_list)
    service_list = filter.qs
    paginator = Paginator(service_list, 3)  # Show 25 contacts per page.
    pageNumber = request.GET.get('page')
    pagePaginator = paginator.get_page(pageNumber)

    context ={'services': pagePaginator, 'service_provider': service_list, 'filter': filter}
    return render(request, 'ServiceProvider/Service_list.html', context)


def service_detals(request, id):
    service_detals = ServicProvider.objects.get(id=id)
    profile_detals = ''
    if request.user.is_authenticated:
        profile_detals = Profile.objects.get(user=request.user)
    # Comments
    comments = Comment.objects.filter(serviceProvider_id = service_detals)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        form = ReservationProblem(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.service = service_detals
            myform.save()
            service_detals.Vacancy -= 1
            service_detals.save()
    else:
        form = ReservationProblem()

    commentForm = None
    if request.method == 'POST' and not form.is_valid():
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = commentForm.save(commit=False)
            # Assign the current post to the comment
            new_comment.user = profile_detals 
            new_comment.serviceProvider = service_detals 
            # Save the comment to the database
            new_comment.save()
    else:
        commentForm = CommentForm()


    context = {'service': service_detals, 'form': form,'profile_detals':profile_detals,
                'comments': comments, 'new_comment': new_comment, 'commentForm': commentForm}
    return render(request, 'ServiceProvider/Service_detail.html', context)


@login_required
def add_service(request):
    if request.method == 'POST':
        serviceProviderForm = AddService(request.POST, request.FILES)
        if serviceProviderForm.is_valid():         
            formService = serviceProviderForm.save(commit=False)
            formService.user = request.user
            formService.save()
            
            return redirect(reverse('services:service_list'))
    else:
        serviceProviderForm = AddService()
    context = { 'serviceProviderForm': serviceProviderForm}
    return render(request, 'ServiceProvider/Post_service.html', context)


def home(request):
    Services = ServicProvider.objects.all()
    categorys = Category.objects.all()

    paginator_cago = Paginator(categorys, 8)
    pageNumberCategory = request.GET.get('page')
    pagePaginatorCategory = paginator_cago.get_page(pageNumberCategory)
    
    paginator = Paginator(Services, 3)  # Show 25 contacts per page.
    pageNumber = request.GET.get('page')
    pagePaginator = paginator.get_page(pageNumber)

    return render( request, 'ServiceProvider/index.html', {'Services':Services, 'categorys':pagePaginatorCategory, 'service':pagePaginator} )





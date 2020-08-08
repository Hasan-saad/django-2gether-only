# from multiprocessing.reduction import register

from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import ServicProvider
from django.core.paginator import Paginator
from .form import ReservationProblem, AddService
from .filters import ServicProviderFilter
from accounts.models import Profile
from accounts.forms import UserForm,ProfileForm


def service_list(request):
    service_list = ServicProvider.objects.filter(Vacancy__lte=0).delete()
    service_list = ServicProvider.objects.all()
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
    profile_detals = Profile.objects.get(user=request.user)
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
    context = {'service': service_detals, 'form': form,'profile_detals':profile_detals}
    return render(request, 'ServiceProvider/Service_detail.html', context)

# @register.filter
# def subtract(value, arg):
#     return value - arg

@login_required
def add_service(request):
    if request.method == 'POST':
        serviceProviderForm = AddService(request.POST, request.FILES)
        if serviceProviderForm.is_valid():         
            formService = serviceProviderForm.save(commit=False)
            formService.user = request.user
            formService.save()
            
            return redirect(reverse('services:sercive_list'))
    else:
        serviceProviderForm = AddService()
    context = { 'serviceProviderForm': serviceProviderForm}
    return render(request, 'ServiceProvider/Post_service.html', context)


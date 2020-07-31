from django.shortcuts import render, redirect, get_object_or_404
from salesrecord.models import Salesrecord
from salesrecord.forms import SalesrecordForm, CreateUserForm
from django.core.paginator import Paginator
from django.http import HttpResponse
from .resources import SalesResource
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def index(request):
    return render(request, 'index.html')


def display_records(request):
    items = Salesrecord.objects.all()
    query = request.GET.get('search')
    if query:
        items = Salesrecord.objects.filter(Q(Country__icontains=query)|
                             Q(Item_type__icontains=query)|
                             Q(Sales_channel__icontains=query)).distinct()
    paginator = Paginator(items, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }
    return render(request, 'index.html', context)


def add_record(request):
    if request.method == "POST":
        form = SalesrecordForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = SalesrecordForm()
        return render(request, 'add.html', {'form': form})



def export(request):
    sales_resource = SalesResource()
    Salesrecord= sales_resource.export()
    response = HttpResponse(Salesrecord.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Salesrecord.csv"'
    return response

def edit_record(request, id):
    item = get_object_or_404(Salesrecord, id=id)

    if request.method == "POST":
        form = SalesrecordForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SalesrecordForm(instance=item)

        return render(request, 'edit.html', {'form': form})


@login_required(login_url='login')
def delete_record(request, id):
    Salesrecord.objects.filter(id=id).delete()
    return redirect('/')

def register(request):
    if request.user.is_authenticated:
        return redirect('display_records')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)


def login_page(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=uname, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('display_records')
    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('display_records')

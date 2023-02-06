from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
from django.contrib import messages

from .forms import AvailabilityForm
from .models import User
from operator import itemgetter
from django.views.generic import ListView,FormView,View
from projects.models import Hotel, Booking
from .forms import AvailabilityForm,CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from projects.booking_functions.availability import check_availability


#def register(request):
   # form = UserCreationForm
  #  return render(request,'register.html',{'form':form})

#def login(request):
    #return render(request,'login.html')


def home(request):
   return render(request, 'store/home.html')

def about(request):
    return render(request, 'store/about.html')

def contact(request):
    return render(request, 'store/contact.html')

@login_required(login_url='login')
def scenaries(request):
    return render(request, 'store/scenaries.html')

@login_required(login_url='login')
def booking(request):
    return render(request, 'store/booking.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect(home)

            else:
                return redirect('home')
        context = {}
        return render(request, 'store/login.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for' + user)
                return redirect('login')
    
        context = {'form':form}
        return render(request, 'store/register.html', context)

def logout(request):
    logout(request)
    return redirect('login')

class HotelListView(ListView):
    model = Hotel

class BookingList(ListView):
    model = Booking

class HotelDetailView(View):
    def get(self,request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        form = AvailabilityForm()
        hotel_list = Hotel.objects.filter(category=category)

        if len(hotel_list)>0:
            hotel = hotel_list[0]
            hotel_category = dict(hotel.HOTEL_CATEGORIES).get(room.category, None)
            context={
                'hotel_category' : hotel_category,
                'form' : form,

            }
            return render(request, 'hotel_detail_view.html', context)
        else:
            return HttpResponse('Category does not exist')
        


    def post(self,request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        hotel_list = Hotel.objects.filter(category=category)
        form = AvailabilityForm(request.POST)

        if form.is_valid():
            data - form.cleaned_data
            
        available_hotels=[]
        for hotel in hotel_list:
            if check_availability(hotel, data['check_in'], data['check_out']):
                available_hotels.append(hotel)

        if len(available_hotels)>0:
            hotel = available_hotels[0]
            booking = Booking.objects.create(
                user = self.request.User,
                hotel = hotel,
                 check_in=data['check_in'],
                check_out=data['check_out']
        )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('All this category of hotels are booked!! Try another one')

class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'availability_form.html'

    def form_valid(self,form):
        data = form.cleaned_data
        hotel_list = Hotel.objects.filter(category=category)
        available_hotels=[]
        for hotel in hotel_list:
            if check_availability(hotel, data['check_in'], data['check_out']):
                available_hotels.append(hotel)

        if len(available_hotels)>0:
            hotel = available_hotels[0]
            booking = Booking.objects.create(
                user = self.request.User,
                hotel = hotel,
                check_in=data['check_in'],
                check_out=data['check_out']
        )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('All this category of hotels are booked!! Try another one')





#def project(request, pk):
    #return render(request, 'project.html')


from django.shortcuts import render , redirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .serializers import UserSerializer , BookingSerializer , CarSerializer
from rest_framework.response import Response
from .models import UserMaster ,  Booking , Car
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = UserMaster.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse({'message': 'User Fetched Successfully', 'data': serializer.data})

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'User created successfully', 'data': serializer.data})
        return JsonResponse({'message': 'Failed to create user', 'errors': serializer.errors})


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    user = get_object_or_404(UserMaster, pk=pk)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse({'data': serializer.data})

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'User updated successfully', 'data': serializer.data})
        return JsonResponse({'message': 'Failed to update user', 'errors': serializer.errors})

    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message': 'User deleted successfully'})


@api_view(['GET', 'POST'])
def car_list(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response({'message': 'Cars Fetched Successfully', 'data': serializer.data})

    elif request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Car created successfully', 'data': serializer.data})
        return Response({'message': 'Failed to create car', 'errors': serializer.errors})


@api_view(['GET', 'PUT', 'DELETE'])
def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'GET':
        serializer = CarSerializer(car)
        return Response({'data': serializer.data})
    
    if request.method == 'PUT':
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Car updated successfully', 'data': serializer.data})
        return Response({'message': 'Failed to update car', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        car.delete()
        return Response({'message': 'Car deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def booking_list(request):
    if request.method == 'GET':
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response({'message': 'Bookings Fetched Successfully', 'data': serializer.data})

    elif request.method == 'POST':
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Booking created successfully', 'data': serializer.data})
        return Response({'message': 'Failed to create booking', 'errors': serializer.errors})


@api_view(['GET', 'PUT', 'DELETE'])
def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)

    if request.method == 'GET':
        serializer = BookingSerializer(booking)
        return Response({'data': serializer.data})

    elif request.method == 'PUT':
        serializer = BookingSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Booking updated successfully', 'data': serializer.data})
        return Response({'message': 'Failed to update booking', 'errors': serializer.errors})

    elif request.method == 'DELETE':
        booking.delete()
        return Response({'message': 'Booking deleted successfully'})

def login_view(request):
    if request.method == 'POST':
       print("Hello")
       email = request.POST['email']
       password = request.POST['password']
    try:
        user = UserMaster.objects.get(email=email, password = password)
        if user is not None:
            user = {
                "id":user.id,
                "name":user.name,
                "email":user.email,
                "role":user.role
            }
            return JsonResponse({
                "message":"Login SuccessFully",
                "data":user
            })
    except Exception as e:
           return JsonResponse({
               "message":str(e)
           })

    return render(request , "login.html")

def create_car(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        model = request.POST.get('model')
        year = request.POST.get('year')
        price = request.POST.get('price')

        Car.objects.create(name=name, model=model, year=year, price=price)
        return redirect('home')  

    return render(request, 'create_car.html')


def index(request):
    cars = Car.objects.filter(delete_flag=False)
    return render(request, 'index.html', {'cars': cars})


def book_car(request, car_id , user_id):
    car_id = car_id
    user_id = user_id
    Booking.objects.create(user_id=user_id, car_id=car_id)
    return redirect('home')  


def view_bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'booking.html', {'bookings': bookings})

def edit_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        model = request.POST.get('model')
        year = request.POST.get('year')
        price = request.POST.get('price')
        print(name)
        print(model)
        try:
            car.name = name
            car.model = model
            car.year = year
            car.price = price
            car.save()
            return redirect("home")
        except Exception as e:
            return redirect("create_car")

def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id, delete_flag=False)

    if request.method == 'POST':
        car.soft_delete()
        return redirect("home")  # Redirect to home or the appropriate URL

    return render(request, 'index.html', {'car': car})
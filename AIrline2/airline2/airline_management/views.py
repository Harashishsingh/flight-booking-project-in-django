from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from airline_management.models import table,signup,my,reserve

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['firstname']
        lname =request.POST['lastname']
        el = request.POST["email"]
        passw = request.POST["password"]
        
        
        if passw:
            user = User.objects.create_user(username=username,first_name=fname,last_name=lname, email=el, password=passw)
            user.save()
            if user:
                return redirect(signin)
            else:
                return HttpResponse("Try again")
        else:
            return HttpResponse("Incorrect Password")
    else:
        return render(request, "signup.html")
    


def signin(request):
    if request.method =="POST":
        if request.method == "POST":
            
            username = request.POST['username']
            passw = request.POST['password']

            user = authenticate(username=username,password=passw)
            if user is not None:
                login(request, user)
                return redirect('/home')
            else:
                return HttpResponse("user not found")
    else:
        return render(request,"login.html")


def signout(request):
    logout(request)
    return redirect (signin)



def view_form(request):
    if request.method =="POST":
        flight_name=request.POST['flight_name']
        dea=request.POST['dea']
        dest=request.POST['dest']
        depart=request.POST['depart']
        time=request.POST['time']

        aa= table(Flight_name=flight_name,Departure=dea,Destination=dest,Depart=depart,Time=time)
        aa.save()
        if aa:
            return HttpResponse("done")
        else:
            return HttpResponse("try again")
    else:
        return render(request,"view_flight.html")
    
def view_data(request):
    data = table.objects.all()
    return render(request,"flight.html",{"data":data})

def flight(request):
    data = table.objects.all()
    return render(request,"flight.html",{"data":data})

def reservation(request,id):
    flight_id = table.objects.get(id=id)
    if request.method =="POST":
        user_id = request.user
        passenger=request.POST['passenger']
        em=request.POST['email']
        phone=request.POST['phn']
        number=request.POST['num']
        sea=request.POST['seat']

        bb= reserve(flight_id=flight_id,user_id=user_id,Passenger_name=passenger,Email=em,Phone_number=phone,Number_pass=number,Seat=sea)
        bb.save()
        return redirect(home)
    else:
        return render(request,"reservation.html")

def delete_data(request,id):
    data = table.objects.get(id = id)
    data.delete()
    return redirect('/views')

def update_data(request,id):
    data = table.objects.get(id = id)
    if request.method == "POST":
        data.flight_name = request.POST["flight_name"]
        data.dea = request.POST["dea"]
        data.dest = request.POST["dest"]
        data.depart = request.POST["depart"]
        data.time = request.POST["time"]

        data.save()
        return redirect('views')
    else:
        
        return render(request,"view_flight.html",{"data":data})
    
def home(request):
        return render(request,"home.html")
    
def re(request):
    data = reserve.objects.all()
    return render(request,"res.html",{"data":data})

def contact(request):
    return render(request,"contact.html")

def ticket(request):
    data = reserve.objects.filter(user_id=request.user)
    print(data,'-=-=-=-=')
    return render(request,'ticket.html',{"data":data})




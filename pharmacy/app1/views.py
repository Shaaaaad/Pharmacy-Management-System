from django.shortcuts import render,HttpResponse,redirect
from.models import Login,Medicine,Sales
# Create your views here.
def view(request):
    return render(request,'home.html')

def home(request):
    return render(request,'home.html')



def controlpage(request):
    data = Medicine.objects.all()
    return render(request,'controlpage.html',{'data':data})




def loginform(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        try:
            data = Login.objects.get(username=username)
            if data.password == password:
                request.session['id'] = data.id
                return redirect(controlpage)
            else:
                return  HttpResponse("PASSWORD ERROR")
        except Exception:
            return HttpResponse("USERNAME ERROR")
    else:
        return render(request, 'home.html')


def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(home)
    else:
        return render(request, 'controlpage.html')

def addmedicine(request):
    if request.method == 'POST':
        medicinename = request.POST['medicinename']
        medicinetype = request.POST['medicinetype']
        medicinestock = request.POST['medicinestock']
        medicineprice = request.POST['medicineprice']
        data = Medicine.objects.create(medicinename=medicinename,medicinetype=medicinetype,medicinestock=medicinestock,medicineprice=medicineprice)
        data.save()
        return redirect(controlpage)


def deletemedicine(request, id):
  data = Medicine.objects.get(id=id)
  data.delete()
  return redirect(controlpage)



def editmedicine(request,id):

    data = Medicine.objects.get(id=id)
    if request.method == "POST":
        newmedicinename = request.POST['newmedicinename']
        newmedicinetype = request.POST['newmedicinetype']
        newmedicineprice = request.POST['newmedicineprice']
        newmedicinestock = request.POST['newmedicinestock']


        try:
            data = Medicine.objects.get(id=id)
            if data.id == id:
                data.medicinename = newmedicinename
                data.medicinetype = newmedicinetype
                data.medicineprice = newmedicineprice
                data.medicinestock = newmedicinestock
                data.save()
                return redirect(controlpage)
            else:
                return HttpResponse("Book not Found")
        except Exception:
            return HttpResponse("Check the Book name")
    else:
        return render(request, 'editmedicine.html', {'data':data})


def addsalesview(request):
    data = Medicine.objects.all()
    return render(request,'addsales.html',{'data':data})


def addsales(request):
    if request.method == 'POST':
        customername = request.POST['customername']
        customercontact = request.POST['customercontact']
        medicine = request.POST['medicine']
        data = Sales.objects.create(customername=customername,customercontact=customercontact,medicine=medicine)
        data.save()
        data1=Sales.objects.filter(customername=customername)
        return render(request,'addsales.html',{'data1':data1})

def deletesales(request, id):
  data = Sales.objects.get(id=id)
  data.delete()
  return redirect(addsalesview)
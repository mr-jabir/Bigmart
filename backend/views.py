from django.shortcuts import render,redirect
# Create your views here.
from backend.models import admindb, categorysave, proDetails, contactdb
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


def viewindex(req):
    return render(req,"index.html")
def viewadmin(req):
    return  render(req,"addadmin.html")
def saveadmin(req):
    if req.method == "POST":
        na = req.POST.get('name')
        email = req.POST.get('email')
        num = req.POST.get('number')
        uname = req.POST.get('username')
        passwrd = req.POST.get('password')
        img = req.FILES['image']
        obj = admindb(NAME=na, EMAIL=email, NUMBER=num, USERNAME=uname, PASSWORD=passwrd, IMAGE=img )
        obj.save()
        return redirect(viewadmin)
def displayadmin(req):
    data = admindb.objects.all()
    return render(req,"displayadmin.html", {'data':data})

def editadminpage(req,dataid):
    data = admindb.objects.get(id=dataid)
    print(data)
    return render(req,"editadmin.html", {'data':data})
def updateadmin(req,dataid):
    if req.method == "POST":
        na = req.POST.get('name')
        email = req.POST.get('email')
        num = req.POST.get('number')
        uname = req.POST.get('username')
        passwrd = req.POST.get('password')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = admindb.objects.get(id=dataid).IMAGE
        admindb.objects.filter(id=dataid).update(NAME=na, EMAIL=email, NUMBER=num, USERNAME=uname, PASSWORD=passwrd, IMAGE=file)
        return redirect(displayadmin)

def deleteadmin(req,dataid):
    data = admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayadmin)

def category(req):
    return render(req,"addcategory.html")

def savecategory(request):
    if request.method == "POST":
        na = request.POST.get('name')
        de = request.POST.get('description')
        im = request.FILES['image']
        obj=categorysave(Name=na,Description=de,Image=im)
        obj.save()
        return redirect(category)

def displayproduct(request):
    data = categorysave.objects.all()
    return render(request, "displaycategory.html", {'data': data})

def editproduct(request, dataid):
    data = categorysave.objects.get(id=dataid)
    print(data)
    return render(request, "editcategory.html", {'data': data})

def updateproduct(request,dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        de = request.POST.get('description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = categorysave.objects.get(id=dataid).Image
        categorysave.objects.filter(id=dataid).update(Name=na, Description=de,Image=file)
        return redirect(displayproduct)

def deleteproduct(req,dataid):
    data = categorysave.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproduct)

def productDetails(request):
    data = categorysave.objects.all()
    return render(request,"addProduct.html", {'data':data})

def prodSave(request):
    if request.method == "POST":
        ca = request.POST.get("category")
        na = request.POST.get('name')
        pr = request.POST.get('price')
        qu = request.POST.get('qty')
        de = request.POST.get('description')
        im = request.FILES['image']
        obj=proDetails(Category=ca,Name=na,Price=pr,Quantity=qu,Description=de,Image=im)
        obj.save()
        return redirect(productDetails)

def productDisplay(request):
    data = proDetails.objects.all()
    return render(request,"displayproduct.html", {'data':data})

def Productedit(request,dataid):
    data = proDetails.objects.get(id=dataid)
    da =categorysave.objects.all()
    print(data)
    print(da)
    return render(request,"editproduct.html", {'datas':data,'da':da})

def productupdate(request,dataid):
    if request.method == "POST":
        ca = request.POST.get('category')
        na = request.POST.get('name')
        pr = request.POST.get('price')
        qu = request.POST.get('qty')
        de = request.POST.get('description')
        try:
            im = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(im.name,im)
        except MultiValueDictKeyError:
            file = proDetails.objects.get(id=dataid).Image
        proDetails.objects.filter(id=dataid).update(Category=ca,Name=na,Price=pr,Quantity=qu, Description=de,Image=file)
        return redirect(productDisplay)

def productdelete(req,dataid):
    data = proDetails.objects.filter(id=dataid)
    data.delete()
    return redirect(productDisplay)

def logintemp(req):
    return render(req,"loginpage.html")

def adminlogin(req):
    if req.method=="POST":
        username_r = req.POST.get('username')
        password_r = req.POST.get('pass')

        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r,password=password_r)
            if user is not None:
                login(req,user)
                req.session['username']=username_r
                req.session['pass']=password_r
                return redirect(viewindex)
            else:
                return redirect(logintemp)

def displaycontact(req):
    data = contactdb.objects.all()
    return render(req,"contactdisplay.html",{'data':data})
def deletecontact(req,dataid):
    data = contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycontact)

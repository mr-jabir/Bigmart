from django.shortcuts import render,redirect
from backend.models import categorysave
from backend.models import proDetails
from frontend.models import CustRegdb
from backend.models import contactdb

# Create your views here.

def homepage(request):
    return render(request,"home.html")

def aboutus(request):
    return render(request,"aboutus.html")

def contact(request):
    return render(request,"contactus.html")

def homepage(request):
    data = categorysave.objects.all()
    return render(request,"home.html",{'data':data})

def categories(req):
    return render(req,"category_display.html")


def discategory(request,itemcatg):
    print("===itemcatg===", itemcatg)
    catg = itemcatg.upper()

    products = proDetails.objects.filter(Category=itemcatg)
    context = {
        'products': products,
        'catg': catg
    }
    return render(request,"category_display.html",context)



def prodetails(request,dataid):
    data=proDetails.objects.get(id=dataid)
    return render(request,"singleproduct.html",{'dat':data})

def loginpage(req):
    return render(req,"loginpage.html")






def loginsave(req):
    if req.method == "POST":
        uname = req.POST.get('uname')
        email = req.POST.get('email')
        passwrd = req.POST.get('pwd')
        copwd = req.POST.get('cpwd')
        obj = CustRegdb(USERNAME=uname, EMAIL=email, PASSWORD=passwrd, CONPWD=copwd)
        obj.save()
        return redirect(loginpage)


def customerlogin(request):
    if request.method=="POST":
        username_r=request.POST.get("username")
        password_r=request.POST.get("password")
        if CustRegdb.objects.filter(USERNAME=username_r,PASSWORD=password_r).exists():
            request.session['username']=username_r
            request.session['password']=password_r

            return redirect(homepage)
        else:
            return render(request,'loginpage.html',{'msg':"sorry... invalid username or password"})

def userlogout(request):
    del request.session['username']
    del request.session['password']

    return redirect(homepage)


def contactsavedb(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        sb = request.POST.get('sub')
        ms = request.POST.get('message')
        obj = contactdb(Name=na, Email=em, Subject=sb, Message=ms)
        obj.save()
        return redirect(contact)

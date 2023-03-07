from django.urls import path
from frontend import views

urlpatterns=[
    path('homepage/',views.homepage,name="homepage"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('contact/',views.contact,name="contact"),
    path('categories/',views.categories,name="categories"),
    path('discategory/<itemcatg>',views.discategory,name="discategory"),
    path('prodetails/<int:dataid>',views.prodetails,name="prodetails"),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('loginsave/',views.loginsave,name="loginsave"),
    path('customerlogin/',views.customerlogin,name="customerlogin"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('contactsavedb/',views.contactsavedb,name="contactsavedb")
]
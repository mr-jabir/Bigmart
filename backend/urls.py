from django.urls import path
from backend import views

urlpatterns=[
    path('viewindex/', views.viewindex, name="viewindex"),
    path('viewadmin/', views.viewadmin, name="viewadmin"),
    path('saveadmin/', views.saveadmin, name="saveadmin"),
    path('displayadmin/', views.displayadmin, name="displayadmin"),
    path('editadminpage/<int:dataid>/', views.editadminpage, name="editadminpage"),
    path('updateadmin/<int:dataid>/',views.updateadmin, name="updateadmin"),
    path('deleteadmin/<int:dataid>/', views.deleteadmin, name="deleteadmin"),
    path('category/',views.category,name="category"),
    path('savecategory/',views.savecategory,name="savecategory"),
    path('displayproduct/',views.displayproduct,name="displayproduct"),
    path('editproduct/<int:dataid>/',views.editproduct,name="editproduct"),
    path('updateproduct/<int:dataid>/',views.updateproduct,name="updateproduct"),
    path('deleteproduct/<int:dataid>/',views.deleteproduct,name="deleteproduct"),
    path('productDetails/',views.productDetails,name="productDetails"),
    path('prodSave/',views.prodSave,name="prodSave"),
    path('productDisplay/',views.productDisplay,name="productDisplay"),
    path('Productedit/<int:dataid>/',views.Productedit,name="Productedit"),
    path('productupdate/<int:dataid>/',views.productupdate,name="productupdate"),
    path('productdelete/<int:dataid>/',views.productdelete,name="productdelete"),
    path('logintemp/',views.logintemp,name="logintemp"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('displaycontact/',views.displaycontact,name="displaycontact"),
    path('deletecontact/<int:dataid>/',views.deletecontact,name="deletecontact")
]
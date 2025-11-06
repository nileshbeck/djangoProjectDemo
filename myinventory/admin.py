from django.contrib import admin
from . models import *

# Register your models here.
 
# id is auto generated in the db
class listcustomer(admin.ModelAdmin):
    list_display=[ 'name','phone','email','address'] # display in admin like list


admin.site.register(customer,listcustomer) #register table 

admin.site.register(Categories) # use to view data in django admin

class venderlist(admin.ModelAdmin):
    list_display=[ 'vender_name','contact_person','Phone','Email','Address'] # display in admin like list

admin.site.register(vender,venderlist)

class productlist(admin.ModelAdmin):
    list_display=[ 'Product_name','Category','Vender','Quantity','Purchase_price','Selling_price'] # display in admin like list

admin.site.register(product,productlist)
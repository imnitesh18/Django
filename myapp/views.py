from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import InputForm1

def hello(request):
    return HttpResponse("hello")
def home(request):
    return HttpResponse("""<body style='background-color:pink'>
        <h1 style='color:red'> heading</
        h1> </body>
        <p> para </p>""")
def menuitem(request):
    item ="pizza"
    return HttpResponse(f"The item name is {item}")
def menuitems(request):
    items ={
            'noodles': 'costs Rs 100',
            'pizza': 'costs Rs 500',
            'momos' : 'costs Rs 50'
        }
    content ="<h1> The menu are </h1> "
    for item,description in items.items():
        content+= f"<h2>(item)</h2> <p>{description}</p>"
    return HttpResponse(content)

def great(request, name):
    return HttpResponse(f"Hello{name},Welcome to our website")   


def addition(request,num1,num2):
    sum=num1+num2
    return HttpResponse(f"The addition is{sum}")

def add(request):
    value1=request.GET.get('value1')
    value2=request.GET.get('value2')
    sum=int(value1)+int(value2)
    return HttpResponse(f'the sum is {sum}')

def user_profile(request,username):
    return HttpResponse(f'the username is {username}')


def items(request,item_id):
    return HttpResponse(f'the username is {item_id}')  
    
def info(request,month,year):
    return HttpResponse(month + " "+year)    


def restuarant(request,category,subcategory):
    if (category=='') and (subcategory==''):
        return HttpResponse("Not found",status=404)
    else:
        return HttpResponse(f'The category is {category} and the subcategory is {subcategory}')
    
def about(request):
    return render(request,'about.html')    

def menus(request):
    items={'type':'India'}
    return render(request,'menu.html',items)

def menu1(request):
    items={'menuitems':[
       {'name':'north indian thali','cost':50},
       {'name':'south indian thali','cost':500}     
       ]}
    return render(request,'menu1.html',items)

def restro(request):
    items = [
        {'name': 'pizza', 'cost': 500},
        {'name': 'Fries', 'cost': 'free'},
        {'name': 'Momos', 'cost': 80},
        {'name': 'Chutney', 'cost': 'free'},
        {'name': 'pasta', 'cost': 70}
    ]
    
    # free=[item for item in items if item['cost']=='free']
    # return render(request, 'restro.html', {'free': free})
    return render(request, 'restro.html', {'items': items})

def restroo(request,item):
     items = {'menuitems4':[
        {'name': 'pizza', 'cost': 500},
        {'name': 'fries', 'cost': 'free'},
        {'name': 'momos', 'cost': 80},
        {'name': 'chutney', 'cost': 'free'},
        {'name': 'pasta', 'cost': 70}
    ]}
     
     selected_item=None
     for menu_item in items['menuitems4']:
         if menu_item['name']==item:
             selected_item=menu_item
             break
    
     return render(request, 'restroo.html', {'item':selected_item})


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# def food(request):
#     items = [
#         {'name': 'Naan', 'cost': 500, 'details':'Details for Naan'},
#         {'name': 'Idli', 'cost': 'free', 'details':'Details for Idli'},
#         {'name': 'Punugulu', 'cost': 80, 'details':'Details for Punugulu'},
#         {'name': 'Paratha', 'cost': 'free', 'details':'Details for Paratha'},
#         {'name': 'Daal Rice', 'cost': 70, 'details':'Details for Daal Rice'}
#     ]
#     return render(request, 'food.html', {'items':items})

# def food2(request, item):
#     list_items = [
#         {'name': 'Naan', 'cost': 500, 'details': 'Details for Naan'},
#         {'name': 'Idli', 'cost': 'free', 'details': 'Details for Idli'},
#         {'name': 'Punugulu', 'cost': 80, 'details': 'Details for Punugulu'},
#         {'name': 'Paratha', 'cost': 'free', 'details': 'Details for Paratha'},
#         {'name': 'Daal Rice', 'cost': 70, 'details': 'Details for Daal Rice'}
#     ]

#     singleItem = {}
#     for food in list_items:
#         if food['name'] == item:
#             singleItem = food
#             break

#     data = {
#         "item": singleItem
#     }
#     return render(request, 'food2.html', data)

def food(request):
    items = [
        {'name': 'Burger', 'cost': '₹300', 'details': 'Burger details'},
        {'name': 'Pizza', 'cost': '₹500', 'details': 'Pizza details'},
        {'name': 'Fries', 'cost': '₹200', 'details': 'Fries details'},
        {'name': 'Hot Dog', 'cost': '₹250', 'details': 'Hot Dog details'},
        {'name': 'Chicken Wings', 'cost': '₹400', 'details': 'Chicken Wings details'}
    ]
    context = {'items': items}
    return render(request, 'food.html', context)

def food_detail(request, item_name):
    items = [
        {'name': 'Burger', 'cost': '₹300', 'details': 'Burger details'},
        {'name': 'Pizza', 'cost': '₹500', 'details': 'Pizza details'},
        {'name': 'Fries', 'cost': '₹200', 'details': 'Fries details'},
        {'name': 'Hot Dog', 'cost': '₹250', 'details': 'Hot Dog details'},
        {'name': 'Chicken Wings', 'cost': '₹400', 'details': 'Chicken Wings details'}
    ]
    for item in items:
        if item['name'] == item_name:
            context = {'item': item}
            return render(request, 'food_detail.html', context)
    return render(request, '404.html')

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def simpleform(request):
  if request.method == 'POST':
      textbox1=request.POST.get('textbox1')
      textbox2=request.POST.get('textbox2')
      return HttpResponse(f"The values are {textbox1} and {textbox2}")
  else:
      form_html="""
      <form method="POST">
      <label for="textbox1">Text Box 1:</label><br>
      <input type="text" id="textbox1" name="textbox1"><br>
      <label for="textbox2">Text Box 2:</label><br>
      <input type="text" id="textbox2" name="textbox2"><br>
      <input type="submit" value="Submit">
      </form>
      """

      return HttpResponse(form_html)
  

from django.middleware.csrf import get_token
def simpleform1(request):
  csrf_token=get_token(request)
  if request.method == 'POST':
      textbox1=request.POST.get('textbox1')
      textbox2=request.POST.get('textbox2')
      return HttpResponse(f"The values are {textbox1} and {textbox2}")
  else:
      form_html=f"""
      <form method="POST">
      <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
      <label for="textbox1">Text Box 1:</label><br>
      <input type="text" id="textbox1" name="textbox1"><br>
      <label for="textbox2">Text Box 2:</label><br>
      <input type="text" id="textbox2" name="textbox2"><br>
      <input type="submit" value="Submit">
      </form>
      """

      return HttpResponse(form_html)


# two text box csrf addd two number with form submit button addition result
  

def simpleform3(request):
    csrf_token=get_token(request)
    if request.method == 'POST':
        textbox1 = int(request.POST.get('textbox1', 0)) 
        textbox2 = int(request.POST.get('textbox2', 0)) 
        result = textbox1 + textbox2
        return HttpResponse(f"The addition result is: {result}")
    else:
        form_html = f"""
            <form method="POST">
                <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
                <label for="textbox1">Number 1:</label><br>
                <input type="number" id="textbox1" name="textbox1" required><br>
                <label for="textbox2">Number 2:</label><br>
                <input type="number" id="textbox2" name="textbox2" required><br>
                <input type="submit" value="Add">
            </form>
        """
        return HttpResponse(form_html)
    

from django.views import View

class MyView(View):
    def get(self,request):
        return render(request,'form.html')
    

    def post(self,request):
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')

        if name and email and password:
            return HttpResponse('Form submitted Successfully!')
        
        return render(request,'form.html')
    

    def css(request):
        return render(request,'testcss.html')
    


def validation(request):
    name=''
    email=''
    password=''
    name_error=''
    email_error=''
    password_error=''


    if(request.method=='POST'):
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')

        if not name:
            name_error="NAme is Mandatory"

        if not email:
            email_error="email is Mandatory"

        if not password:
            password_error="password is Mandatory"   

        if name_error or email_error or password_error:
            return render(request,'validation.html',{
                'name':name,
                'email':email,
                'password':password,
                'name_error':name_error,
                'email_error':email_error,
                'password_error':password_error
            })   

    return render(request,'validation.html',{
        'name':name,
        'email':email,
        'password':password,
    }) 

from django.shortcuts import render
from .forms import InputForm1

def val_django_form(request):
    submitted_details = None
    if request.method == 'POST':
        form = InputForm1(request.POST)
        if form.is_valid():
            submitted_details = form.cleaned_data
        else:
            return render(request, 'val_django_form.html', {'form': form, 'submitted_details': submitted_details})
        
    else:
        form = InputForm1()
    
    return render(request, 'val_django_form.html', {'form': form, 'submitted_details': submitted_details})


from .forms import SignupForm
from .models import SignUp

from django.shortcuts import render
from .forms import SignupForm
from .models import SignUp

def sign(request):
    account_created = False
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email'] 
            password = form.cleaned_data['password']
            s = SignUp.objects.create(username=username, email=email, password=password)
            s.save()
            account_created = True
    else:
        form = SignupForm()
        
    return render(request, 'signup.html', {'form': form, 'account_created': account_created})

from .forms import CustomersForm
from .models import Customers

def sign1(request):
    account_created = False
    
    if request.method == 'POST':
        form = CustomersForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email'] 
            password = form.cleaned_data['password']
            s = Customers.objects.create(username=username, email=email, password=password)
            s.save()
            account_created = True
    else:
        form = CustomersForm()
        
    return render(request, 'signup.html', {'form': form, 'account_created': account_created})

       

def get_cookie(request):
    cookie_value=request.COOKIES.get('name')
    if cookie_value:
     return HttpResponse(f"Cookie value:{cookie_value}")

    else:
        return HttpResponse("cookie not found!") 


from .models import Blogpost

def blogpost(request):
    post=Blogpost.objects.filter()[2]
    return render(request, 'blogpost.html',{'post':post})


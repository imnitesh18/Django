from django.shortcuts import render
from django.http import HttpResponse
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

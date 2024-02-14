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
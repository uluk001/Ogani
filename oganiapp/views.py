from django.http import HttpResponseRedirect
from django.shortcuts import render
from oganiapp.models import Contact, Category, FoodCard
# Create your views here.
def ogani(request):
    return render(request, 'index.html')



def sendMessage(request):
    if request.method == 'POST':
        send_message = Contact()
        send_message.email = request.POST.get("email")
        send_message.save()
        return HttpResponseRedirect('/')

def base(request):
    categories = Category.objects.all()
    food_card = FoodCard.objects.all()
    context = {'food_card':food_card, 'categories':categories } 
    return render(request, 'index.html', context=context)


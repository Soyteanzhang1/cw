from django.shortcuts import render,redirect,reverse,HttpResponse
from web import models
from web.forms import BolgForm
# Create your views here.

def index(request):
    all = models.Blog.objects.all()
    return render(request,'index.html',{'all':all})

def operation(request,id=None):
    obj = models.Blog.objects.filter(pk=id).first()
    form_obj = BolgForm(instance=obj)
    if request.method == 'POST':
        form_obj = BolgForm(request.POST,instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('index'))
    return render(request,'form_tem.html',{'form_obj':form_obj})




def delete(request,id):
    models.Blog.objects.filter(pk=id).delete()
    return redirect(reverse('index'))

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = models.User.objects.filter(user=username,pwd=password).first()
        if obj:
            # init_permission(request, obj)
            return redirect(reverse('index'))

    return render(request,'login.html')
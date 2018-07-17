from django.shortcuts import render,HttpResponse,redirect
from  app01 import models
# Create your views here.
from app01.models import Book

def query(request):
    '''
     queryset :  [model对象,model对象,model对象.....]
    model对象
    API接口返回值是什么
    :param request:
    :return:
    '''

    book_list = Book.objects.all()[0].nid
    # ret1=Book.objects.filter(price=100).first()
    # obj = Book.objects.all().first()
    # obj= Book.objects.filter(price__in=[100,200, 300])
    ret2=Book.objects.all().order_by("price")
    # ret = Book.objects.all().order_by("price").reverse()

    # print(ret)
    #模糊查询
    # ret=Book.objects.filter(price__gte=100)
    return HttpResponse(book_list)
def addl(request):
        if request.method=='POST':
            print(request.POST)
            title=request.POST.get("title")
            price = request.POST.get("price")
            pub_date = request.POST.get("pub_date")
            publish = request.POST.get("publish")
            is_pub = request.POST.get("is_pub")
            obj = models.Book.objects.create(title=title, price=price, pub_date=pub_date, publish=publish, is_pub=is_pub)
            print(obj.title)
            return redirect("/check/")
        return render(request, 'addbooks.html')




def delete(request,nid):
    models.Book.objects.filter(nid=nid).delete()
    return redirect("/check/")
def change(request,nid):
    book_list1=Book.objects.filter(nid=nid)
    book_list=book_list1.first()
    if request.method=="POST":
        print(request.POST)
        book_list1.update(title=request.POST.get('title'),price=request.POST.get('price'),pub_date=request.POST.get('pub_date'),publish=request.POST.get('publish'),is_pub=request.POST.get('is_pub'))
        return redirect('/check/')
    return render(request, 'change.html',{'book_list':book_list})
def check(request):
    book_list = models.Book.objects.all()
    return render(request,'check.html',{'book_list':book_list})
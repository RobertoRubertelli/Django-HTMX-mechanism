from django.shortcuts import render , redirect


# I'm importing what I need the model and the form
from .models import Company
from .forms import InsertCompany 
# Create your views here.


def Home(request):
    
    ## I'm building an empty context
    context={}

    ## I'm getting my queryset
    mydata = Company.objects.all()
    
    ## I'm giving my queryset to the context
    context={'mydata':mydata,}
    
    ## I'm choosing the return with the request.htmx
    if request.htmx:
        return render(request,'homepartial.html',context)
    return render(request,'home.html',context)

def NewCompany(request):
    
    ## I'm building an empty context
    context={}
    
    ## I'm getting the URL where I'm coming from in "myback", the view we left
    myback = request.META['HTTP_REFERER']
    ## with hx-patch in the "x" template button , I'm going back joining myback url.
    if request.method == 'PATCH':
        return redirect(myback)

    ## I'm opening the form to insert a new company in hx-get
    if request.method == 'GET':    
        form = InsertCompany()
        context={'form':form}
        return render(request,'insertcompany.html',context)    
    
    ## I'm confirming to add a new company and redirect to home in hx-post, in home view using if request.htmx: the view will update the partial html
    if request.method == 'POST':
        form = InsertCompany(request.POST)
        if form.is_valid():
            form.save()
        if request.htmx:
            return redirect('home')
        
def DeleteCompany(request,pk):
    
    ## I'm getting the id to delete
    mydata = Company.objects.get(id=pk)
    ## I'm deleting the id found
    mydata.delete()

    ##I'll back to home, the view home listen the request.htmx ,the DOM partial table will be updated
    return redirect('home')
    
def EditCompany(request,pk):

    ## I'm building an empty context
    context={}
 
    ## I'm getting the URL where I'm coming from in "myback", the view we left
    myback = request.META['HTTP_REFERER']
    ## with hx-patch in the "x" template button , I'm going back joining myback url.
    if request.method == "PATCH":
        return redirect(myback)
    
    ## I'm getting my company ID to edit    
    mydata = Company.objects.get(id=pk)
    ## I'm  filling the form with the ID data
    form = InsertCompany(instance=mydata)
    ## I'm filling the context for render
    context= {
            'form':form ,
            'mydata':mydata ,
            }    

    ## I'm updating the row and return with myback
    if request.method == 'POST':
        form = InsertCompany(request.POST, instance=mydata)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect(myback)
    
    ## I'm opening the edit html page 
    return render(request,'editcompany.html',context)

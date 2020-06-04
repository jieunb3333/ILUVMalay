from django.shortcuts import render, redirect
from .models import Portfolio
from .forms import CreatePortfolioForm

# Create your views here.
def portfolio(request):
    portfolioes = Portfolio.objects
    return render(request, 'portfolio/portfolio.html',{'portfolioes':portfolioes})

def portfolio_create(request):
    if request.method == "POST":
        form = CreatePortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio:list')
    else:
        form = CreatePortfolioForm()
        return render(request,'portfolio/portfolio_create.html',{'form':form})

def portfolio_update(request,portfolio_id):
    portfolio = Portfolio.objects.get(id=portfolio_id)
    if request.method == "POST":
        form = CreatePortfolioForm(request.POST, instance=portfolio)
        if form .is_valid():
            portfolio = form.save()
            return redirect('portfolio:list')
    else:
        form = CreatePortfolioForm(instance=portfolio)
        return render(request,'portfolio/portfolio_create.html',{'form':form})



def portfolio_delete(request,portfolio_id):
    portfolio = Portfolio.objects.get(id=portfolio_id)
    portfolio.delete()

    return redirect('portfolio:list')

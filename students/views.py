# students/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Portfolio
from .forms import PortfolioForm

def create_portfolio(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            portfolio = form.save(commit=False)
            if not portfolio.skills:
                portfolio.skills = '[]'
            portfolio.save()
            messages.success(request, 'Портфолио успешно сохранено!')
            return redirect('students:portfolio_list')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = PortfolioForm()
    # 👇 теперь шаблон services.html
    return render(request, 'main/services.html', {'form': form})


def portfolio_list(request):
    portfolios = Portfolio.objects.all().order_by('-created_at')
    return render(request, 'students/portfolio_list.html', {'portfolios': portfolios})

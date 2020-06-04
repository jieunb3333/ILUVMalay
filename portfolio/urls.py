from django.urls import path
import portfolio.views

app_name = 'portfolio'
urlpatterns = [
    path('', portfolio.views.portfolio,name='list'),
    path('create/', portfolio.views.portfolio_create,name='create'),
    path('portfolio_update/<int:portfolio_id>/', portfolio.views.portfolio_update,name='portfolio_update'),
    path('portfolio_delete/<int:portfolio_id>/', portfolio.views.portfolio_delete,name='portfolio_delete'),
]
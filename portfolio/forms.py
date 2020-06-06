from django import forms
from .models import Portfolio

class CreatePortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['image','pakage_num','pakage_name','max_person','pre_person','during_date','description']
from django import forms
from django.core.validators import validate_email

from . import telegram_orders_bot

class MakeAnOrderForm(forms.Form):
    name = forms.CharField()
    country = forms.CharField()
    email = forms.CharField()
    contact_way = forms.ChoiceField(choices=((1, 'Telegram'), (2, 'Instagram'),))
    account_name = forms.CharField()

    def clean_email(self):
        email = self.cleaned_data['email']
        if validate_email(email):
            self.add_error('email', 'Enter a valid email address')

    def send_order(self, request):
        name = request['name']
        country = request['country']
        email = request['email']
        if request['contact_way'] == '1':
            contact_way = 'Телеграмм'
        else:
            contact_way = 'Инстаграм'
        account_name = request['account_name']
        massege = f'Имя: {name} \nСтрана: {country} \nПочта: {email} \nСпособ связи: {contact_way} \nАккаунт: {account_name}'    
        
        telegram_orders_bot.new_order(massege)

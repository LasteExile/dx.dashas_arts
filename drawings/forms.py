from django import forms

from . import telegram_orders_bot

class MakeAnOrderForm(forms.Form):
    name = forms.CharField()
    country = forms.CharField()
    email = forms.CharField()
    contact_way = forms.ChoiceField(choices=((1, 'Telegram'), (2, 'Instagram'),))
    account_name = forms.CharField()
    

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

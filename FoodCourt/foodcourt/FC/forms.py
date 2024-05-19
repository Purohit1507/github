from django import forms
from .models import Order, OrderItem, MenuItem

class OrderForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Order
        fields = ['name', 'ps_no', 'dept_shop', 'mobile_number', 'date', 'break_time']

class OrderItemForm(forms.ModelForm):
    menu_item = forms.ModelMultipleChoiceField(
        queryset=MenuItem.objects.all(),
        widget=forms.SelectMultiple(attrs={'id': 'menu_item_select'})
    )

    class Meta:
        model = OrderItem
        fields = ['menu_item', 'quantity']

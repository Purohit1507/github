from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import MenuItem, Order, OrderItem, DayMenu, PunjabiItems
import datetime

def create_order(request):
    selected_date = request.GET.get('date', '')
    initial_data = {
        'name': request.GET.get('name', ''),
        'ps_no': request.GET.get('ps_no', ''),
        'dept_shop': request.GET.get('dept_shop', ''),
        'mobile_number': request.GET.get('mobile_number', ''),
        'date': selected_date if selected_date else datetime.date.today().strftime('%Y-%m-%d'),
    }

    print("Initial data:", initial_data)  # Debugging print

    day_menu_items = []
    punjabi_items = PunjabiItems.objects.all()

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        menu_item_ids = request.POST.getlist('menu_item')
        menu_item_quantities = request.POST.getlist('menu_item_quantity')
        random_menu_ids = request.POST.getlist('random_menu')
        random_menu_quantities = request.POST.getlist('random_menu_quantity')

        if order_form.is_valid():
            order = order_form.save()

            for menu_item_id, quantity in zip(menu_item_ids, menu_item_quantities):
                menu_item = MenuItem.objects.get(id=menu_item_id)
                OrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity)

            for random_menu_id, quantity in zip(random_menu_ids, random_menu_quantities):
                random_menu_item = MenuItem.objects.get(id=random_menu_id)
                OrderItem.objects.create(order=order, menu_item=random_menu_item, quantity=quantity)

            return redirect('order_success')
        else:
            print(order_form.errors)  # Print form errors to the console for debugging

    else:
        order_form = OrderForm(initial=initial_data)

        if selected_date:
            day_of_week = datetime.datetime.strptime(selected_date, '%Y-%m-%d').strftime('%A')
            try:
                day_menu = DayMenu.objects.get(day=day_of_week)
                day_menu_items = day_menu.items.all()
            except DayMenu.DoesNotExist:
                day_menu_items = []

    context = {
        'order_form': order_form,
        'day_menu_items': day_menu_items,
        'selected_date': selected_date,
        'punjabi_items': punjabi_items,
    }
    return render(request, 'FC/order_form.html', context)

def order_success(request):
    return render(request, 'FC/order_success.html')

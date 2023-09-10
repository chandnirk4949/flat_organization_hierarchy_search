from django.shortcuts import render

from .models import Employee


def search_employee(request):
    searched_employee = None
    direction = None  # Initialize direction variable
    child = None

    if request.method == 'POST':
        search_name = request.POST.get('search_name')
        direction = request.POST.get('direction')
        try:
            searched_employee = Employee.objects.get(name=search_name)
            child = searched_employee.get_child_by_direction(direction)
        except Employee.DoesNotExist:
            searched_employee = None
            child = None

    return render(request, 'search_employee.html', {
        'searched_employee': searched_employee,
        'direction': direction,
        'child': child,
    })


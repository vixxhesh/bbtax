from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Resource
from .forms import ResourceForm

@login_required
def upload_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resource_list')
    else:
        form = ResourceForm()
    return render(request, 'resource_store/upload_resource.html', {'form': form})

def resource_list(request):
    query = request.GET.get('q')
    if query:
        resources = Resource.objects.filter(title__icontains=query)
    else:
        resources = Resource.objects.all()
    return render(request, 'resource_store/resource_list.html', {'resources': resources, 'query': query})

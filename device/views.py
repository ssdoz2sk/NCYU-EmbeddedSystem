from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CreateDeviceForm
from .models import Device

# Create your views here.

@login_required
def device(request, pk):
    devices = Device.objects.filter(project=pk)
    return render(request, 'device/device.html', {'devices': devices})

@login_required
def new_device(request, pk):
    if request.method == 'POST':
        device_form = CreateDeviceForm(request.POST)
        if device_form.is_valid():
            new_device = device_form.save(commit=False)
            new_device.project = pk
            new_device.save()
            return redirect(new_device)

    else:
        device_form = CreateDeviceForm()

    return render(request,
                  'device/new_device.html',
                  {'device_form': device_form})

@login_required
def device_detail(request, pk):
    device = get_object_or_404(Device, pk=pk)
    return render(request, 'device/device/detail.html', {'device': device})
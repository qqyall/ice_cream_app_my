from django.shortcuts import render

from .forms import ContestForm


def proposal(request):
    form = ContestForm(request.GET or None)
    context = {'form': form}
    return render(request, 'contest/form.html', context)
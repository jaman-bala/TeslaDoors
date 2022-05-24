from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import ProductForm


# def index(request):
#     """Process images uploaded by users"""
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             img_obj = form.instance
#             return render(request, 'index.html',
#                           {'form': form, 'img_obj': img_obj})
#
#     else:
#         form = ProductForm()
#     return render(request, 'index.html', {'form': form, 'index': index})


class Index(FormView):
    form_class = ProductForm
    template_name = 'index.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        img_obj = form.instance
        return redirect('repos', {'form': form, 'img_obj': img_obj})


class ReposView(TemplateView):
    template_name = 'repos.html'
    success_url = reverse_lazy('repos')

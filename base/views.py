from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, DeleteView
from django.shortcuts import redirect, render
from .models import Product
from .forms import ProductForm


class Index(FormView, ListView):
    model = Product
    form_class = ProductForm
    context_object_name = 'informations'
    template_name = 'index.html'
    success_url = reverse_lazy('index')


    def form_valid(self, form):
        data = {}
        if self.request.method == 'POST':
            form = ProductForm(self.request.POST)
            if form.is_valid():
                form.save()
                return redirect('repos')
        else:
            error = 'Формат был неверной'
            form = ProductForm()
            data = {
                'form': form,
                'error': error
        }
        return render(self.request, 'repos.html', data)


class IndexDetail(DeleteView):
    model = Product.objects.all()
    template_name = 'code.html'
    context_object_name = 'code'
    success_url = reverse_lazy('code')
    queryset = Product.objects.all()


class ReposView(ListView):
    model = Product
    context_object_name = 'informationsi'
    template_name = 'repos.html'
    success_url = reverse_lazy('repos')
    paginate_by = 15



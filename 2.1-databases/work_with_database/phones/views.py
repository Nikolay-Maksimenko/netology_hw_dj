from django.shortcuts import render, redirect
from phones.models import Phone
from django.urls import reverse

def index(request):
    return redirect('catalog')

def show_catalog(request):
    sort = request.GET.get('sort')
    sort_mapper = {'id': 'id', 'name': 'name', 'min_price': 'price', 'max_price': '-price'}

    if sort not in sort_mapper.keys():
        sort = 'id'
    phones = Phone.objects.order_by(sort_mapper[sort]).all()
    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)

def show_product(request, slug):
    slugs = [slug[0] for slug in Phone.objects.values_list('slug')]
    if slug not in slugs:
        return redirect(reverse('catalog'))
    else:
        phones_obj = Phone.objects.filter(slug=slug)
        phone = [{'id': c.id, 'name': c.name, 'price': c.price, 'image': c.image, 'release_date': c.release_date, 'lte_exists': c.lte_exists, 'slug': c.slug} for c in phones_obj]
    template = 'product.html'
    context = {'phone': phones_obj[0]}
    return render(request, template, context)

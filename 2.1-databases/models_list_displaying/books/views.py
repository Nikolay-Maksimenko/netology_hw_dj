from django.shortcuts import render, redirect
from django.urls import reverse
from books.models import Book

def index(request):
    return redirect(reverse('books'))

def books_view(request, date=None):
    template = 'books/books_list.html'
    books = Book.objects.all().order_by('-pub_date')
    print(books)
    context = {'books': books}
    if date:
        pub_dates = sorted({book.pub_date for book in books})
        print(f'List {pub_dates}')
        books = [book for book in books if book.pub_date == date]
        print(f'Books {books}')
        current_page_index = pub_dates.index(date)
        try:
            prev_page = pub_dates[current_page_index - 1]
        except IndexError:
            prev_page = None

        try:
            next_page = pub_dates[current_page_index + 1]
        except IndexError:
            next_page = None

        context.update({'books': books, 'prev_page_url': prev_page, 'next_page_url': next_page})

    return render(request, template, context)

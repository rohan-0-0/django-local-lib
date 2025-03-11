from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.
def index(request):
    """View function for home page of site"""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books(status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is applied by default
    num_authors = Author.objects.count()
    
    num_genre_word = Genre.objects.filter(name__icontains="fiction")
                
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genre_word': num_genre_word,
    }
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
    # context_object_name = 'book_list'
    # # Get 5 books containing the war title
    # queryset = Book.objects.filter(title__icontains='war')[:5]
    # template_name = 'catalog/templates/books_list.html'

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    
class AuthorDetailView(generic.DetailView):
    model = Author
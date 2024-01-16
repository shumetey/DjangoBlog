from django.shortcuts import render, redirect
from .models import Book, Contact
from .forms import BookForm

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about-us.html')

def service(request):
    return render(request, 'services.html')

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('text')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create a new Contact object and save it to the database
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        # Redirect to a success page or perform other actions
        return redirect('contact')  # Replace 'success' with the URL name of your success page

    return render(request, 'contact.html')

def book_desc(request):
    # book = Book.objects.get(id=book_id)

    # context = {'book': book}
    return render(request, 'book_desc.html') #, context)

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'book_detail.html', {'book': book})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

def book_update(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        # form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': book})

def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('book_list')

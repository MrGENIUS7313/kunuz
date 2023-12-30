from .models import Category, News, Tags

def category(request):
    category = Category.objects.all()
    context = {
        'category' : category
    }
    return context
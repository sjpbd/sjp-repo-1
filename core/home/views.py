from django.shortcuts import render, get_object_or_404
from .models import Slide, About, DetailedAbout, Saint, Member, School, NewsItem, FAQ, Obituary
from django.http import JsonResponse

def home(request):
    slides = Slide.objects.all()
    about_us = About.objects.first()
    # news_items = NewsItem.objects.all()  # Fetch all news items
    news_items = NewsItem.objects.all()[:3]  # Get the latest 3 news items
    faqs = FAQ.objects.all()
    context = {
        'slides': slides,
        'about_us': about_us,
        'news_items': news_items,
        'faqs': faqs,
    }
    return render(request, 'home/home.html', context)

def about(request):
    about_us = About.objects.first()
    return render(request, 'home/about.html', {'about_us': about_us})

def slider(request):
    slides = Slide.objects.all()
    return render(request, 'home/slider.html', {'slides': slides})

def members(request):
    members_list = Member.objects.all()
    return render(request, 'home/members.html', {'members': members_list})

def obituary_view(request):
    obituaries = Obituary.objects.all().order_by('death_date')
    return render(request, 'home/obituary.html', {'obituaries': obituaries})

def contact(request):
    return render(request, 'home/contact.html')

# def detailed_about(request):
#     detailed_about_obj = DetailedAbout.objects.first()
#     return render(request, 'home/detailed_about.html', {'detailed_about': detailed_about_obj})
def detailed_about(request):
    try:
        detailed_about_obj = DetailedAbout.objects.first()
    except DetailedAbout.DoesNotExist:
        detailed_about_obj = None
    
    if detailed_about_obj:
        context = {
            'detailed_about': detailed_about_obj
        }
        return render(request, 'home/detailed_about.html', context)
    else:
        # Handle case where detailed about us content is not found
        return render(request, 'home/detailed_about.html', {'detailed_about': None})

def detailed_holyones(request):
    saints_list = Saint.objects.all()
    return render(request, 'home/detailed_holyones.html', {'saints': saints_list})

def saint_detail_api(request, saint_id):
    saint = get_object_or_404(Saint, id=saint_id)
    data = {
        'name': saint.name,
        'designation': saint.designation,
        'image_url': saint.image.url if saint.image else '',
        'detail': {
            'full_content': saint.detail.full_content
        }
    }
    return JsonResponse(data)

def school_table(request):
    schools_list = School.objects.all()
    return render(request, 'home/school_table.html', {'schools': schools_list})

def news_detail(request, slug):
    news_item = get_object_or_404(NewsItem, slug=slug)
    recent_news = NewsItem.objects.exclude(id=news_item.id)[:3]  # Exclude current news item and get latest 3
    context = {
        'news_item': news_item,
        'recent_news': recent_news,
    }
    return render(request, 'home/details_news.html', context)


# Constitution
from .models import Chapter

def chapter_list(request):
    chapters = Chapter.objects.all()
    return render(request, 'home/chapter_list.html', {'chapters': chapters})

def chapter_detail(request, pk):
    chapter = get_object_or_404(Chapter, pk=pk)
    chapters = Chapter.objects.all()  # Fetch all chapters for the navigation
    return render(request, 'home/chapter_detail.html', {'chapter': chapter, 'chapters': chapters})



# Photo Album
from django.views.generic import ListView, DetailView
from .models import Album, Photo

class AlbumListView(ListView):
    model = Album
    template_name = 'photos/album_list.html'
    context_object_name = 'albums'
    queryset = Album.objects.filter(is_visible=True)

class AlbumDetailView(DetailView):
    model = Album
    template_name = 'photos/album_detail.html'
    context_object_name = 'album'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = self.object.photos.all()
        return context

class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photos/photo_detail.html'
    context_object_name = 'photo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['album'] = self.object.album
        return context

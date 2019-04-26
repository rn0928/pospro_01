# Create your views here.
from django.template.response import TemplateResponse

from pospos.forms import PostingForm
from pospos.models import Posting #モデルインポート


def index(request):
    """メイン画面."""
    if request.method == 'POST':
        form = PostingForm(request.POST)
        if form.is_valid():
            # データの新規追加
            form.save()
    else:
        form = PostingForm()
        
        
    postings = Posting.objects.order_by('-created_at')[:10]
    return TemplateResponse(request,
                            'layout/index.html',
                            {'postings':postings,
                             'form':form})
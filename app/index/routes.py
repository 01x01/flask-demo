from .views import IndexView 
from . import index

index.add_url_rule('/',view_func=IndexView.as_view('index'))
from django.urls import path

from .views import IndexView, ShowView, ProFormView, SaveCommentView
from .forms import ProForm

app_name = 'crt_forms'


urlpatterns = [
    path('view/<int:id>/', ShowView.as_view(), name='crt-forms-show'),
    path('view/', IndexView, name='crt-forms-index'),
    path('new/', ProFormView.as_view([ProForm]), name='crt-pro-form'),
    path('comment/report/<int:report_id>/', SaveCommentView.as_view(), name='save-report-comment')
]

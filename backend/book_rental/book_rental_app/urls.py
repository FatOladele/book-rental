from django.urls import path
from .views import StudentView, SingleStudentView, BookView, RentalView, SingleRentalView, AnalyticsView

urlpatterns = [
    path('student', StudentView.as_view()),
    path('student/<str:pk>', SingleStudentView.as_view()),
    path('book', BookView.as_view()),
    path('rental', RentalView.as_view()),
    path('rental/<str:pk>', SingleRentalView.as_view()),
    path('analytics', AnalyticsView.as_view()),
]
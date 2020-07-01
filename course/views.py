from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from django.shortcuts import render, get_object_or_404
from membership.models import UserMembership
from .models import course, Lesson



class CourseListView(ListView):
    model = course

class CourseDetailView(DetailView):
    model = course

class LessonDetailView(LoginRequiredMixin, View):
    def get(self, request, course_slug, *args, **kwargs):
        course = get_object_or_404(course, slug=course_slug)
        lesson = get_object_or_404(Lesson, slug=lesson_slug)
        user_membership = get_object_or_404(UserMembership, user=request.user)
        user_membership_type = user_membership.membership_type
        course_allowed_mem_types = course.allowed_memberships.all()
        context = {'object': None}
        if course_allowed_mem_types.filter(membership_type=user_membership_type).exists():
            context = {'object': lesson}
        return render(request, "courses/lesson1_detail.html", context)

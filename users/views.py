from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import Group
from django.contrib.auth import login, logout
from users.forms import CustomRegistrationForm, AssignRoleForm, CreateGroupForm
from django.contrib import messages
from users.forms import LoginForm,CustomPasswordChangeForm,CustomPasswordResetForm,CustomPasswordResetConfirmForm,EditProfileForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Prefetch
# from events.urls import search
from events.models import Event,Category
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView,TemplateView,UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.views import PasswordChangeView,PasswordResetView,PasswordResetDoneView,PasswordChangeDoneView,PasswordResetCompleteView,PasswordContextMixin,PasswordResetConfirmView
from django.contrib.auth import get_user_model

User = get_user_model() 

def is_admin(user):
    return user.groups.filter(name='Admin').exists()


def sign_up(request):
    form = CustomRegistrationForm()
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data.get('password1'))
            user.is_active=False
            user.save()
            messages.success(
                request, 'A Confirmation mail sent to your email. Please check your email')
            return redirect('sign-in')
        else:
            print("Form is not valid")
    return render(request, 'registration/register.html', {"form": form})


class SignIn(LoginView):
    form_class = LoginForm

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        return next_url if next_url else super().get_success_url()

'''def sign_in(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # return redirect('')
    return render(request, 'registration/login.html', {'form': form})'''
    

'''def sign_in(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.groups.filter(name='Admin').exists():
                return redirect('admin-dashboard')
            else:
                return redirect('search')
    return render(request, 'registration/login.html', {'form': form})'''

@login_required
def sign_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('sign-in')
    

def activate_user(request, user_id, token):
    try:
        user = User.objects.get(id=user_id)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('sign-in')
        else:
            return HttpResponse('Invalid Id or token')

    except User.DoesNotExist:
        return HttpResponse('User not found')

Admin_dashboard_decorator=[
    user_passes_test(is_admin,login_url='no-permission')
]
@method_decorator(decorator=Admin_dashboard_decorator,name='dispatch')
class AdminDashboard(ListView):
    model=User
    template_name='admin/admin_dashboard.html'
    context_object_name = 'users'
    def get_queryset(self):
        users= User.objects.prefetch_related(
        Prefetch('groups', queryset=Group.objects.all(), to_attr='all_groups')
        ).all()
        for user in users:
            if user.all_groups:
                user.group_name = user.all_groups[0].name
            else:
                user.group_name = 'No Group Assigned'
        
        print(users)
        return users

    

'''@user_passes_test(is_admin, login_url='no-permission')
def admin_dashboard(request):
    users = User.objects.prefetch_related(
        Prefetch('groups', queryset=Group.objects.all(), to_attr='all_groups')
    ).all()

    print(users)

    for user in users:
        if user.all_groups:
            user.group_name = user.all_groups[0].name
        else:
            user.group_name = 'No Group Assigned'
    return render(request, 'admin/admin_dashboard.html', {"users": users})
'''

@user_passes_test(is_admin, login_url='no-permission')
def assign_role(request, user_id):
    user = User.objects.get(id=user_id)
    form = AssignRoleForm()

    if request.method == 'POST':
        form = AssignRoleForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data.get('role')
            user.groups.clear()  
            user.groups.add(role)
            messages.success(request, f"User {user.username} has been assigned to the {role.name} role")
            return redirect('admin-dashboard')

    return render(request, 'admin/assign_role.html', {"form": form})

@user_passes_test(is_admin, login_url='no-permission')
def create_group(request):
    form = CreateGroupForm()
    if request.method == 'POST':
        form = CreateGroupForm(request.POST)

        if form.is_valid():
            group = form.save()
            messages.success(request, f"Group {group.name} has been created successfully")
            return redirect('create-group')

    return render(request, 'admin/create_group.html', {'form': form})

@user_passes_test(is_admin, login_url='no-permission')
def group_list(request):
    groups = Group.objects.prefetch_related('permissions').all()
    return render(request, 'admin/group_list.html', {'groups': groups})

user_profile_decorator=[
    login_required(login_url='sign-in'),
]
@method_decorator(decorator=user_profile_decorator,name='dispatch')
class UserProfileView(TemplateView):
    template_name='accounts/profile.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        user=self.request.user
        context['name']=user.get_full_name
        context['username']=user.username
        context['email']=user.email
        context['member_since']=user.date_joined
        context['last_login']=user.last_login
        context['bio']=user.bio
        context['contact_number']=user.contact_number
        context['profile_images']=user.profile_image
        return context 


class CustomPasswordChangeView(PasswordChangeView):
    template_name='accounts/change_password.html'
    form_class=CustomPasswordChangeForm

class CustomPasswordChangeDone(PasswordChangeDoneView):
    template_name='accounts/password_change_done.html'

class CustomPasswordResetView(PasswordResetView):
    form_class=CustomPasswordResetForm
    template_name='registration/reset_password.html'
    success_url=reverse_lazy('sign-in')
    html_email_template_name='registration/reset_email.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['protocol']='https' if self.request.is_secure() else 'http'
        context['domain']=self.request.get_host()
        return context
    
    def form_valid(self, form):
        messages.success(self.request,'A reset email send.Please check your email')
        return super().form_valid(form)
    
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class=CustomPasswordResetConfirmForm
    template_name='registration/reset_password.html'
    success_url=reverse_lazy('sign-in')

    def form_valid(self, form):
        messages.success(self.request,'Password reset successfully')
        return super().form_valid(form)

'''class EditProfileView(UpdateView):
    form_class=EditProfileForm
    template_name='accounts/update_profile.html'
    context_object_name='form'
    
    def get_object(self):
        return self.request.user
    
    def get_form_kwargs(self):
        kwargs=super().get_form_kwargs()
        kwargs['userprofile']= UserProfile.objects.get(user=self.request.user)
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile=UserProfile.objects.get(user=self.request.user)
        context["form"] = self.form_class(instance=self.object,userprofile=user_profile)
        return context
    
    def form_valid(self, form):
        form.save(commit=True)
        return redirect('profile')'''

edit_profile_decorator=[
    login_required(login_url='sign-in'),
]
@method_decorator(decorator=edit_profile_decorator,name='dispatch')
class EditProfileView(UpdateView):
    form_class=EditProfileForm
    template_name='accounts/update_profile.html'
    context_object_name='form'
    
    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        form.save()
        return redirect('profile')


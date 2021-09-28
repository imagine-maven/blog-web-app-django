from typing import ContextManager
from django.shortcuts import render, redirect

# importing user creation form for creating a form
# from django.contrib.auth.forms import UserCreationForm

# importing messages to display a flash message
from django.contrib import messages
# importing user register form from forms.py
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

#login required decorator to access profile page only when  logged in 
from django.contrib.auth.decorators import login_required

# Use UserRegisterForm in place of UserCreationForm 
# because it inherits everything from UserCreationForm

# register view method
def register(request):
    # creating a form instance
    if request.method == 'POST':
        # submitting data from UserRegisterForm and storing in form instance
        form = UserRegisterForm(request.POST)
        # checking the validity of the form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # flash message
            messages.success(request, f'Your account has been created! You can now log in')
            return redirect('login')
            
    else:
        # redirects to an empty form
        form = UserRegisterForm()
    return render(request, 'users/register.html', { 'form' : form }) 

# profile view method
@login_required
def profile(request):
    # creating instances of the UserUpdateForm and profileUpdateForm
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES , instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
            
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    # passing forms in a dict
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)


# different types of messages
# messages.debug
# messages.info
# messages.warning
# messages.success
# messages.error
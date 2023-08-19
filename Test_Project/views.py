from django.shortcuts import render, redirect
from profiles.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
def signup(request):
    profile_id = request.session.get('ref_profile')
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        if profile_id is not None:
            recommended_by_profile = Profile.objects.get(id=profile_id)
            instance = form.save()
            registered_user = User.objects.get(id=instance.id)
            registered_profile = Profile.objects.get(user=registered_user)
            registered_profile.referred_by = recommended_by_profile.user
            registered_profile.save()  
        else:
            instance = form.save() 
        username = form.cleaned_data.get('username')
        phone= form.cleaned_data.get('phone') 
        password = form.cleaned_data.get('password1')  
        user = authenticate(username=username, phone=phone, password=password)
        login(request, user)
        return redirect('main_view')
    context = {'form': form}
    return render(request, 'signup.html', context)

def main_view(request, *args, **kwargs):
    invite_code = str(kwargs.get('ref_code'))
    try:
        profile = Profile.objects.get(invite_code=invite_code)
        request.session['ref_profile'] = profile.id
        print('id', profile.id)
    except Profile.DoesNotExist:
        pass
    return render(request, 'main.html', {})

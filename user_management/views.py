from django.shortcuts import render, redirect
from .models import CustomUser, Students, Teachers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth import logout

def register_view(request):
    if request.method == 'POST':
        try:
            user_name = request.POST['user_name']
            email = request.POST['email']
            password = request.POST['password']
            role = request.POST['role']
            address = request.POST.get('address')
            dob = request.POST['dob']
            profile_pic = request.FILES.get('profile_pic')  
            phone_number = request.POST['phone_number']
            gender = request.POST.get('gender')

            user = CustomUser(
                username=email,
                user_name=user_name,
                email=email,
                password=make_password(password), 
                role=role,
                address=address,
                dob=dob,
                profile_pic=profile_pic,
                phone_number=phone_number,
                gender=gender
            )
            user.save()

            if role == 'student':
                Students.objects.create(
                    user=user,
                    guardian_name=request.POST.get('guardian_name'),
                    guardian_contact=request.POST.get('guardian_contact')
                    
                )
            elif role == 'teacher':
                Teachers.objects.create(
                    user
                    =user,
                    qualification=request.POST.get('qualification'),
                    skills=request.POST.get('skills'),
                    experience=request.POST.get('experience')
                )

            return redirect('login')
        
        except IntegrityError:
            error_msg = "This email is already registered. Please try logging in or use another email."
            return render(request, 'user_management/register.html', {'error': error_msg})

    return render(request, 'user_management/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.role == 'student':
                return redirect('student_dashboard')
            elif user.role == 'teacher':
                return redirect('guide_dashboard')
        else:
            return render(request, 'user_management/login.html', {'error': 'Invalid credentials'})
    return render(request, 'user_management/login.html')

@login_required
def student_dashboard(request):
    return render(request, 'user_management/student_dashboard.html')

@login_required
def student_dashboard(request):
    try:
        student = Students.objects.get(user=request.user)
    except Students.DoesNotExist:
        student = None

    return render(request, 'user_management/student_dashboard.html', {
        'student': student,           
        'user': request.user          
    })

@login_required
def guide_dashboard(request):  
    return render(request, 'user_management/guide_dashboard.html') 


@login_required
def edit_student_profile(request):
    try:
        student = Students.objects.get(user=request.user)
    except Students.DoesNotExist:
        student = Students.objects.create(user=request.user)

    if request.method == 'POST':
        # Update CustomUser fields
        request.user.address = request.POST.get('address')
        request.user.phone_number = request.POST.get('phone_number')
        request.user.gender = request.POST.get('gender')
        request.user.save()
        profile_pic = request.FILES.get('profile_pic')

        if profile_pic:
            request.user.profile_pic = profile_pic
            request.user.save()
    
        # Update Students fields
        student.guardian_name = request.POST.get('guardian_name')
        student.guardian_contact = request.POST.get('guardian_contact')
        student.save()

        return redirect('student_dashboard')

    return render(request, 'user_management/edit_student_profile.html', {'student': student})


@login_required
def edit_guide_profile(request):
    try:
        guide = Teachers.objects.get(user = request.user)
    except Teachers.DoesNotExist:
        guide = Teachers.objects.create(user = request.user) 
    if request.method == 'POST':
        # update coustom model
        request.user.address = request.POST.get('address')
        request.user.phone_number = request.POST.get('phone_number')
        request.user.gender = request.POST.get('gender')
        request.user.portfile_pic = request.FILES.get('profile_pic')
        request.user.save()

        # update teacher model
        guide.qualification = request.POST.get('qualification')
        guide.skills = request.POST.get('skills')
        guide.experience = request.POST.get('experience')
        guide.save()

        return redirect('guide_dashboard')

    return render(request, 'user_management/edit_guide_profile.html', {'guide': guide})

@login_required
def logout_view(request):
    logout(request)
    return render(request, 'user_management/logout.html')




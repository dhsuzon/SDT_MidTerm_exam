from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .forms import CarForm,CommentForm
from django.views.generic import DetailView
from .models import CarModel
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegisterForm,UserChangeData
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@login_required
def Add_Car(request):
    if request.method == "POST":
        form = CarForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addcar')
    else:
         form = CarForm()
    return render(request, 'car_add.html',{'form':form})


@method_decorator(login_required, name='dispatch')
class DetailCarView(DetailView):
    model = CarModel
    pk_url_kwarg = 'id'
    template_name ="Car_Details.html"
    
    def post(self,request,*args,**kwargs):
        car = self.get_object()
        if self.request.method == 'POST':
              form = CommentForm(self.request.POST)
              if form.is_valid():
                  comment =form.save(commit=False)
                  comment.car = car
                  comment.save()
              return self.get(self,request,*args,**kwargs)
       
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            car = self.get_object()
            context['car'] = car
            context['Comments'] = car.comments.all()
            context['form'] = CommentForm()
            return context
        
class SignUp(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'signup.html'
    success_url = reverse_lazy('signup')
    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, "Your account has been created successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return self.render_to_response({'form': form})
    
    

class UserloginView(LoginView):
    template_name = 'Login.html'
    success_url = reverse_lazy("Profile")
    def form_valid(self, form):
        messages.success(self.request, "Your account has been logged successfully!")
        return super().form_valid(form)
    
    def get_success_url(self):
        return self.success_url

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return self.render_to_response({'form': form})
    

@login_required
def UserProfile(request):
     return render(request, 'Profile.html')



@method_decorator(login_required, name='dispatch')
class UserProfileEdit(UpdateView):
    model = User
    form_class = UserChangeData 
    pk_url_kwarg  = 'id'
    template_name = 'User_Data_edit.html'
    success_url = reverse_lazy('Profile')

    def form_valid(self, form):
        form.save() 
        messages.success(self.request, "Your account has been updated successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return self.render_to_response({'form': form})
    
    
class UserProfileLogout(LogoutView):
    next_page = 'login'
    
   
    
    
@login_required
def buy_now(request,Car_id):
    car = CarModel.objects.get(id=Car_id)
    if car.quantity >0:
        car.quantity -= 1
        car.save()
    return render(request, 'Profile.html', {'car': car})



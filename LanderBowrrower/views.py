from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from accounts.models import Borrower, User,Lender
# Create your views here.
from .forms import BorrowerForm

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"


class BorrowerRegister(TemplateView):
    # template_name = "borrower_register.html"
    # form = BorrowerForm()
    def get(self, request, *args, **kwargs):
        # form = BorrowerForm()
        return render(request, 'borrower_register.html')

    def post(self, request, *args, **kwargs):
        username=request.POST.get('username')
        password=request.POST.get('password')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        address=request.POST.get('address')
        creditrating=request.POST.get('creditrating')
        sscard=request.POST.get('sscard')
        print(password)
        # form =BorrowerForm(request.POST)
        # print( form['address'].value())
        # print(" post request ljljllllllll")
        # form = BorrowerForm(request.POST)
        # print(form)
        # if form.is_valid():
        #     form.save()
        #     return render(request, 'index.html')
        # else:
        print(" ooooooooooojhhhhhhhhhhhhhh")

        user = User.objects.create(username=username, password=password, is_borrower=True,first_name=firstname,last_name=lastname,address=address)
        user.set_password(password)
        user.save()
        print(user)

        sscard = request.POST.get('sscard')
        borrower = Borrower.objects.create(user=user,  credit_rating=creditrating,
                                           sscard=sscard)
        return render(request, 'home.html')


class LanderRegister(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'lander_register.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname= request.POST.get('lastname')
        entityname = request.POST.get('entityname')

        availablefund = request.POST.get('availablefund')
        loanrange = request.POST.get('loanrange')
        minloansize = request.POST.get('minloansize')
        maxloansize = request.POST.get('maxloansize')
        mincradit = request.POST.get('mincradit')
        maxltv = request.POST.get('maxltv')
        maxltc = request.POST.get('maxltc')
        states = request.POST.get('states')
        propertytpe = request.POST.get('propertytpe')
        foreclousure = request.POST.get('foreclousure')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        if foreclousure == None:
            foreclousure = False
        else:
            foreclousure = True

        print(username)
        print(firstname)
        print(lastname)
        print(entityname)
        print(availablefund)
        print(loanrange)
        print(minloansize)
        print(maxloansize)
        print(mincradit)
        print(maxltv)
        print(maxltc)
        print(states)
        print(propertytpe)
        print(foreclousure)
        print(password)
        print(confirmpassword)

        print(" ooooooooooojhhhhhhhhhhhhhh")

        lander_user = User.objects.create(username=username, password=password, is_lender=True,first_name=firstname,last_name=lastname)
        lander_user.set_password(password)
        lander_user.save()
        print(lander_user)
        # # user = super().save(commit=False)
        # # user.is_borrower = True
        # # user.save()
        # name = request.POST.get('name')
        # address = request.POST.get('address')
        # credit_rating =request.POST.get('creditrating')
        # sscard =request.POST.get('sscard')
        # borrower = Borrower.objects.create(user=user, name=name, address=address, credit_rating=credit_rating,
        #                                    sscard=sscard)
        lander=Lender.objects.create(user=lander_user,entity_name=entityname,available_funds=availablefund,loan_range=loanrange,min_loan_size=minloansize,max_loan_size=maxloansize,min_credit=mincradit,max_ltv=maxltv,max_ltc=maxltc,states=states,property_type=propertytpe,foreclosure=foreclousure)
        return render(request, 'home.html')








# Create your views here.
@login_required
def home(request):
    if request.user.is_borrower:
        return render(request, 'borrower_home.html')
    if request.user.is_lender:
     return render(request, 'home.html')


# Create your views here.
@login_required
def single(request):
    return render(request, 'single.html')


@login_required
def SubmitRequest(request):
    return render(request, 'submit_request.html')



@login_required(login_url='login')
def profile(request):
    if request.user.is_borrower:
        bowwer_obj=Borrower.objects.filter(user__username=request.user.username).first()
        print('jimy')
        print(bowwer_obj.user.first_name)
        return render(request, 'profile.html' ,{'bowwer_obj':bowwer_obj})
    if request.user.is_lender:
        lander = Lender.objects.filter(user__username=request.user.username).first()
        return render(request, 'lander_profile.html',{'lander':lander})

@login_required(login_url='login')
def editProfile(request):
    if request.user.is_borrower:
        if request.method=="GET":
            print('edit barrower profile')
            bowwer_obj = Borrower.objects.filter(user__username=request.user.username).first()
            return render(request, 'borrower_edit_profile.html',{'bowwer_obj':bowwer_obj})
        if request.method == "POST":
            print('POST MEYHOD')
            bowwer_obj = Borrower.objects.filter(user__username=request.user.username).first()
            user=User.objects.filter(username=request.user.username).first()
            firstname= request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            craditrating = request.POST.get('craditrating')
            email= request.POST.get('email')
            adress = request.POST.get('adress')
            sscard = request.POST.get('sscard')
            print(sscard)
            user.first_name=firstname
            user.last_name= lastname
            user.email = email
            user.address = adress
            user.save()
            bowwer_obj.credit_rating= craditrating
            bowwer_obj.sscard=sscard
            bowwer_obj.save()
            bowwer_obj = Borrower.objects.filter(user__username=request.user.username).first()
            return render(request, 'profile.html', {'bowwer_obj': bowwer_obj})
    if request.user.is_lender:
        print('edit lander profile')
        if request.method=="GET":
            print('edit barrower profile')
            lander = Lender.objects.filter(user__username=request.user.username).first()
            return render(request, 'lander_edit_profile.html',{'lander':lander})
        if request.method == "POST":
            print('POST MEYHOD')
            lender = Lender.objects.filter(user__username=request.user.username).first()
            user=User.objects.filter(username=request.user.username).first()
            firstname= request.POST.get('firstname')
            lastname= request.POST.get('lastname')
            entityname= request.POST.get('entityname')
            loanrange= request.POST.get('loanrange')
            minloansize= request.POST.get('minloansize')
            maxltv= request.POST.get('maxltv')
            propertytype= request.POST.get('propertytype')
            email= request.POST.get('email')
            adress= request.POST.get('adress')
            availablefund= request.POST.get('availablefund')
            minimumcradit= request.POST.get('minimumcradit')
            maxloansize= request.POST.get('maxloansize')
            maxltc= request.POST.get('maxltc')
            state= request.POST.get('state')
            foreclousure= request.POST.get('foreclousure')
            if foreclousure==None:
                foreclousure=False
            else:
                foreclousure = True

            user.first_name=firstname
            user.last_name= lastname
            user.email = email
            user.address = adress
            user.save()
            lender.entity_name= entityname
            lender.loan_range=loanrange
            lender.max_loan_size=maxloansize
            lender.min_loan_size=minloansize
            lender.max_ltv=maxltv
            lender.max_ltc=maxltc
            lender.property_type=propertytype
            lender.available_funds=availablefund
            lender.min_credit=minimumcradit
            lender.states=state
            lender.foreclosure=foreclousure
            lender.save()
            lender_obj = Lender.objects.filter(user__username=request.user.username).first()
            return render(request, 'lander_profile.html', {'lander': lender_obj})



@login_required(login_url='login')
def editPassword(request):
        if request.method=="GET":
            print('editPassword')
            return render(request, 'change_password.html')
        if request.method == "POST":
            user = User.objects.filter(username=request.user.username).first()
            Password= request.POST.get('Password')
            user.set_password(Password)
            user.save()
            print('post')
            return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')


def validate_username(request):
    print(' in validate')
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

from django import forms

from accounts.models import Borrower,User

class BorrowerForm(forms.Form):
    name = forms.CharField(max_length=255, required=True, help_text='Required.')
    address = forms.CharField(max_length=255, required=True, help_text='Required.')
    credit_rating = forms.CharField(max_length=255, required=True, help_text='Required.')
    sscard = forms.CharField(max_length=255, required=False, help_text='Optional.')

    class Meta(forms.ModelForm):
        model = User
        fields = ('username','first_name','last_name' ,'password','name', 'address', 'credit_rating', 'sscard')


    def save(self):
        print('clll save')
        user = super().save(commit=False)
        user.is_borrower = True
        user.save()
        name = self.cleaned_data.get('name')
        address = self.cleaned_data.get('address')
        credit_rating = self.cleaned_data.get('credit_rating')
        sscard = self.cleaned_data.get('sscard')
        borrower = Borrower.objects.create(user=user, name=name, address=address, credit_rating=credit_rating,
                                           sscard=sscard)
        print(borrower.address)
        return user
    # class Meta:
    #     model = Borrower
    #     fields = ('first_name','name', 'address','credit_rating','sscard')

        # def __init__(self, *args, **kwargs):
        #     user = kwargs.pop('user', '')
        #     super(UerForm, self).__init__(*args, **kwargs)
        #     self.fields['user_defined_code'] = forms.ModelChoiceField(
        #         queryset=UserDefinedCode.objects.filter(owner=user))
        #     self.fields['unique_code'] = forms.CharField(max_length=15)
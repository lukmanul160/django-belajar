from django import forms

class ContactForm(forms.Form):
    nama_lengkap    = forms.CharField(
        label = 'Nama Lengkap',
        max_length=20,
        widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Masukkan Nama Lengkap Anda',
            }
        )
    )

    choices = [
        ('P','Pria'),
        ('W','Wanita')
    ]
    jenis_kelamin = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs={
                'class':'form-check-input',
            }
        ),
        choices=choices
        )

    tanggal_lahir = forms.DateField(
        widget=forms.SelectDateWidget(
            years=range(1945,2019,1),
            attrs={
                'class':'form-control col-sm-2'
            }
        )
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Isi dengan email anda'
            }
        )
    )

    alamat = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
        }
    ))

    agree = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class':'form-check-input'
            }
        )
    )
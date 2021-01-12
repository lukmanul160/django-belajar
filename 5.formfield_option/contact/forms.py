from django import forms

class ContactForm(forms.Form):
    nama_lengkap = forms.CharField(max_length=30)
    GENDER = (
        ('P','Pria'),
        ('W','Wanita')
    )
    jenis_kelamin = forms.ChoiceField(
        widget = forms.RadioSelect,
        choices=GENDER)

    email = forms.EmailField(label='Alamat Email')
    alamat = forms.CharField(required=False,
    widget=forms.Textarea,
    max_length=100 )
    # kode_pos = forms.IntegerField(required=False)
    # kota = forms.CharField(required=False)
    # provinsi = forms.CharField(required=False)
    TAHUN = range(1945,2018,1)
    tanggal_lahir = forms.DateField(widget = forms.SelectDateWidget(years=TAHUN))
    agree = forms.BooleanField()


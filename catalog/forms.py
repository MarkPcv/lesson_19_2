from django import forms

from catalog.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    restricted_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                        'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        exclude = ('date_modified',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        if cleaned_data.lower() in self.restricted_words:
            raise forms.ValidationError('Данное название нельзя использовать')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        data_by_word = cleaned_data.lower().split()
        for word in data_by_word:
            if word in self.restricted_words:
                raise forms.ValidationError(
                    'Данное описание содержит запрещённые слова')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
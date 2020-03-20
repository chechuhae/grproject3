from django.forms import DateTimeInput

# Все что делают "виджеты" в этом фреймворке, это генерируют html код\формы с автоматической привязкой к данным моделей
# template_name это путь к куску html, который этот виджет и будет вставлять на твою страницу. Это просто кусок html
class BootstrapDateTimePickerInput(DateTimeInput):
    template_name = 'widgets/bootstrap_datetimepicker.html'

    def get_context(self, name, value, attrs):
        datetimepicker_id = 'datetimepicker_{name}'.format(name=name)
        if attrs is None:
            attrs = dict()
        attrs['data-target'] = '#{id}'.format(id=datetimepicker_id)
        attrs['class'] = 'form-control datetimepicker-input'
        context = super().get_context(name, value, attrs)
        context['widget']['datetimepicker_id'] = datetimepicker_id
        return context
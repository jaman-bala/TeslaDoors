from django.db import models
from django.core.files import File


import qrcode
from io import BytesIO
from PIL import Image, ImageDraw
from ckeditor_uploader.fields import RichTextUploadingField


class Product(models.Model):
    number_doc = models.CharField(verbose_name="Номер Договора", unique=True, max_length=200)
    adress = models.CharField(verbose_name="Адрес", max_length=200)
    title = models.CharField(verbose_name="Вид изделия", blank=True, null=True, max_length=200)
    phone = models.CharField(verbose_name="Номер телефона", max_length=10)
    first_name = models.CharField(verbose_name="Имя", max_length=200)
    last_name = models.CharField(verbose_name="Фамилия", max_length=200)
    sum = models.CharField(verbose_name="Сумма", max_length=10)
    comments =  RichTextUploadingField('Комментарии')
    file1 = models.FileField("Прикрепить файл", blank=True, null=True, upload_to="file")
    file2 = models.FileField("Прикрепить файл", blank=True, null=True, upload_to="file")
    file3 = models.FileField("Прикрепить файл", blank=True, null=True, upload_to="file")
    file4 = models.FileField("Прикрепить файл", blank=True, null=True, upload_to="file")
    file5 = models.FileField("Прикрепить файл", blank=True, null=True, upload_to="file")
    file6 = models.FileField("Прикрепить файл", blank=True, null=True, upload_to="file")
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)
    is_active = models.BooleanField("Активный", default=True)
    created = models.DateTimeField(verbose_name="Дата создание", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return str(self.number_doc)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.number_doc)
        canvas = Image.new('RGB', (390, 390), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.number_doc}' + '.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

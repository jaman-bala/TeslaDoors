from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


class Category(models.Model):
    name = models.CharField("Название", max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Категории')
    name = models.CharField(verbose_name="Название", max_length=200)
    number_doc = models.CharField(verbose_name="Номер Договора", unique=True, max_length=200)
    image = models.ImageField("Прикрепить файл", blank=True, null=True, upload_to="products/images/")
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
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.number_doc}' + '.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

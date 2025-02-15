from django.db import models


class SeoSettings(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sayt nomi")
    favicon = models.FileField(upload_to='favicons/', verbose_name="Favicon")

    site_author = models.TextField(verbose_name="Sayt muallifi")
    site_keywords = models.TextField(verbose_name="Sayt kalit so‘zlari")
    site_description = models.TextField(verbose_name="Sayt tavsifi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "SEO Sozlamasi"
        verbose_name_plural = "SEO Sozlamalari"

class SiteSettings(models.Model):
    header_logo = models.ImageField(upload_to='logos/', verbose_name="Bosh logo")
    footer_logo = models.ImageField(upload_to='logos/', verbose_name="Pastki logo")

    phone_number = models.CharField(max_length=255, verbose_name="Telefon raqami")
    email = models.CharField(max_length=255, null=True, blank=True, verbose_name="Email")
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name="Manzil")

    footer_text = models.TextField(verbose_name="Pastki matn")
    copyright_text = models.TextField(verbose_name="Mualliflik huquqi matni")

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = "Sayt Sozlamasi"
        verbose_name_plural = "Sayt Sozlamalari"

class SocialNetworks(models.Model):
    title = models.CharField(max_length=255, verbose_name="Nomi")
    icon = models.CharField(max_length=255, verbose_name="Ikonkasi")
    link = models.CharField(max_length=255, verbose_name="Havolasi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ijtimoiy Tarmoq"
        verbose_name_plural = "Ijtimoiy Tarmoqlar"

class TelegramBotConfig(models.Model):
    username = models.CharField(max_length=255, verbose_name="Bot usernamesi")
    token = models.TextField(verbose_name="Tokeni")

    admins = models.CharField(max_length=255, verbose_name="Adminlar")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Telegram Bot Konfiguratsiyasi"
        verbose_name_plural = "Telegram Bot Konfiguratsiyalari"

from django.db import models
import jalali_date
import datetime
from django.contrib.auth.models import User

# Create your models here.


class RANK_CHOISES(models.IntegerChoices):
    SOTVAN_3 = 7, 'ستوانسوم'
    SOTVAN_2 = 8, 'ستواندوم'
    SOTVAN_1 = 9, 'ستوانیکم'
    SARGORD = 10, 'سرگرد'
    SARHANG_2 = 11, 'سرهنگ 2'
    SARHANG = 12, 'سرهنگ تمام'
    SARTIP_2 = 13, 'سرتیپ 2'
    SARTIP = 14, 'سرتیپ'


class GUILD_CHOISES(models.IntegerChoices):
    PIADE = 0, 'پیاده'
    BEHDASHT = 1, 'بهداشت و درمان'


class LEVEL_CHOICES(models.IntegerChoices):
    NONE = 0, 'هیچ'
    VERY_LOW = 1, 'خیلی کم'
    LOW = 2, 'کم'
    MODERATE = 3, 'متوسط'
    HIGH = 4, 'زیاد'
    VERY_HIGH = 5, 'خیلی زیاد'


class TIME_STEP_CHOICES(models.IntegerChoices):
    DAILY = 0, 'روزانه'
    WEEKLY = 1, 'هفتگی'
    MONTHLY = 2, 'ماهانه'


class JALALI_MONTHS(models.IntegerChoices):
    FARVARDIN = 1, 'فروردین'
    ORDIBEHEST = 2, 'اردیبهشت'
    KHORDAD = 3, 'خرداد'
    TIR = 4, 'تیر'
    MORDAD = 5, 'مرداد'
    SHAHRIVAR = 6, 'شهریور'
    MEHR = 7, 'مهر'
    ABAN = 8, 'آبان'
    AZAR = 9, 'آذر'
    DEI = 10, 'دی'
    BAHMAN = 11, 'بهمن'
    ESFAND = 12, 'اسفند'


def get_this_jalali_month_index():
    return jalali_date.jdatetime.datetime.now().month


class Place(models.Model):
    name = models.CharField(max_length=64, verbose_name='نام')
    correspondence = models.ForeignKey(
        to=User, on_delete=models.PROTECT, related_name='places', verbose_name='مسئول')

    class Meta:
        verbose_name = 'یگان'
        verbose_name_plural = 'یگان ها'

    def __str__(self) -> str:
        return self.name


class Major(models.Model):
    name = models.CharField(max_length=64, verbose_name='نام')

    class Meta:
        verbose_name = 'تخصص'
        verbose_name_plural = 'تخصص ها'

    def __str__(self) -> str:
        return self.name


class Subject(models.Model):
    first_name = models.CharField(max_length=64, verbose_name='نام')
    last_name = models.CharField(max_length=64, verbose_name='نشان')
    organization_id = models.CharField(
        max_length=12, verbose_name='شماره کارگزینی')
    rank = models.PositiveSmallIntegerField(
        choices=RANK_CHOISES.choices, default=RANK_CHOISES.SOTVAN_1.value, verbose_name='درجه')
    serve_place = models.ForeignKey(
        to=Place, on_delete=models.CASCADE, related_name='subjects', verbose_name='محل خدمت')
    major = models.ForeignKey(
        to=Major, on_delete=models.CASCADE, related_name='subjects', verbose_name='تخصص')
    monthly_mandatory_serve_time_hours = models.PositiveIntegerField(
        null=True, blank=True, verbose_name='ساعات خدمت موظف ماهیانه')

    class Meta:
        verbose_name = 'شخص'
        verbose_name_plural = 'اشخاص'

    def __str__(self) -> str:
        rank = self.get_rank_display()
        return f'{rank} {self.first_name} {self.last_name} | {self.organization_id}'


class SubjectRecord(models.Model):
    created_at = models.DateTimeField(
        verbose_name='زمان ایجاد', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='زمان تغییر', auto_now=True)
    time_step = models.PositiveSmallIntegerField(
        choices=TIME_STEP_CHOICES.choices, default=TIME_STEP_CHOICES.MONTHLY.value, verbose_name='بازه زمانی')
    time = models.PositiveSmallIntegerField(choices=JALALI_MONTHS.choices, default=get_this_jalali_month_index, verbose_name='زمان')
    subject = models.ForeignKey(
        to=Subject, on_delete=models.CASCADE, related_name='records', verbose_name='شخص')
    subject_place = models.ForeignKey(
        to=Place, on_delete=models.CASCADE, related_name='records', verbose_name='محل خدمت')
    subject_rank = models.PositiveSmallIntegerField(
        choices=RANK_CHOISES.choices, default=RANK_CHOISES.SOTVAN_1.value, verbose_name='درجه')
    outpatient_visit_counts = models.PositiveSmallIntegerField(
        default=0, verbose_name='تعداد ویزیت سرپایی بیمار')
    hospitalized_patients_counts = models.PositiveSmallIntegerField(
        default=0, verbose_name='تعداد بیمار بستری شده')
    total_served_time = models.TimeField(default=datetime.time(
        0, 0, 0, 0), verbose_name='مجموع ساعات خدمت')
    additive_served_time = models.TimeField(default=datetime.time(
        0, 0, 0, 0), verbose_name='مجموع ساعات اضافه کاری')

    class Meta:
        verbose_name = 'گزارش مربوط به شخص'
        verbose_name_plural = 'گزارشات مربوط به اشخاص'

    def __str__(self) -> str:
        return f'{self.subject} | '

from django.db import models
import json

class Portfolio(models.Model):
    EDUCATION_LEVELS = [
        ('school', 'Среднее образование'),
        ('college', 'Среднее специальное'),
        ('bachelor', 'Бакалавриат'),
        ('master', 'Магистратура'),
        ('phd', 'Аспирантура'),
    ]
    
    # Основная информация
    last_name = models.CharField(
        max_length=100, 
        verbose_name="Фамилия",
        help_text="Введите вашу фамилию"
    )
    first_name = models.CharField(
        max_length=100, 
        verbose_name="Имя",
        help_text="Введите ваше имя"
    )
    email = models.EmailField(
        blank=True, 
        null=True, 
        verbose_name="Email",
        help_text="your.email@example.com"
    )
    phone = models.CharField(
        max_length=20, 
        blank=True, 
        null=True, 
        verbose_name="Телефон",
        help_text="+7 (XXX) XXX-XX-XX"
    )
    
    # Образование
    school = models.CharField(
        max_length=200, 
        blank=True, 
        null=True, 
        verbose_name="Учебное заведение",
        help_text="Название учебного заведения"
    )
    education_level = models.CharField(
        max_length=20, 
        choices=EDUCATION_LEVELS, 
        blank=True, 
        null=True,
        verbose_name="Уровень образования"
    )
    specialization = models.CharField(
        max_length=200, 
        blank=True, 
        null=True, 
        verbose_name="Специализация",
        help_text="Ваша специальность или направление"
    )
    
    # Опыт и навыки
    experience = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Опыт работы",
        help_text="Опишите ваш опыт работы, стажировки, проекты..."
    )
    hobbies = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Увлечения",
        help_text="Опишите ваши хобби и интересы..."
    )
    skills = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Навыки",
        help_text="Список ваших навыков"
    )
    achievements = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Достижения",
        help_text="Расскажите о ваших наградах, проектах, сертификатах..."
    )
    goals = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Карьерные цели",
        help_text="Кем вы хотите стать? Каких целей планируете достичь?"
    )
    
    # Метаданные
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name="Дата обновления"
    )

    class Meta:
        verbose_name = "Портфолио"
        verbose_name_plural = "Портфолио"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    @property
    def skills_list(self):
        """
        Возвращает список навыков из JSON строки
        """
        try:
            if self.skills:
                return json.loads(self.skills)
            return []
        except (json.JSONDecodeError, TypeError):
            return []

    @skills_list.setter
    def skills_list(self, value):
        """
        Устанавливает навыки из списка
        """
        if isinstance(value, list):
            self.skills = json.dumps(value, ensure_ascii=False)
        else:
            self.skills = '[]'

    def get_full_name(self):
        """
        Возвращает полное имя
        """
        return f"{self.last_name} {self.first_name}"

    def get_education_level_display_name(self):
        """
        Возвращает читаемое название уровня образования
        """
        if self.education_level:
            return dict(self.EDUCATION_LEVELS).get(self.education_level, '')
        return ''

    def save(self, *args, **kwargs):
        """
        Переопределяем метод save для дополнительной обработки
        """
        # Очищаем пустые строки перед сохранением
        if self.email == '':
            self.email = None
        if self.phone == '':
            self.phone = None
        if self.school == '':
            self.school = None
        if self.specialization == '':
            self.specialization = None
            
        super().save(*args, **kwargs)
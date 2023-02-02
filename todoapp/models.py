from django.db import models
from services.mixin import DateMixin, SlugMixin
from services.generator import CodeGenerator

# Create your models here.


class Todo(DateMixin, SlugMixin):
    name = models.CharField(max_length=200)
    deadline = models.DateField()
    status = models.BooleanField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Todo"
        verbose_name_plural = "Todo List"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = CodeGenerator.create_slug_shortcode(size=20, model_=Todo)
        return super(Todo, self).save(*args, **kwargs)

from django.core.management.base import BaseCommand, CommandError
from todoapp.models import Todo
from services.generator import CodeGenerator




class Command(BaseCommand):
    help = "Load Slugs for Todo List"

    def handle(self, *args, **options):
        todo_list = Todo.objects.all()
        for todo in todo_list:
            todo.slug = CodeGenerator.create_slug_shortcode(size=20, model_=Todo)
            todo.save()
        
        print("Finished!!!")

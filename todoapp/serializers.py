from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(view_name="todoapp:detail", lookup_field="slug")
    class Meta:
        model = Todo
        fields = "__all__"
        extra_kwargs = {
            "status": {"read_only": True}
        }
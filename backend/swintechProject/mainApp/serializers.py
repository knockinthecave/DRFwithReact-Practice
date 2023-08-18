from rest_framework import serializers
from .models import Worker


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'Worker'
        model = Worker
        fields = ('wid', 'workerName')
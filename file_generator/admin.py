from django.contrib import admin
from django_celery_results.admin import TaskResultAdmin
from django_celery_results.models import TaskResult, GroupResult
import json
from ast import literal_eval
from django.utils.html import format_html


class TaskResultAdminModified(TaskResultAdmin):
    list_display = ("task_id", "date_done", "status", "worker", "argument_field")

    def argument_field(self, obj):
        data = literal_eval(json.loads(obj.task_args))
        return format_html(
            f'<span style="font-weight: bold;">Filename:{data[0]}.csv </br> count:{data[1]}</span>'
        )

    argument_field.short_description = "Argument Data"


admin.site.unregister(TaskResult)
admin.site.unregister(GroupResult)
admin.site.register(TaskResult, TaskResultAdminModified)

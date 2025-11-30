import os
from celery import Celery
from decouple import config

# 设置Django的默认设置模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quant_platform.settings')

# 创建Celery应用实例
app = Celery('quant_platform')

# 使用django-configurations库从Django设置中加载配置
app.config_from_object('django.conf:settings', namespace='CELERY')

# 从所有已注册的Django应用中加载任务模块
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
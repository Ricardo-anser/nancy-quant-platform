import os
import sys
import django
from decouple import config

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quant_platform.settings')
django.setup()

# 启动Celery工作进程
if __name__ == '__main__':
    from quant_platform.celery import app
    app.start()
import os
import subprocess
import sys
import zipfile

zip_path = 'university_guide_marketplace_deploy.zip'
if os.path.exists(zip_path) and not os.path.exists('config/settings.py'):
    with zipfile.ZipFile(zip_path, 'r') as zf:
        for member in zf.infolist():
            rel_path = member.filename.replace('\\', '/')
            if rel_path.endswith('/'):
                os.makedirs(rel_path, exist_ok=True)
            else:
                parent = os.path.dirname(rel_path)
                if parent:
                    os.makedirs(parent, exist_ok=True)
                with zf.open(member) as src, open(rel_path, 'wb') as dst:
                    dst.write(src.read())

settings_path = 'config/settings.py'
if os.path.exists(settings_path):
    text = open(settings_path, 'r', encoding='utf-8').read()
    if 'whitenoise' not in text:
        text = text.replace(
            "'django.middleware.security.SecurityMiddleware',",
            "'django.middleware.security.SecurityMiddleware',\n    'whitenoise.middleware.WhiteNoiseMiddleware',",
        )
        if 'STATIC_ROOT' not in text:
            text += "\nSTATIC_ROOT = BASE_DIR / 'staticfiles'\n"
        open(settings_path, 'w', encoding='utf-8').write(text)

subprocess.run([sys.executable, 'manage.py', 'migrate', '--noinput'], check=True)
subprocess.run([sys.executable, 'manage.py', 'seed_data'], check=True)
subprocess.run([sys.executable, 'manage.py', 'collectstatic', '--noinput'], check=True)

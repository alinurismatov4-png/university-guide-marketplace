import os
import shutil
from pathlib import Path
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.test import Client
from marketplace.models import University

BASE_DIR = Path(__file__).resolve().parent
DIST_DIR = BASE_DIR / 'netlify_dist'

if DIST_DIR.exists():
    shutil.rmtree(DIST_DIR)
DIST_DIR.mkdir(parents=True, exist_ok=True)

shutil.copytree(BASE_DIR / 'static', DIST_DIR / 'static', dirs_exist_ok=True)

client = Client(HTTP_HOST='uniguide-marketplace.netlify.app')

routes = [
    ('/', 'index.html'),
    ('/universities/', 'universities/index.html'),
    ('/guides/', 'guides/index.html'),
    ('/scholarships/', 'scholarships/index.html'),
    ('/login/', 'login/index.html'),
    ('/register/', 'register/index.html'),
    ('/sitemap.xml', 'sitemap.xml'),
    ('/robots.txt', 'robots.txt'),
]

for uni in University.objects.filter(is_verified=True):
    routes.append((f'/universities/{uni.pk}/', f'universities/{uni.pk}/index.html'))

for url_path, out_rel in routes:
    resp = client.get(url_path, secure=True)
    out_file = DIST_DIR / out_rel
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(resp.content.decode('utf-8'), encoding='utf-8')

(DIST_DIR / '_redirects').write_text(
    "/universities /universities/index.html 200\n"
    "/guides /guides/index.html 200\n"
    "/scholarships /scholarships/index.html 200\n"
    "/login /login/index.html 200\n"
    "/register /register/index.html 200\n",
    encoding='utf-8',
)

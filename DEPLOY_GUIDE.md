# Инструкция по публикации сайта в интернет и добавлению в поиск Google / Яндекс 🌐

Ваш проект **University Guide Marketplace** уже полностью настроен для выкладки в интернет:
- Добавлены **SEO-теги** (`meta description`, `keywords`, `OpenGraph`) во все шаблоны;
- Настроена автоматическая генерация карты сайта **`/sitemap.xml`** и файла **`/robots.txt`** для поисковых роботов Google и Яндекса;
- Настроены `STATIC_ROOT` и `CSRF_TRUSTED_ORIGINS` для облачных хостингов.

---

## Шаг 1. Загрузите код на GitHub

1. Зарегистрируйтесь на [github.com](https://github.com) и создайте новый репозиторий с именем `university-guide-marketplace`.
2. Откройте терминал в папке проекта `C:\Users\SRM\.gemini\antigravity\scratch\university_guide_marketplace` и выполните:

```bash
git init
git add .
git commit -m "Initial commit: University Guide Marketplace"
git branch -M main
git remote add origin https://github.com/ВАШ_ЛОГИН/university-guide-marketplace.git
git push -u origin main
```

---

## Шаг 2. Бесплатный хостинг на PythonAnywhere (5 минут, без карты)

1. Создайте бесплатный аккаунт **Beginner** на сайте [www.pythonanywhere.com](https://www.pythonanywhere.com/).
2. Откройте вкладку **Consoles → Bash** и клонируйте ваш репозиторий:
   ```bash
   git clone https://github.com/ВАШ_ЛОГИН/university-guide-marketplace.git
   cd university-guide-marketplace
   mkvirtualenv --python=/usr/bin/python3.10 myenv
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py seed_data
   python manage.py collectstatic --noinput
   ```
3. Перейдите во вкладку **Web → Add a new web app → Manual configuration (Python 3.10)**:
   - В поле **Source code** укажите: `/home/ВАШ_ЛОГИН/university-guide-marketplace`
   - В поле **Virtualenv** укажите: `/home/ВАШ_ЛОГИН/.virtualenvs/myenv`
   - В разделе **Static files** добавьте:
     - URL: `/static/` → Directory: `/home/ВАШ_ЛОГИН/university-guide-marketplace/staticfiles`
     - URL: `/media/` → Directory: `/home/ВАШ_ЛОГИН/university-guide-marketplace/media`
   - Откройте **WSGI configuration file** и оставьте подключение Django к `config.settings`.
4. Нажмите зелёную кнопку **Reload** — ваш сайт сразу заработает по публичной ссылке `https://ВАШ_ЛОГИН.pythonanywhere.com`!

---

## Шаг 3. Добавление сайта в поиск Google и Яндекса

Как только сайт открывается по вашей ссылке `https://ВАШ_ЛОГИН.pythonanywhere.com`:

1. **Google Search Console ([search.google.com/search-console](https://search.google.com/search-console)):**
   - Введите адрес вашего сайта в блок **«Префикс URL»**.
   - В меню слева откройте **«Файлы Sitemap»** и отправьте ссылку:
     `https://ВАШ_ЛОГИН.pythonanywhere.com/sitemap.xml`
   - Google автоматически обойдёт все страницы университетов и гидов и добавит сайт в поиск!

2. **Яндекс.Вебмастер ([webmaster.yandex.ru](https://webmaster.yandex.ru)):**
   - Добавьте адрес сайта и в разделе **«Индексирование → Файлы Sitemap»** укажите тот же адрес `/sitemap.xml`.

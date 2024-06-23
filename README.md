# 2466-dj5-blog-app
Membuat Aplikasi Blog menggunakan Django versi 5
Github:https://github.com/gurnitha/2466-dj5-ultimate-task-manager
Local:E:\_WORKSPACE\2024\django\Rathan Kumar\DjangoBlog



## 1. SETUP


#### 1. Membuat dan mengklon repositori

        modified:   README.md


#### 2. Membuat struktur file

        modified:   README.md


#### 3. Membuat lingkungan virtual dengan nama 'venv312504'

        modified:   README.md


#### 4. Menginstal Django versi 5.0.4 dan meng-upgrade pip

        modified:   README.md



## 2. PROYEK DAN APLIKASI DJANGO


#### 1. Meng-inisiasi proyek Django

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### 2. Menjalankan development server dan melihat tampilan laman default Django

        (dj5-blog) λ ls
        config/  manage.py*  README.md  venv312504/

        E:\django\2466-dj5-blog-app\src(main -> origin)
        (dj5-blog) λ python manage.py runserver
        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).

        You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
        Run 'python manage.py migrate' to apply them.
        June 23, 2024 - 07:02:20
        Django version 5.0.4, using settings 'config.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.


#### 3. Membuat aplikasi Django

        modified:   README.md
        new file:   app/blog/__init__.py
        new file:   app/blog/admin.py
        new file:   app/blog/apps.py
        new file:   app/blog/migrations/__init__.py
        new file:   app/blog/models.py
        new file:   app/blog/tests.py
        new file:   app/blog/views.py


#### 4. Mendaftarkan aplikasi blog pada config/settings.py

        modified:   README.md
        modified:   app/blog/apps.py
        modified:   config/settings.py
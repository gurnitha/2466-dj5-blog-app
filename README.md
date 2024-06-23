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



## 3. DATABASE DAN KONFIGURASI


#### 1. Membuat MySQL database

        λ mysql -u root
        Welcome to the MySQL monitor.  Commands end with ; or \g.
        Your MySQL connection id is 272
        Server version: 8.0.30 MySQL Community Server - GPL

        Copyright (c) 2000, 2022, Oracle and/or its affiliates.

        Oracle is a registered trademark of Oracle Corporation and/or its
        affiliates. Other names may be trademarks of their respective
        owners.

        Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

        mysql> CREATE DATABASE 2466_dj5_blog_app;
        Query OK, 1 row affected (0.49 sec)


#### 2. Meng-instal mysqlclient

        (dj5-blog) λ pip install mysqlclient
        Collecting mysqlclient
          Using cached mysqlclient-2.2.4-cp312-cp312-win_amd64.whl.metadata (4.6 kB)
        Using cached mysqlclient-2.2.4-cp312-cp312-win_amd64.whl (203 kB)
        Installing collected packages: mysqlclient
        Successfully installed mysqlclient-2.2.4


#### 3. Menghubungan database dengan proyek

        modified:   README.md
        modified:   config/settings.py


#### 4. Membuat konfigurasi bahasa dan waktu

        modified:   README.md
        modified:   config/settings.py



## 4. MIGRASI DAN SUPERUSER


#### 1. Membuat dan meng-aplikasikan migrasi

        (dj5-blog) λ python manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, sessions
        Running migrations:
          Applying contenttypes.0001_initial... OK
          Applying auth.0001_initial... OK
          Applying admin.0001_initial... OK
          Applying admin.0002_logentry_remove_auto_add... OK
          Applying admin.0003_logentry_add_action_flag_choices... OK
          Applying contenttypes.0002_remove_content_type_name... OK
          Applying auth.0002_alter_permission_name_max_length... OK
          Applying auth.0003_alter_user_email_max_length... OK
          Applying auth.0004_alter_user_username_opts... OK
          Applying auth.0005_alter_user_last_login_null... OK
          Applying auth.0006_require_contenttypes_0002... OK
          Applying auth.0007_alter_validators_add_error_messages... OK
          Applying auth.0008_alter_user_username_max_length... OK
          Applying auth.0009_alter_user_last_name_max_length... OK
          Applying auth.0010_alter_group_name_max_length... OK
          Applying auth.0011_update_proxy_permissions... OK
          Applying auth.0012_alter_user_first_name_max_length... OK
          Applying sessions.0001_initial... OK


#### 2. Membuat superuser/admin

        (dj5-blog) λ ls
        app/  config/  db.sqlite3  manage.py*  README.md  venv312504/

        E:\django\2466-dj5-blog-app\src(main -> origin)
        (dj5-blog) λ python manage.py createsuperuser
        Nama pengguna (leave blank to use 'ing'): superuser
        Alamat email: superuser@mail.com
        Password:
        Password (again):
        Kata sandi terlalu mirip dengan alamat email.
        Bypass password validation and create user anyway? [y/N]: y
        Superuser created successfully.



## 5. URLS, VIEWS, TEMPLATES


#### 1. Membuat laman home bagian 1: membuat urls

        modified:   README.md
        new file:   app/blog/urls.py
        modified:   config/urls.py


#### 2. Membuat laman home bagian 2: membuat home_view

        modified:   README.md
        modified:   app/blog/views.py


#### 3. Membuat laman home bagian 3: membuat template untuk laman home

        modified:   README.md
        new file:   templates/blog/index.html


#### 4. Membuat laman home bagian 4: meng-aktifkan templates Django

        modified:   README.md
        modified:   config/settings.py


#### 5. Membuat laman home bagian 5: mengisi text pada laman home

        modified:   README.md
        modified:   templates/blog/index.html


#### 6. Membuat laman home bagian 6: mengisi bootstrap template pada laman home

        modified:   README.md
        modified:   templates/blog/index.html


#### 7. Membuat laman home bagian 7: membuat path untuk static file

        modified:   README.md
        modified:   config/settings.py
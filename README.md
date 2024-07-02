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


#### 8. Membuat laman home bagian 8: mengisi static file

        modified:   README.md
        new file:   app/blog/static/blog.css
        new file:   app/blog/static/blog.rtl.css
        new file:   app/blog/static/bootstrap.bundle.min.js
        new file:   app/blog/static/bootstrap.min.css
        new file:   app/blog/static/color-modes.js


#### 9. Membuat laman home bagian 9: mengelompokan static file

        modified:   README.md
        renamed:    app/blog/static/blog.css -> app/blog/static/css/blog.css
        renamed:    app/blog/static/blog.rtl.css -> app/blog/static/css/blog.rtl.css
        renamed:    app/blog/static/bootstrap.min.css -> app/blog/static/css/bootstrap.min.css
        renamed:    app/blog/static/bootstrap.bundle.min.js -> app/blog/static/js/bootstrap.bundle.min.js
        new file:   app/blog/static/js/bootstrap.min.css
        renamed:    app/blog/static/color-modes.js -> app/blog/static/js/color-modes.js


#### 10. Membuat laman home bagian 10: mengunggah (load) static file pada laman home

        modified:   README.md
        modified:   templates/blog/index.html


#### 11. Membuat laman home bagian 11: memodifikasi template laman home

        modified:   README.md
        modified:   templates/blog/index.html


#### 12. Template inheritance bagian 1: membuat dan menampilkan base template

        modified:   README.md
        new file:   app/blog/static/images/cricket.jpg
        modified:   app/blog/views.py
        new file:   templates/base.html


#### 13. Template inheritance bagian 2: extends base.html pada laman home

        modified:   README.md
        new file:   app/blog/static/images/national_team.png
        modified:   app/blog/views.py
        modified:   templates/base.html
        modified:   templates/blog/index.html



## 6. MODELS


#### 1. Membuat model Category

        modified:   README.md
        modified:   app/blog/models.py


#### 2. Membuat dan mengaplikasikan migrasi untuk model Category

        modified:   README.md
        new file:   app/blog/migrations/0001_initial.py


#### 3. Melihat perintah Django untuk membuat tabel

        (dj5-blog) λ python manage.py sqlmigrate blog 0001

        --
        -- Create model Category
        --
        CREATE TABLE `blog_category` (
                `id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, 
                `category_name` varchar(50) NOT NULL UNIQUE, 
                `created_at` datetime(6) NOT NULL, 
                `updated_at` datetime(6) NOT NULL
        );

        mysql> SHOW tables;
        +-----------------------------+
        | Tables_in_2466_dj5_blog_app |
        +-----------------------------+
        | auth_group                  |
        | auth_group_permissions      |
        | auth_permission             |
        | auth_user                   |
        | auth_user_groups            |
        | auth_user_user_permissions  |
        | blog_category               |
        | django_admin_log            |
        | django_content_type         |
        | django_migrations           |
        | django_session              |
        +-----------------------------+
        11 rows in set (0.01 sec)

        mysql> DESC blog_category;
        +---------------+-------------+------+-----+---------+----------------+
        | Field         | Type        | Null | Key | Default | Extra          |
        +---------------+-------------+------+-----+---------+----------------+
        | id            | bigint      | NO   | PRI | NULL    | auto_increment |
        | category_name | varchar(50) | NO   | UNI | NULL    |                |
        | created_at    | datetime(6) | NO   |     | NULL    |                |
        | updated_at    | datetime(6) | NO   |     | NULL    |                |
        +---------------+-------------+------+-----+---------+----------------+
        4 rows in set (0.01 sec)

        mysql> SELECT * FROM blog_category;
        Empty set (0.00 sec)


#### 4. Mendaftarkan model Category pada blog/admin.py dan membuat entries

        modified:   README.md
        modified:   app/blog/admin.py


#### 5. Membuat model Blog

        modified:   README.md
        modified:   app/blog/models.py


#### 3. Membuat dan mengaplikasikan migrasi untuk model Blog

        (dj5-blog) λ python manage.py makemigrations blog blog
        System check identified some issues:

        WARNINGS:
        ?: (staticfiles.W004) The directory 'blog/static' in the STATICFILES_DIRS setting does not exist.
        Migrations for 'blog':
          app\blog\migrations\0002_blog.py
            - Create model Blog

        E:\django\2466-dj5-blog-app\src(main -> origin)
        (dj5-blog) λ python manage.py migrate blog 0002
        System check identified some issues:

        WARNINGS:
        ?: (staticfiles.W004) The directory 'blog/static' in the STATICFILES_DIRS setting does not exist.
        Operations to perform:
          Target specific migration: 0002_blog, from blog
        Running migrations:
          Applying blog.0002_blog... OK

        (dj5-blog) λ python manage.py sqlmigrate blog 0002
        System check identified some issues:

        WARNINGS:
        ?: (staticfiles.W004) The directory 'blog/static' in the STATICFILES_DIRS setting does not exist.
        --
        -- Create model Blog
        --
        CREATE TABLE `blog_blog` (
                `id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, 
                `title` varchar(100) NOT NULL, 
                `slug` varchar(150) NOT NULL UNIQUE, 
                `featured_image` varchar(100) NOT NULL, 
                `short_description` longtext NOT NULL, 
                `blog_body` longtext NOT NULL, 
                `status` varchar(20) NOT NULL, 
                `is_featured` bool NOT NULL, 
                `created_at` datetime(6) NOT NULL, 
                `updated_at` datetime(6) NOT NULL, 
                `author_id` integer NOT NULL, 
                `category_id` bigint NOT NULL
        );
        ALTER TABLE `blog_blog` ADD CONSTRAINT `blog_blog_author_id_8791af69_fk_auth_user_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`);
        ALTER TABLE `blog_blog` ADD CONSTRAINT `blog_blog_category_id_c34d5f94_fk_blog_category_id` FOREIGN KEY (`category_id`) REFERENCES `blog_category` (`id`);

        mysql> SHOW tables;
        +-----------------------------+
        | Tables_in_2466_dj5_blog_app |
        +-----------------------------+
        | auth_group                  |
        | auth_group_permissions      |
        | auth_permission             |
        | auth_user                   |
        | auth_user_groups            |
        | auth_user_user_permissions  |
        | blog_blog                   |
        | blog_category               |
        | django_admin_log            |
        | django_content_type         |
        | django_migrations           |
        | django_session              |
        +-----------------------------+
        12 rows in set (0.00 sec)

        mysql> DESC blog_blog;
        +-------------------+--------------+------+-----+---------+----------------+
        | Field             | Type         | Null | Key | Default | Extra          |
        +-------------------+--------------+------+-----+---------+----------------+
        | id                | bigint       | NO   | PRI | NULL    | auto_increment |
        | title             | varchar(100) | NO   |     | NULL    |                |
        | slug              | varchar(150) | NO   | UNI | NULL    |                |
        | featured_image    | varchar(100) | NO   |     | NULL    |                |
        | short_description | longtext     | NO   |     | NULL    |                |
        | blog_body         | longtext     | NO   |     | NULL    |                |
        | status            | varchar(20)  | NO   |     | NULL    |                |
        | is_featured       | tinyint(1)   | NO   |     | NULL    |                |
        | created_at        | datetime(6)  | NO   |     | NULL    |                |
        | updated_at        | datetime(6)  | NO   |     | NULL    |                |
        | author_id         | int          | NO   | MUL | NULL    |                |
        | category_id       | bigint       | NO   | MUL | NULL    |                |
        +-------------------+--------------+------+-----+---------+----------------+
        12 rows in set (0.00 sec)


#### 5. Mendaftarkan model Blog pada blog/admin.py dan membuat entries

        modified:   README.md
        modified:   app/blog/admin.py
        new file:   uploads/2024/06/23/prabowo.png

        NOTE: Error krn blm disetup path untuk media files

        NEXT: Setup media file path


#### 6. Mensetup media file path dan re-upload image

        modified:   README.md
        modified:   config/settings.py
        modified:   config/urls.py
        renamed:    uploads/2024/06/23/prabowo.png -> media/uploads/2024/06/23/prabowo.png

        Note: Kolom slug masih diisi scr manual. Sebaiknya bisa diisi scr otomatis.

        NEXT: Pre-populated slug


#### 7. Pre-populated slug

        modified:   README.md
        modified:   app/blog/admin.py


#### 8. Memodifikasi tampilan model/tabel pada admin panel

        modified:   README.md
        modified:   app/blog/admin.py


#### 9. Menambahkan bebera blog entri melalui admin panel

        modified:   README.md
        new file:   media/uploads/2024/06/23/bisnis.png
        new file:   media/uploads/2024/06/23/budaya.png
        new file:   media/uploads/2024/06/23/covid-19.png
        new file:   media/uploads/2024/06/23/rupiah.png
        new file:   media/uploads/2024/06/23/sain.png
        new file:   media/uploads/2024/06/23/teknologi.png
        new file:   media/uploads/2024/06/23/timnas.png



## 7. LOAD DAN DISPLAY OBJECTS


#### 1. Load dan display Category objects bagian 1: testing print categories object ke terminal

        modified:   README.md
        modified:   app/blog/views.py


#### 2. Load dan display Category objects bagian 2: display categories object pada navbar

        modified:   README.md
        modified:   app/blog/views.py
        modified:   templates/base.html


#### 3. Load dan display featured objects dari Blog bagian 1: testing print featured objects ke terminal

        modified:   README.md
        modified:   app/blog/views.py


#### 4. Load dan display featured objects dari Blog bagian 2: display featured objects ke laman home

        modified:   README.md
        modified:   app/blog/views.py
        modified:   templates/base.html

        NOTE: Too many featured posts for hero section

        NEXT: Show only 1 featured post as hero section


#### 5. Show only 1 featured post as hero section

        modified:   README.md
        modified:   templates/base.html

        {% for featured_post in featured_posts %}
            {% if forloop.first %}
                codes here ...
            {% endif %}
        {% endfor %}


#### 6. Menampilkan sisa featured posts

        modified:   README.md
        modified:   templates/blog/index.html


#### 7. Menampilkan recent posts

        modified:   README.md
        modified:   app/blog/views.py
        modified:   templates/blog/index.html



## 8. BLOGS BY CATEGORY


#### 1. Load dan display blogs by category bagian 1: testing

        modified:   README.md
        modified:   app/blog/urls.py
        modified:   app/blog/views.py


#### 2. Load dan display blogs by category bagian 2: display pada laman blogs_by_category

        modified:   README.md
        modified:   app/blog/views.py
        new file:   templates/blog/blogs_by_category.html


#### 3. Load dan display blogs by category bagian 3: mengisi layout untuk laman blogs_by_category

        modified:   README.md
        modified:   templates/blog/blogs_by_category.html

        Note: 

        <p>Tidak ditemui blog by category.</p> sebaiknya
        tidak ditampilkan.

        Arahkan user ke laman home bila tidak ditemui blog by category.


#### 4. Load dan display blogs by category bagian 4: mengarahkan user ke laman home bila tidak ditemui blog by category

        modified:   README.md
        modified:   app/blog/views.py


#### 5. Load dan display blogs by category bagian 5: menampilkan laman custom error (404)

        modified:   README.md
        modified:   app/blog/views.py
        modified:   config/settings.py
        new file:   templates/404.html


#### 6. Load dan display blogs by category bagian 6: mengembalikan 'page not found' ke laman home

        modified:   README.md
        modified:   app/blog/views.py
        modified:   config/settings.py


#### 7. Load dan display blogs by category bagian 7: context_processors

        modified:   README.md
        new file:   app/blog/context_processors.py
        modified:   app/blog/views.py
        modified:   config/settings.py


#### 8. Load dan display blogs by category bagian 8: membuat tautan (links)

        modified:   README.md
        modified:   templates/base.html
        modified:   templates/blog/blogs_by_category.html



## 9. BLOGS BY SLUG


#### 1. Load dan display blogs by slug - bagian 1: urls, views, templates

        modified:   README.md
        modified:   app/blog/urls.py
        modified:   app/blog/views.py
        new file:   templates/blog/blogs_by_slug.html


#### 2. Load dan display blogs by slug - bagian 2: extending base template dan membuat tautan

        modified:   README.md
        modified:   templates/base.html
        modified:   templates/blog/blogs_by_slug.html

        Note: 

        Konten yang ditampilkan bersifat statis dan
        tidak ada hubungan dengan slug.

        NEXT: Menampilkan konten yang berkaitan dengan slug.


#### 3. Load dan display blogs by slug - bagian 3: menampilkan konten yang berkaitan dengan slug

        modified:   README.md
        modified:   app/blog/views.py
        modified:   templates/blog/blogs_by_slug.html


#### 4. Load dan display blogs by slug - bagian 4: membuat tautan untuk judul blog

        modified:   README.md
        modified:   templates/blog/index.html


#### 5. Load dan display blogs by slug - bagian 5: mengisi layout dan fetch data

        modified:   README.md
        modified:   templates/blog/blogs_by_slug.html


#### 6. Load dan display blogs by slug - bagian 6: fetch categories pada laman blogs_by_slug

        modified:   README.md
        modified:   templates/blog/blogs_by_slug.html


#### 7. Load dan display blogs by slug - bagian 7: Membuat tautan

        modified:   README.md
        modified:   templates/blog/blogs_by_category.html
        modified:   templates/blog/blogs_by_slug.html
        modified:   templates/blog/index.html



## 10. SOSIAL MEDIA DAN LAMAN ABOUT


#### 1. Membuat model About

        modified:   README.md
        modified:   app/blog/models.py


#### 2. Membuat dan meng-aplikasikan migrasi untuk model About

        (dj5-blog) λ python manage.py makemigrations blog
        Migrations for 'blog':
          app\blog\migrations\0003_about.py
            - Create model About

        E:\django\2466-dj5-blog-app\src(main -> origin)
        (dj5-blog) λ python manage.py migrate blog 0003
        Operations to perform:
          Target specific migration: 0003_about, from blog
        Running migrations:
          Applying blog.0003_about... OK

        E:\django\2466-dj5-blog-app\src(main -> origin)
        (dj5-blog) λ python manage.py sqlmigrate blog 0003
        --
        -- Create model About
        --
        CREATE TABLE `blog_about` (
                `id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, 
                `about_heading` varchar(25) NOT NULL, 
                `about_description` longtext NOT NULL, 
                `created_at` datetime(6) NOT NULL, 
                `updated_at` datetime(6) NOT NULL
        );

        mysql> DESC blog_about;
        +-------------------+-------------+------+-----+---------+----------------+
        | Field             | Type        | Null | Key | Default | Extra          |
        +-------------------+-------------+------+-----+---------+----------------+
        | id                | bigint      | NO   | PRI | NULL    | auto_increment |
        | about_heading     | varchar(25) | NO   |     | NULL    |                |
        | about_description | longtext    | NO   |     | NULL    |                |
        | created_at        | datetime(6) | NO   |     | NULL    |                |
        | updated_at        | datetime(6) | NO   |     | NULL    |                |
        +-------------------+-------------+------+-----+---------+----------------+
        5 rows in set (0.05 sec)

        modified:   README.md
        new file:   app/blog/migrations/0003_about.py


#### 3. Mendaftarkan model About pada blog/admin.py

        modified:   README.md
        modified:   app/blog/admin.py


#### 4. Membuat laman about: url, views template

        modified:   README.md
        modified:   app/blog/urls.py
        modified:   app/blog/views.py
        new file:   templates/blog/about.html
        modified:   templates/blog/index.html


#### 5. Membuat layout untuk laman about

        modified:   README.md
        modified:   templates/blog/about.html


#### 6. Menampilkan data pada laman about

        modified:   README.md
        modified:   app/blog/views.py
        modified:   templates/blog/about.html


### 7. Membuat model SocialLink

        modified:   README.md
        modified:   app/blog/models.py


### 8. Membuat dan meng-aplikasikan migrasi untuk model SocialLink

        (dj5-blog) λ python manage.py makemigrations blog
        Migrations for 'blog':
          app\blog\migrations\0004_sociallink.py
            - Create model SocialLink

        E:\django\2466-dj5-blog-app\src(main -> origin)
        (dj5-blog) λ python manage.py migrate blog 0004
        Operations to perform:
          Target specific migration: 0004_sociallink, from blog
        Running migrations:
          Applying blog.0004_sociallink... OK

        E:\django\2466-dj5-blog-app\src(main -> origin)
        (dj5-blog) λ python manage.py sqlmigrate blog 0004
        --
        -- Create model SocialLink
        --
        CREATE TABLE `blog_sociallink` (
                `id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, 
                `platform` varchar(25) NOT NULL, 
                `link` varchar(150) NOT NULL, 
                `created_at` datetime(6) NOT NULL, 
                `updated_at` datetime(6) NOT NULL
        );

        mysql> show tables;
        +-----------------------------+
        | Tables_in_2466_dj5_blog_app |
        +-----------------------------+
        | auth_group                  |
        | auth_group_permissions      |
        | auth_permission             |
        | auth_user                   |
        | auth_user_groups            |
        | auth_user_user_permissions  |
        | blog_about                  |
        | blog_blog                   |
        | blog_category               |
        | blog_sociallink             |
        | django_admin_log            |
        | django_content_type         |
        | django_migrations           |
        | django_session              |
        +-----------------------------+
        14 rows in set (0.00 sec)

        mysql> DESC blog_sociallink;
        +------------+--------------+------+-----+---------+----------------+
        | Field      | Type         | Null | Key | Default | Extra          |
        +------------+--------------+------+-----+---------+----------------+
        | id         | bigint       | NO   | PRI | NULL    | auto_increment |
        | platform   | varchar(25)  | NO   |     | NULL    |                |
        | link       | varchar(150) | NO   |     | NULL    |                |
        | created_at | datetime(6)  | NO   |     | NULL    |                |
        | updated_at | datetime(6)  | NO   |     | NULL    |                |
        +------------+--------------+------+-----+---------+----------------+
        5 rows in set (0.01 sec)

        modified:   README.md
        new file:   app/blog/migrations/0004_sociallink.py


### 9. Mendaftarkan model SocialLink pada blog/admin.py

        modified:   README.md
        modified:   app/blog/admin.py


### 10. Membuat context_processors get_social_links

        modified:   README.md
        modified:   app/blog/context_processors.py
        modified:   config/settings.py


### 11. Membuat entries dan menampilkan SocialLink

        modified:   README.md
        modified:   app/blog/context_processors.py
        modified:   templates/blog/about.html



## 11. SEACRCH


#### 1. Membuat search form

        modified:   README.md
        modified:   templates/base.html


#### 2. Membuat search url, view, dan template

        modified:   README.md
        modified:   app/blog/urls.py
        modified:   app/blog/views.py
        new file:   templates/blog/search.html


#### 3. Membuat layout untuk laman search 

        modified:   README.md
        modified:   templates/blog/search.html


#### 4. Membuat funsionalitas search pada search_view

        modified:   README.md
        modified:   app/blog/views.py
        modified:   templates/base.html


#### 5. Memfungsikan search pada laman search

        modified:   README.md
        modified:   app/blog/views.py
        modified:   templates/blog/search.html



## 12. LOGIN & REGISTRASI


#### 1. Membuat aplikasi user

        modified:   README.md
        new file:   app/user/__init__.py
        new file:   app/user/admin.py
        new file:   app/user/apps.py
        new file:   app/user/migrations/__init__.py
        new file:   app/user/models.py
        new file:   app/user/tests.py
        new file:   app/user/views.py


#### 2. Mendaftarkan aplikasi user pada config/settings.py

        modified:   README.md
        modified:   app/user/apps.py
        modified:   config/settings.py


#### 3. Membuat laman register: url, view, template

        modified:   README.md
        new file:   app/user/urls.py
        modified:   app/user/views.py
        modified:   config/urls.py
        new file:   templates/user/register.html


#### 4. Menambahkan form layout pada laman register

        modified:   README.md
        modified:   templates/user/register.html


#### 5. Membuat model RegistrationForm

        modified:   README.md
        new file:   app/user/forms.py


#### 6. Menampilkan model RegistrationForm melalui register_view

        modified:   README.md
        modified:   app/user/views.py
        modified:   templates/user/register.html


#### 7. Styling laman register menggunakan crispy form

        modified:   README.md
        modified:   config/settings.py
        modified:   templates/base.html
        modified:   templates/user/register.html


#### 8. Membuat fungsionalitas registrasi

        modified:   README.md
        modified:   app/user/views.py
        modified:   templates/base.html

        NOTE:

        Sukses register user baru.


#### 9. Membuat laman login: url, view, template

        modified:   README.md
        modified:   app/user/urls.py
        modified:   app/user/views.py
        modified:   templates/base.html
        new file:   templates/user/login.html


#### 10. Menambahkan form layout pada laman login

        modified:   README.md
        modified:   templates/user/login.html


#### 11. Menggunakan AuthenticationForm pada laman login melalui login_view

        modified:   README.md
        modified:   app/user/views.py
        modified:   templates/user/login.html


#### 12. Membuat fungsionalitas login

        modified:   README.md
        modified:   app/user/views.py
        modified:   templates/user/login.html

        NOTE:

        Setelah berhasil login, user seharusnya tidak lagi
        ditampilkan menu login dan register, tetapi
        seharusnya ditampilkan menu logout.


#### 13. Menambahkan logik pada navbar untuk menu login, register, dan logout

        modified:   README.md
        modified:   templates/base.html


#### 14. Logout the logged in user

        modified:   README.md
        modified:   app/user/urls.py
        modified:   app/user/views.py
        modified:   templates/base.html



## 13. PERMISSIONS DAN GROUPS


#### 1. Tentang otorisasi dan otentikasi

        modified:   README.md


#### 2. Membuat user baru sebagai editor

        modified:   README.md
        new file:   media/uploads/2024/06/30/perkotaan.PNG


#### 3. Membuat Groups user dengan nama 'Manajer'

        modified:   README.md


#### 4. Menempatkan pengguna ke grup

        modified:   README.md



## 14. CUSTOM DASHBOARD ATAU PROJECT SCALING


#### 1. Membuat requirements.txt file

        modified:   README.md
        new file:   requirements.txt


#### 2. Meng-upgrade paket-paket (packages)

        modified:   README.md
        modified:   requirements.txt


#### 3. Tentang dashboar untuk manager dan editor

        modified:   README.md


#### 4. Membuat app dashboard

        modified:   README.md
        new file:   app/dashboard/__init__.py
        new file:   app/dashboard/admin.py
        new file:   app/dashboard/apps.py
        new file:   app/dashboard/migrations/__init__.py
        new file:   app/dashboard/models.py
        new file:   app/dashboard/tests.py
        new file:   app/dashboard/views.py


#### 5. Mendaftarkan app dashboard pada dashboard/apps.py

        modified:   README.md
        modified:   app/dashboard/apps.py
        modified:   config/settings.py


#### 6. Membuat laman dashboard: url, view, template

        modified:   README.md
        new file:   app/dashboard/urls.py
        modified:   app/dashboard/views.py
        modified:   config/urls.py
        new file:   templates/dashboard/dashboard.html


#### 7. Membuat layout untuk laman dashboard

        modified:   README.md
        modified:   templates/dashboard/dashboard.html


#### 8. Count category dan blog

        modified:   README.md
        modified:   app/dashboard/views.py
        modified:   templates/dashboard/dashboard.html


#### 9. Login required decorator

        modified:   README.md
        modified:   app/dashboard/views.py
        modified:   app/user/views.py


#### 10. Membuat laman dashboard untuk categories: url, view, dan template

        modified:   README.md
        modified:   app/dashboard/urls.py
        modified:   app/dashboard/views.py
        new file:   templates/dashboard/categories.html


#### 11. Membuat include file: left_sidebar

        modified:   README.md
        modified:   templates/dashboard/categories.html
        modified:   templates/dashboard/dashboard.html
        new file:   templates/dashboard/left_sidebar.html


#### 12. Membuat links highliting

        modified:   README.md
        modified:   templates/dashboard/left_sidebar.html


#### 13. Load categories pada laman dashboard_categories

        modified:   README.md
        modified:   app/dashboard/views.py
        modified:   templates/dashboard/categories.html


#### 14. Add font-awesome css

        modified:   README.md
        new file:   app/blog/static/css/font-awesome.min.css
        modified:   templates/base.html
        modified:   templates/dashboard/categories.html



## 15. CRUD CATEGORIES


#### 1. Membuat laman add category part 1: url, view, dan template

        modified:   README.md
        modified:   app/dashboard/urls.py
        modified:   app/dashboard/views.py
        new file:   templates/dashboard/add_category.html


#### 2. Membuat laman add category part 2: membuat layout

        modified:   README.md
        modified:   templates/dashboard/add_category.html


#### 3. Membuat laman add category part 3: membuat form model

        modified:   README.md
        new file:   app/dashboard/forms.py


#### 4. Membuat laman add category part 4: render model CategoryForm

        modified:   README.md
        modified:   app/dashboard/views.py


#### 5. Membuat laman add category part 5: add logic pada add_category view dan testing

        modified:   README.md
        modified:   app/dashboard/views.py
        modified:   templates/dashboard/add_category.html
        modified:   templates/dashboard/categories.html


#### 6. Membuat laman edit category part 1: url, view, dan template

        modified:   README.md
        modified:   app/dashboard/urls.py
        modified:   app/dashboard/views.py
        modified:   templates/dashboard/categories.html
        new file:   templates/dashboard/edit_category.html


#### 7. Membuat laman edit category part 2: membuat form

        modified:   README.md
        modified:   templates/dashboard/edit_category.html


#### 8. Membuat laman edit category part 3: add logic pada edit_category_view

        modified:   README.md
        modified:   app/dashboard/views.py
        modified:   templates/dashboard/edit_category.html


#### 9. Delete a category

        modified:   README.md
        modified:   app/dashboard/urls.py
        modified:   app/dashboard/views.py
        modified:   templates/dashboard/categories.html



## 16. CRUD BLOGS


#### 1. Membuat laman blogs part 1: url, view, dan template

        modified:   README.md
        modified:   app/dashboard/urls.py
        modified:   app/dashboard/views.py
        new file:   templates/dashboard/blogs.html


#### 2. Membuat laman blogs part 2: highliting menu blogs

        modified:   README.md
        modified:   templates/dashboard/left_sidebar.html


#### 3. Membuat laman blogs part 3: load dan fetch blogs

        modified:   README.md
        modified:   app/dashboard/views.py
        modified:   templates/dashboard/blogs.html


#### 4. Add blog part 1: url, view, dan template

        modified:   README.md
        modified:   app/dashboard/urls.py
        modified:   app/dashboard/views.py
        new file:   templates/dashboard/add_blog.html


#### 5. Add blog part 2: membuat model BlogForm

        modified:   README.md
        modified:   app/dashboard/forms.py


#### 6. Add blog part 3: mengisi layout laman add_blog

        modified:   README.md
        modified:   templates/dashboard/add_blog.html


#### 7. Add blog part 4: rendering BlogForm

        modified:   README.md
        modified:   app/dashboard/views.py
        modified:   templates/dashboard/add_blog.html


#### 8. Add blog part 5: add logic pada add_blog_view dan add new blog

        modified:   README.md
        modified:   app/dashboard/views.py
        new file:   media/uploads/2024/07/01/car.PNG
        new file:   media/uploads/2024/07/01/car_Bn2qxkx.PNG
        new file:   media/uploads/2024/07/01/car_MwlZzXN.PNG
        new file:   media/uploads/2024/07/01/car_U9ERvsD.PNG
        new file:   media/uploads/2024/07/01/car_sa48IIq.PNG
        new file:   media/uploads/2024/07/01/car_tnFX6kR.PNG


#### 9. Membuat laman edit blog part 1: url, view, dan template

        modified:   README.md
        modified:   app/dashboard/urls.py
        modified:   app/dashboard/views.py
        new file:   templates/dashboard/edit_blog.html


#### 10. Membuat laman edit blog part 2: membuat form layout

        modified:   README.md
        modified:   templates/dashboard/edit_blog.html


#### 11. Membuat laman edit blog part 3: render BlogForm melalui edit_blog_view

        modified:   README.md
        modified:   app/dashboard/views.py
        modified:   templates/dashboard/edit_blog.html


#### 12. Membuat laman edit blog part 4: menambahkan logic pada edit_blog_view dan testing edit blog

        modified:   README.md
        modified:   app/dashboard/urls.py
        modified:   app/dashboard/views.py
        modified:   templates/dashboard/blogs.html
        modified:   templates/dashboard/edit_blog.html



## 17. MENGELOLA PENGGUNA DARI DASHBOARD


#### 1. Membuat laman user part 1: url, view, template

        modified:   README.md
        modified:   app/dashboard/urls.py
        modified:   app/dashboard/views.py
        new file:   templates/dashboard/users.html


#### 2. Membuat laman user part 2: menambahkan layout

        modified:   README.md
        modified:   templates/dashboard/users.html


#### 3. Membuat laman add user part 1: url, view, template

        modified:   README.md
        modified:   app/dashboard/urls.py
        modified:   app/dashboard/views.py
        new file:   templates/dashboard/add_user.html


#### 4. Membuat laman add user part 2: menambahkan layout

        modified:   README.md
        modified:   templates/dashboard/add_user.html


#### 5. Membuat laman add user part 3: membuat model AddUserForm

        modified:   README.md
        modified:   app/dashboard/forms.py


#### 6. Membuat laman add user part 4: me-render model AddUserForm

        modified:   README.md
        modified:   app/dashboard/views.py
        modified:   templates/dashboard/add_user.html


#### 7. Membuat laman add user part 5: menambahkan logik pada add_user_view

        modified:   README.md
        modified:   app/dashboard/views.py
        modified:   templates/dashboard/add_user.html


#### 8. Membuat laman add user part 6: membuat user baru

        modified:   README.md

        NOTE:

        1. User barus sebagai editor dan sebagai manajer
        telah berhasil dibuat.
        2. Tidak ada perubahan file.


#### 9. Membuat laman add user part 7: load dan display users

        modified:   README.md
        modified:   app/dashboard/views.py
        modified:   templates/dashboard/users.html


#### 10. Membuat laman edit user part 1:  url, view, template

        modified:   README.md
        modified:   app/dashboard/urls.py
        modified:   app/dashboard/views.py
        new file:   templates/dashboard/edit_user.html


#### 11. Membuat laman edit user part 2:  menambahkan layout

        modified:   README.md
        modified:   templates/dashboard/edit_user.html


#### 12. Membuat laman edit user part 3: membuat model EditUserForm

        modified:   README.md
        modified:   app/dashboard/forms.py


#### 13. Membuat laman edit user part 4: me-render model EditUserForm

        modified:   README.md
        modified:   app/dashboard/views.py
        modified:   templates/dashboard/edit_user.html


#### 14. Membuat laman edit user part 5: membuat logik pada edit_user_view dan testing

        modified:   README.md
        modified:   app/dashboard/views.py
        modified:   templates/dashboard/edit_user.html


#### 15. Delete user dan membuat tautan edit dan delete

        modified:   README.md
        modified:   app/dashboard/urls.py
        modified:   app/dashboard/views.py
        modified:   templates/dashboard/users.html
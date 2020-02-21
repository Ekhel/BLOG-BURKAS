# BLOG-BURKAS (Buruh Kasar)

![Imgur](https://i.imgur.com/bIaKakh.png)

## System Requirements :
* Bahasa Utama :
  - Python 3

* Framework :
  - Django 2.2.6

* DBMS :
  - SQLite (On Local)
  - PostgreSQL (On Heroku)

* Template :
  - Backend Default Django
  - Frontend ![MaterialKit](https://demos.creative-tim.com/material-kit/index.html)

* Services :
  - virtual env

* Web Server
  - gunicorn

------------------------------------------------------------------------

## Caran Menjalankan Project :

  * Clone Repositori ini (*git clone https://github.com/Ekhel/BLOG-BURKAS.git*)
  * Pastikan Python Telah Terinstal, Saya Menggunakan Python 3
  * Create Env didalam Project yang telah di clone Saya Menggunakan Windows 10 Pro

    - Buka Command Promt (CMD)
    - Buat virtual env ( *python -m venv envburkas* )
    - Activkan env dalam folder BLOG-BURKAS ( *envburkas\Scripts\activate* )
    
  * Upgrade pip ( *python -m pip install --upgrade pip* )
  * Install requirements.txt ( *pip install -r requirements.txt* )
  * Migrasi database ( *python manage.py migrate* )
  * Triger Migrasi ( *python manage.py makemigrations* )
  * Buat Super User ( *python manage.py createsuperuser* )

    - Buat Super User untuk Login Admin

  * Running Project ( *python manage.py runserver* )

------------------------------------------------------------------------

## Progres Pembuatan & Pengembangan

### Michael :
  * **Kamis 20  Februari 2020**
    - Buat Project [Solved]
    - Buat Applikasi blog-burkas [Solved]
    - Deploy ke heroku [Solved]
    - Buat Model Article [Solved]
    - Perbaiki base template [Solved]
    - Install Django Summernote [Solved]

  * **Jumat 21 Februari 2020**
    - Buat Detail Article [Solved]
    - Buat View Embed Video [Solved]
    - Buat View Body Article [Solve]
    - Buat dan Tambah Disqus Comment [Solved]
    - Perbaiki View Detail Post [NotSolved]
    

[![Built with Spacemacs](https://cdn.rawgit.com/syl20bnr/spacemacs/442d025779da2f62fc86c2082703697714db6514/assets/spacemacs-badge.svg)](http://github.com/syl20bnr/spacemacs)

---

<p align="center"><img src="/doc/img/logo.png" alt="team-builder_logo"/></p>

# Introduction

This a web app, a team course project in SYSU.
SQLite3 array
# Requirement

- python3
- PostgreSQL 9.5

# Libraries

- django 1.96
- django rest_framework

# Run

Please set up PostgreSQL according to `DATABASES` in `settings.py`.

Then run the following command under `./mysite` directory. 

```
./manage.py runserver
```

visit `localhost:8000` to see the local website.

visit `localhost:8000/admin` to manage the website as super user.

Before that, you may want to create a superuser account with this command.

```
./manage.py createsuperuser
```

visit `localhost:8000/api` to manage api.

# License

The MIT License (MIT)

Copyright © 2016 TeamBuilder Group

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

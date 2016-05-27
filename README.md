[![Built with Spacemacs](https://cdn.rawgit.com/syl20bnr/spacemacs/442d025779da2f62fc86c2082703697714db6514/assets/spacemacs-badge.svg)](http://github.com/syl20bnr/spacemacs)

---

<p align="center"><img src="/doc/img/logo.png" alt="team-builder_logo"/></p>

# Introduction

This a web app, a team course project in SYSU.

# Requirement

- python3
- PostgreSQL 9.5

# Libraies

- django 1.96
- djangorestframework


# Run

Please set up PostgreSQL according to `DATABASES` in `settings.py` and import database correctly.

Then run the following command under `./mysite` directory. 

```
./manage.py runserver
```

visit `localhost:8000` to see the local website.

visit `localhost:8000/admin` to manage the website as super user.

```
usename: peter
password: teambuilder
```

visit `localhost:8000/api` to manage api.

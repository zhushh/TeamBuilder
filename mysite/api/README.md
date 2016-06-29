# API v1.0

This is the api demonstration of team builder's model.

## Permission

All api is **read only** for any **unauthenticated users**.

Currently, only the **authenticated owner** of model instance can edit it. Otherwise, it's **read only**.

And only those whose role is `special` can create `project` as we've discussed in meeting 01.
    
## List

The following api return the list of corresponding model instances where `post` method can create a new instance.

I plan to add some extra parameters to `get` method to filter unwanted instances in the next api version.

- http://localhost:8000/api/users/
- http://localhost:8000/api/profiles/
- http://localhost:8000/api/projects/
- http://localhost:8000/api/teams/
- http://localhost:8000/api/comments/

Take User list as example.

- `count`: The number of model instances returned.
- `next`: The url of next page.
- `previous`': The url of previous page.
- `results`: A list of model instances.


```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "url": "http://localhost:8000/api/users/2/",
            "username": "user002",
            "email": "",
            "is_staff": false,
            "profile": "http://localhost:8000/api/profiles/2/",
            "project_published": [
                2
            ]
        },
        {
            "url": "http://localhost:8000/api/users/1/",
            "username": "peter",
            "email": "sptzxbbb@gmail.com",
            "is_staff": true,
            "profile": "http://localhost:8000/api/profiles/1/",
            "project_published": [
                1
            ]
        }
    ]
}
```

The api of a specific model instance looks like below.

```
http://localhost:8000/api/models/pk
```

## User
 
The value of project_published is a list of primary keys.

```json
{
    "url": "http://localhost:8000/api/users/1/",
    "username": "peter",
    "email": "sptzxbbb@gmail.com",
    "is_staff": true,
    "profile": "http://localhost:8000/api/profiles/1/",
    "project_published": [
        1
    ]
}
```

## Profile

```json
{
    "url": "http://localhost:8000/api/profiles/1/",
    "realname": "张三",
    "phone": "18800000000",
    "school": "Sun Yat-Sen University",
    "department": "School of Data and Computer Science",
    "major": "Software Engineering",
    "grade": "2013",
    "description": "This is a description",
    "role": "common",
    "tags": [
        "tag1",
        "tag2",
        "tag3"
    ],
    "owner": "http://localhost:8000/api/users/1/",
    "commentList": [
        "http://localhost:8000/api/comments/1/",
        "http://localhost:8000/api/comments/2/"
    ]
}
```

## Project

```json
{
    "url": "http://localhost:8000/api/projects/2/",
    "owner": "user002",
    "title": "Demo Project 2",
    "description": "Enter your description here",
    "school": [
        "Sun Yat-sen University",
        "South China University of Technology"
    ],
    "department": [
        "School of Data and Computer Science",
        "School of Engineering"
    ],
    "major": [
        "Software Engineering",
        "Computer Science and Technology"
    ],
    "deadline": "2016-05-30T17:51:46Z",
    "min_num": 3,
    "max_num": 10
}
```


## Team

```json
{
    "url": "http://localhost:8000/api/teams/1/",
    "name": "Demo Team 1",
    "tags": [
        "tag1",
        "tag2",
        "tag3"
    ],
    "description": "Enter your description here",
    "is_confirmed": false,
    "is_special": false,
    "owner": "http://localhost:8000/api/users/1/",
    "project": "http://localhost:8000/api/projects/1/",
    "memberList": [
        "http://localhost:8000/api/users/1/"
    ]
}
```

## Comment

```json
{
    "url": "http://localhost:8000/api/comments/1/",
    "content": "Enter your comment here",
    "time": "2016-05-30T17:36:54Z",
    "owner": "http://localhost:8000/api/users/1/"
}
```

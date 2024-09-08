# News

### Category

смотреть все, остальное админы

api:

    /api/category/

пример данных которых приходит:

    {
         "id": self.category1.id,
         "name": "Category 1",
         "description": "",
         "parent": None,
         'time_created': "2024-09-07T16:39:08.890866Z"
     },
     {
         "id": self.category2.id,
         "name": "Category 2",
         "description": "asd",
         "parent": self.category1.id,
         'time_created': "2024-09-07T16:39:08.890866Z"
     },

то что надо отправлять:

    "name": "Category 1",
    "description": "",  Необизательное поле
    "parent": None,   Необизательное поле

parent - это чья подкатегория будет нужен id категории

#### Search Category

поля:

    name
    id

api:

    /api/category/?search=

### News

смотреть все, остальное админы

api:
    
    /api/news/

пример данных которых приходит:

    {
        "id": 1,
        "images": [
            {
                "image": "http://localhost:8000/media/news_images/photo_2024-09-07_09-56-20_exVD8ZP.jpg"
            },
            {
                "image": "http://localhost:8000/media/news_images/wallpaperflare.com_wallpaper.jpg"
            }
        ],
        "title": "faaff",
        "description": "ffasfa",
        "time_created": "2024-09-07T16:39:22.284079Z",
        "category": [
            1
        ]
    },

что надо отправлять:

    {
        "title": "asd",
        "description": "asd",
        "category": [
            self.category1.id
        ],
        "uploaded_images": []
    }
    

#### Информация о создание

    Создавать если вместе с фото то через multipart/form-data
    Если без фото то можно через json

    Обновлять без фото можно json
    С фото multipart/form-data

#### Search

поля:

    title
    id
    time_created

api:

    /api/news/?search=

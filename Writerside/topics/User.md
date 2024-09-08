# User

информация о пользователе


user имеет поля в бд:

    password
    last_login
    is_superuser
    username
    first_name
    last_name
    email
    is_staff
    is_active
    data_joined
    id
    middle_name
    phone_number
    date_of_birth
    key
    balance
    status



### Create User
нужно:
    
        email 
        password 
        first_name 
        last_name 
        middle_name
        date_of_birth 
        phone_number 

api:
    
    /user/create

Если успешно
отправляется сообщение на email песле этого ему нужно бедет подтвердить аккаунт

### Activate User
api:

    /user/activate/<str:uid64>/<str:token>/


### Login User
после активации иначе ошибка
нужно:
    
    email
    password

api:
    
    /user/login

Если прошло успешно, пользователя авторезировается

### Logout User
api:
    
    /user/logout

### Profile User

api:
    
    /user/profile

возвращается:

    {
        "id": 12,
        "email": "asd@gmail.com",
        "first_name": "first_name",
        "last_name": "last_name",
        "middle_name": null,
        "status": 1,
        "balance": "0.00",
        "date_of_birth": "1993-12-12",
        "key": "tgwAHTiDXNP8WgYsFvt6"
    }


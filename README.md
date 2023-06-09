# Pizza Store

#### Backend:

- Python3 DRF
- Product models: Pizza, Desert, Drink, Snack, Other
- OrderItem (GenericForeignKey)
- Shopping Cart: Client-Side Javascript
- Account models: OneToOneField (USER)

#### Frontend:

- Vue 3
- Bootstrap 5
- Pinia
- vue3-click-away (close modal window)
- axios (consection with api)

_Сustomer data is stored in Pinia and LocalStorage(auth, email, nickname, phone_number, birthday, **user_token**, last_address)_

#### Database - PostgreSQL

#### AUTHENTICATION: Token (rest_framework.authtoken)

#### Docer compose:

For local development (docker-compose.dev.yml), run the following command:

```bash
docker compose -f docker-compose.dev.yml up --build
```

For production (docker-compose.yml)

```bash
docker compose -f docker-compose.yml up --build
```

##### Check Port Availability:

! nginx used 8000

##### Check file permissions:

! project/backend/scripts/start_dev.sh
! project/backend/scripts/start_prod.sh
! project/backend/settings/wsgi.py
! project/backend/manage.py
! project/backend/gunicorn.py

##### To start :

Build and start docker compose

```bash
docker compose build
docker compose up
```

Create a superuser:

```bash
docker ps # Get container ID
docker exec -it <container ID> /bin/bash
./project/backend/manage.py createsuperuser
```

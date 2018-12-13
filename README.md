# `Event-Mania` — Popular for renting wedding, parties & events supplies

**Event-Mania** is an web application for renting any type of event party supplies.Users can look at the photos of the events we organized previously from the gallery. If users who are intrested in working with us to make event success can contact us through email or phone call. Also, you can get the quote of the rental item by submitting a online form mentioning the description of the rental Item that you are intrested in and will get back to you less than 24hrs.

### Installations

To get you started you can simply clone the `event-mania` repository and install the dependencies.

Clone the `event-mania` repository using git:

```
git clone https://github.com/angular/event-mania.git
cd event-mania
docker-compose build
```

Initialize the Django database using below commands

```
docker-compose run django bash
python manage.py migrate
python manage.py createsuperuser
```

### Run the Application

The simplest way to start the server is:

```
docker-compose up
```

Now browse to the app at `http://localhost:8000/`.

### License

Copyright (c) Mounika Addagada 2018.

This software is licensed by the author under MIT License.

This software is free of charge and I hereby granted permission any person can obtain a copy of this software and without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

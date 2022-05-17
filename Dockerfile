FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

RUN useradd -ms /bin/bash user

USER user

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

RUN mkdir /home/user/payment

WORKDIR /home/user/payment

COPY ./payment /home/user/payment

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

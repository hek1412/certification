FROM python:3.11-slim
# Устанавливаем рабочую директорию в контейнере
WORKDIR /app
# Копируем скрипт в контейнер
COPY app.py .
# Указываем аргумент сборки с дефолтным значением
ARG USER_NAME=User
# Устанавливаем значение аргумента как переменную окружения
ENV USER_NAME=${USER_NAME}
# Устанавливаем, что выполняется при запуске контейнера
CMD ["python", "app.py"]
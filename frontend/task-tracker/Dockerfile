# Используем официальный образ Node.js
FROM node:21.1.0

# Устанавливаем рабочую директорию
WORKDIR /src/app

# Копируем файлы package.json и yarn.lock для установки зависимостей
COPY package.json yarn.lock ./

# Устанавливаем зависимости
RUN yarn install

# Копируем все файлы из текущего каталога в рабочую директорию
COPY . .

# Запускаем команду для сборки фронтенда
RUN yarn build
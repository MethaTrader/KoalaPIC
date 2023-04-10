# Базовый образ
FROM node:14-alpine

# Установка рабочей директории
WORKDIR /app

# Копирование файлов package.json и package-lock.json
COPY package*.json ./

# Установка зависимостей
RUN npm install

# Копирование остальных файлов приложения
COPY . .

# Открываем порт 3000
EXPOSE 3000

# Запускаем сервер приложения
CMD ["node", "server.js"]
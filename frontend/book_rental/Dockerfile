FROM node:20-alpine3.17

WORKDIR /app

COPY package.json ./
RUN npm install

COPY . .

EXPOSE 8080

# RUN npm run serve

CMD ["npm", "run", "serve"]

FROM node:20

WORKDIR /app

COPY vacancy .
RUN npm install

CMD ["npm", "run", "dev", "--", "--host"]
FROM node:20 AS base
WORKDIR /app
COPY vacancy/package*.json ./
RUN npm install
COPY vacancy .

# ========== Dev ==========
FROM base AS dev
ENV VITE_ENV=development
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5173"]

# ========== Test ==========
FROM base AS test
ENV VITE_ENV=test
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5173"]

# ========== Prod ==========
FROM base AS build
ENV VITE_ENV=production
RUN npm run build

FROM nginx:alpine AS prod
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
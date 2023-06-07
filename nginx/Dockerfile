# FROM node:16.13.0-alpine3.11 as build-stage
# WORKDIR /app/
# COPY frontend/package.json /app/
# RUN npm cache verify
# RUN npm install
# COPY frontend /app/
# RUN npm run build

# prod
FROM nginx:latest as production-stage
# RUN rm /etc/nginx/nginx.conf
COPY nginx/nginx.conf /etc/nginx/nginx.conf

# COPY project/backend/static /usr/src/app/static/
# COPY --from=build-stage /app/dist /dist/

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
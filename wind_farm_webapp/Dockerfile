FROM node:19-slim AS build-step

WORKDIR /app

COPY package.json .
COPY yarn.lock .

RUN yarn install

ARG REACT_APP_WIND_FARM_API
ENV REACT_APP_WIND_FARM_API=$REACT_APP_WIND_FARM_API

COPY deployment/ deployment/
COPY public/ public/
COPY src/ src/

RUN yarn build

CMD ["npx", "serve", "build"]


FROM nginx:stable-alpine
COPY --from=build-step /app/build /usr/share/nginx/html
COPY ./deployment/nginx.default.conf /etc/nginx/conf.d/default.conf

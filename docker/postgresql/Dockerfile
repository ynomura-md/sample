FROM postgres:9.6.3

RUN localedef -i ja_JP -c -f UTF-8 -A /usr/share/locale/locale.alias ja_JP.UTF-8
ENV LANG ja_JP.UTF-8

ENV POSTGRES_USER pa1
ENV POSTGRES_PASSWORD test
ENV POSTGRES_DB pa1
EXPOSE 5432

FROM quoinedev/python3.7-pandas-alpine 

COPY . .
ENV SECRET_KEY = ${SECRET_KEY}
ENV DATABASE_URI = ${DATABASE_URI}
ENV DBUser = ${DBUser}
ENV MYSQL_ROOT_PASSWORD = ${MYSQL_ROOT_PASSWORD}
ENV DBserv = ${DBserv}
RUN apk update
RUN apk add libffi-dev
RUN apk add mysql-client
RUN apk add gawk
RUN apk add --no-cache --upgrade bash
RUN chmod +x chkDB.sh
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "app:app"]


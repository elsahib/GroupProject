FROM quoinedev/python3.7-pandas-alpine 

COPY . .
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "app:app"]

FROM python:3.10-silm
WORKDIR /app
COPY . /app
RUN pip install --no cache dir -r requirements.txt
EXPOSE 5000
ENV NAME world
CMD ["python", "app.py"]
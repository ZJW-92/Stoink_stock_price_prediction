FROM python:3.9

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mount the application code
ADD . .

EXPOSE 8000

# run the production server
ENTRYPOINT ["python", "client/manage.py", "runserver", "0.0.0.0:8000"]

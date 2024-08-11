FROM python:3.11

WORKDIR /app

# Copy only the required files and directories
COPY ./Bot/ /app/Bot/
COPY ./requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the `cython.py` script last so it’s available after other steps
COPY ./Bot/cython.py /app/Bot/

CMD ["python", "Bot/cython.py"]

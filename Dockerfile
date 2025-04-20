FROM python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY req.txt /app/
RUN pip install --no-cache-dir -r req.txt
COPY . /app/
# EXPOSE 8000
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
# CMD ["gunicorn", "core.wsgi:application", "--workers", "3", "--bind", "0.0.0.0:8000" , "--reload" , "--timeout", "120", "--access-logfile", "-"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
VOLUME ["/app"]
RUN pip3 install -r requirements.txt
RUN chmod +x /app.py
CMD python /app.py

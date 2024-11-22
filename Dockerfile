FROM python:3

COPY . /home/azureuser/practice

WORKDIR /home/azureuser/practice

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "./app/src/app.py", "&"] 

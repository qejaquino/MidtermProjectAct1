#!/bin/bash

mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

cp ../main.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

echo "FROM python" >> tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "RUN pip install SQLAlchemy" >> tempdir/Dockerfile
echo "RUN pip install flask_sqlalchemy" >> tempdir/Dockerfile
echo "RUN pip install flask_login" >> tempdir/Dockerfile
echo "COPY  ./static /static/" >> tempdir/Dockerfile
echo "COPY  ./templates /templates/" >> tempdir/Dockerfile
echo "COPY  main.py /project/" >> tempdir/Dockerfile
echo "EXPOSE 4040" >> tempdir/Dockerfile
echo "CMD python /main.py" >> tempdir/Dockerfile

cd tempdir
docker build -t serverapp .
docker run -t -d -p 4040:4040 --name designrun serverapp
docker ps -a 

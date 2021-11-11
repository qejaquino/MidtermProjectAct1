#!/bin/bash

mkdir tempdir
mkdir tempdir/website

cp main.py tempdir/.
cp -r website/* tempdir/website/.


echo "FROM python" >> tempdir/Dockerfile
echo "RUN pip3 install flask" >> tempdir/Dockerfile
echo "RUN pip3 install flask_sqlalchemy" >> tempdir/Dockerfile
echo "RUN pip3 install flask_login" >> tempdir/Dockerfile
echo "COPY  ./website/ /home/myapp/website/" >> tempdir/Dockerfile
echo "COPY  main.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 4040" >> tempdir/Dockerfile
echo "RUN ls -la"
echo "CMD python3 /home/myapp/main.py" >> tempdir/Dockerfile

cd tempdir
docker build -t serverapp .
docker run -t -d -p 4040:4040 --name designrun serverapp
docker ps -a 

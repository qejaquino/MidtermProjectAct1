FROM python
RUN pip install flask
COPY  ./static /home/devasc/Desktop/midproj/MidtermProjectAct1/MidtermProjectAct1/project/static/
COPY  ./templates /home/devasc/Desktop/midproj/MidtermProjectAct1/MidtermProjectAct1/project/templates/
COPY  main.py /home/devasc/Desktop/midproj/MidtermProjectAct1/MidtermProjectAct1/project/
EXPOSE 4040
CMD python /home/devasc/Desktop/midproj/MidtermProjectAct1/MidtermProjectAct1/project/main.py
FROM python
RUN pip install flask
COPY  ./static /static/
COPY  ./templates /templates/
COPY  main.py /project/
EXPOSE 4040
CMD python /main.py

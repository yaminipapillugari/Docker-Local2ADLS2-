#Deriving the latest base image
FROM debian:latest
#Labels as key value pair
#LABEL Maintainer="yamini"
RUN mkdir -p /opt/data
#RUN echo "$pwd"

ENV filepath /opt/data
# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /home
#to COPY the remote file at working directory in container
COPY main.py ./
COPY adlsconn.py ./
COPY config.ini ./
COPY sqlconn.py ./

RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install pip -y
#RUN apt-get install unixodbc-dev -y
RUN apt-get install curl -y

RUN pip install pandas
RUN pip install azure-storage-file-datalake
RUN pip install openpyxl
RUN pip install pyodbc

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18
RUN ACCEPT_EULA=Y apt-get install -y mssql-tools18
RUN echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc
#source ~/.bashrc
RUN apt-get install -y unixodbc-dev
RUN apt-get install -y libgssapi-krb5-2
#RUN apt-get install unixODBC-devel
# Now the structure looks like this '/usr/app/src/test.py'
#RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql unixodbc-dev
#CMD instruction should be used to run the software
#contained by your image, along with any arguments.
#RUN python3 ./main.py
#CMD echo "program completed"
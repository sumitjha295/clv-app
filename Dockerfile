############################################################
# Dockerfile to build for test Applications python3 MySQL
# Based on Ubuntu16.04
############################################################
FROM sumitjha295/u16p36mysql:latest

MAINTAINER Sumit "sumitjha295@gmail.com"
################## BEGIN INSTALLATION ######################
RUN chown -R mysql:mysql /var/lib/mysql /var/run/mysqld && \
    service mysql start && usermod -d /var/lib/mysql/ mysql
RUN rm -rf /home/ls-app/
COPY . /home/ls-app/
WORKDIR /home/ls-app/
RUN chmod 755 ./build.sh && ./build.sh
RUN chmod 755 ./run.sh

##################### INSTALLATION END #####################
ENTRYPOINT ["./run.sh"]
# Expose the default port
EXPOSE 5000
EXPOSE 3306

FROM phusion/baseimage:0.9.17
MAINTAINER datawire.io <hello@datawire.io>

# ------------------------------------------------------------------------------
# Setup (Do Not Edit)
#

COPY . /img_build
RUN /img_build/install.sh

RUN cp /img_build/bin/bakerconf.py /bin/bakerconf
RUN cp /img_build/init/10_bakerconf.sh /etc/my_init.d/10_bakerconf.sh

RUN mkdir /etc/service/watson
RUN cp /img_build/service/watson.sh /etc/service/watson/run

RUN mkdir /etc/service/sherlock
RUN cp /img_build/service/sherlock.sh /etc/service/sherlock/run

RUN cp /img_build/conf/datawire.conf /etc/datawire/datawire.conf

# ------------------------------------------------------------------------------
# Customize (Edit)

# Modify or add additional RUN commands to copy files from the /img_build directory, for example, a Java-based service
# might want to copy a runnable JAR instead.
RUN cp /img_build/hello.py /opt/hello.py

# Modify the name of your service below, for example, right now it is "hello", but if your service is a calculator you
# should change "hello" to something like "calculator". Do not forget to modify the name of the initialization script
# also.
RUN mkdir /etc/service/hello
RUN cp /img_build/service/hello.sh /etc/service/hello/run

# Indicate the exposed port for your service.
EXPOSE 8080

# ------------------------------------------------------------------------------
# Cleanup

RUN /img_build/cleanup.sh

FROM phusion/baseimage:0.9.17
MAINTAINER datawire.io <hello@datawire.io>

# ------------------------------------------------------------------------------
# Setup (Do Not Edit)
#

COPY . /img_build
RUN /img_build/install.sh

# TODO(plombardi): move this into the future datawire-bakerstreet package
RUN cp /img_build/bin/bakerconf.py /bin/bakerconf
RUN cp /img_build/init/10_bakerconf.sh /etc/my_init.d/10_bakerconf.sh

RUN mkdir /etc/service/watson
RUN cp /img_build/service/watson.sh /etc/service/watson/run

RUN mkdir /etc/service/sherlock
RUN cp /img_build/service/sherlock.sh /etc/service/sherlock/run

RUN cp /img_build/conf/datawire.conf /etc/datawire/datawire.conf

# ------------------------------------------------------------------------------
# Customize (Edit)

RUN cp /img_build/hello.py /opt/hello.py

RUN mkdir /etc/service/hello
RUN cp /img_build/service/hello.sh /etc/service/hello/run

# ------------------------------------------------------------------------------
# Cleanup 
# 

RUN /img_build/cleanup.sh

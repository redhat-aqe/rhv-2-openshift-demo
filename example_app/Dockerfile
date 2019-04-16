FROM registry.access.redhat.com/rhel7:latest

LABEL maintainer="Ales Raszka <araszka@redhat.com>"
LABEL description="Example Flask app"
LABEL summary="This application just demonstrates running app in Openshift"

ARG USER_UID=1002

USER root

RUN yum repolist --disablerepo=* && \
    yum-config-manager --disable \* > /dev/null && \
    yum-config-manager --enable rhel-7-server-rpms > /dev/null && \
    yum-config-manager --enable rhel-7-server-extras-rpms > /dev/null && \
    yum-config-manager --enable rhel-7-server-optional-rpms > /dev/null

RUN yum update -y && \
    yum install -y python-flask && \
    yum clean all

RUN useradd -ms /bin/bash -u "${USER_UID}" service

COPY requirements.txt /home/service/requirements.txt
COPY setup.py /home/service/setup.py
COPY src/ /home/service/src/

WORKDIR /home/service
RUN python /home/service/setup.py install -O1 --skip-build

# set dir ownership
# https://docs.openshift.com/container-platform/3.11/creating_images/guidelines.html#openshift-specific-guidelines
RUN chgrp -R 0 /home/service /etc/passwd
RUN chmod -R g=u /home/service /etc/passwd

EXPOSE 8080
USER "${USER_UID}"

ENTRYPOINT [ "python", "/usr/bin/flask-app"]
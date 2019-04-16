FROM registry.access.redhat.com/rhscl/python-36-rhel7:latest

LABEL maintainer="Ales Raszka <araszka@redhat.com>"
LABEL description="Example Flask app"
LABEL summary="This application just demonstrates running app in Openshift"

ARG USER_UID=1002

USER root

RUN yum update -y && \
    yum clean all

RUN useradd -ms /bin/bash -u "${USER_UID}" service

COPY setup.py /home/service/setup.py
COPY src/ /home/service/src/
COPY requirements.txt /home/service/requirements.txt

WORKDIR /home/service
RUN pip install -r requirements.txt
RUN python /home/service/setup.py install -O1 --skip-build

# set dir ownership
# https://docs.openshift.com/container-platform/3.11/creating_images/guidelines.html#openshift-specific-guidelines
RUN chgrp -R 0 /home/service /etc/passwd
RUN chmod -R g=u /home/service /etc/passwd

EXPOSE 8080
USER "${USER_UID}"

ENTRYPOINT [ "python", "/opt/app-root/bin/flask-app"]
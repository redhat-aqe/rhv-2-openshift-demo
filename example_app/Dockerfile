FROM fedora:29

MAINTAINER Ales Raszka <araszka@redhat.com>
LABEL description="Example Flask app"
LABEL summary="This application just demonstrates running app in Openshift"

ARG USER_UID=1001

USER root

RUN dnf update -y && \
    dnf install -y \
    python3-devel \
    python3-pip && \
    dnf clean all

RUN useradd -ms /bin/bash -u "${USER_UID}" service

COPY setup.py /home/service/setup.py
COPY src/ /home/service/src/
COPY requirements.txt /home/service/requirements.txt

WORKDIR /home/service
RUN pip3 install -r requirements.txt
RUN python3 /home/service/setup.py install -O1 --skip-build

# set dir ownership
# https://docs.openshift.com/container-platform/3.11/creating_images/guidelines.html#openshift-specific-guidelines
RUN chgrp -R 0 /home/service /etc/passwd
RUN chmod -R g=u /home/service /etc/passwd

EXPOSE 8080
USER "${USER_UID}"

ENTRYPOINT [ "python3", "/usr/local/bin/flask-app"]
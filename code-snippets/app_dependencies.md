# Application & dependencies

Application and dependencies are installed directly in Dockerfile

```Dockerfile
FROM ....

....
RUN dnf update -y && \
    dnf install -y \
    python3-devel \
    python3-pip && \
    dnf clean all

# install app dependencies
RUN pip3 install -r requirements.txt
# install application from source
RUN python3 /home/service/setup.py install -O1 --skip-build

```
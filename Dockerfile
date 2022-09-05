FROM ubuntu:jammy-20220531
USER root
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3 
RUN apt install python3-pip -y
RUN pip install awscli
EXPOSE 22
CMD ["/bin/bash"]

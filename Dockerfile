FROM ubuntu:jammy-20220531
USER root
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3
RUN apt install python3-pip -y
RUN pip3 install requests
RUN apt install curl -y
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl && mkdir /.kube && touch /.kube/config && export PATH=/usr/local/bin/kubectl:$PATH
COPY cd.py .
CMD ["/bin/bash"]

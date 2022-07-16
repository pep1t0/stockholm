FROM ubuntu:latest
LABEL Jose Daniel Requena daniel.requena@aol.com
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install openssh-server -y
RUN apt-get install vsftpd -y
RUN apt-get install git -y
RUN useradd -s /bin/bash -m -d /home/jorequen jorequen
RUN echo "jorequen:password1" | chpasswd
RUN echo "root:password1" | chpasswd
RUN mkdir /home/jorequen/infection
COPY ./infection /home/jorequen/infection
RUN mkdir /root/.ssh
RUN mkdir /var/run/sshd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
RUN sed -i 's/#Port 22/Port 4242/' /etc/ssh/sshd_config
RUN echo "listen_port=4141" >> /etc/vsftpd.conf  
EXPOSE 4141 4242
CMD ["/usr/sbin/sshd","-D"]
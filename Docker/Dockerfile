FROM ubuntu:22.04
RUN apt update && apt upgrade -y
RUN apt-get upgrade -y
RUN apt install -y wget
RUN apt install -y openssh-server
run apt install nano -y
run apt install python3 -y
run echo $PATH
ENV PATH="$PATH:/erc/profile"
run echo $PATH


ENTRYPOINT ["/bin/bash"]

run  mkdir -p /proteus
workdir "/proteus"

# install c++ depenedencies
run apt install cmake -y
run apt install build-essential -y
run apt install git -y

# Making Directories
# C++ Proteus
RUN git clone https:[insert token]h@github.com/csun-tavlab/proteus.git
workdir "/proteus/proteus"

run mkdir -p /proteus/proteus/build
workdir "/proteus/proteus/build"
run cmake ..
run make -j 5

run mv proteus C++Proteus
# run echo "export PATH=/proteus/proteus/build:$PATH" >> /root/.bashrc
# cmd source /root/.bashrc

run echo "export PATH='/proteus/proteus/build:$PATH'" >> /root/.profile
run echo $PATH

ENV PATH="${PATH}:/proteus/proteus/build"

# Swift Proteus Installation
workdir "/proteus"
run apt install clang -y
run apt install libpython2.7 -y 
run apt install libpython2.7-dev -y
run wget https://swift.org/builds/swift-5.8-release/ubuntu2004/swift-5.8-RELEASE/swift-5.8-RELEASE-ubuntu20.04.tar.gz
run tar xzf swift-5.8-RELEASE-ubuntu20.04.tar.gz
run mv swift-5.8-RELEASE-ubuntu20.04 /usr/share/swift

ENV PATH="${PATH}:/usr/share/swift/usr/bin"

# Cloning Swift Proteus
workdir "/proteus"
run git clone  https://[insert token]@github.com/csun-tavlab/swift-proteus.git

#Updating files for Swift Proteus
workdir "/proteus/swift-proteus"         
add Package.swift  /proteus/swift-proteus
add main.swift /proteus/swift-proteus/Sources


# Building Swift Proteus
workdir "/proteus/swift-proteus/Sources"
run rm /proteus/swift-proteus/Sources/Main.swift
run /usr/share/swift/usr/bin/swift build

# Setting Environmental Variables

workdir "/proteus/swift-proteus/.build/debug"
run mv Proteus SwiftProteus

run echo "export PATH='/proteus/swift-proteus/.build/debug:$PATH'" >> /root/.profile
run echo $PATH

ENV PATH="${PATH}:/proteus/swift-proteus/.build/debug"


workdir "/proteus"
run git clone https://github.com/JoseOcampo02/proteus-test-case-generator.git




run mkdir /var/run/sshd
RUN apt install sudo -y
RUN echo 'root:root' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
CMD ["/usr/sbin/sshd", "-D"]

run apt install fish -y
run apt-get install software-properties-common -y

run add-apt-repository ppa:maveonair/helix-editor
run apt update
run apt install helix

run apt install pip -y

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London

run apt-get install python3-tk -y

workdir "/proteus/proteus-test-case-generator/demo/TestingSession"
run mkdir GeneratedTests

workdir "/proteus"

ENV TERM=xterm-256color
RUN echo "PS1='\e[92m\u\e[0m@\e[94m\h\e[0m:\e[35m\w\e[0m# '" >> /root/.bashrc

run echo "hello"

EXPOSE 22
ENTRYPOINT service ssh start && bash


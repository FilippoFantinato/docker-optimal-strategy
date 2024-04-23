FROM ubuntu:latest

WORKDIR /home/
COPY optimal-strategy /bin/optimal-strategy
COPY simple-synth /bin/simple-synth
COPY NuSMV /bin/NuSMV
COPY nuXmv /bin/nuXmv

ENTRYPOINT ["optimal-strategy"]

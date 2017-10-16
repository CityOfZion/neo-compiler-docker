FROM java:8

RUN mkdir /build
RUN mkdir /build/files

WORKDIR /build/files

COPY org.neo.smartcontract.framework.jar /build

ENTRYPOINT ["javac", "-d", "/build/files", "-sourcepath", "/build/files", "-cp", "/build/org.neo.smartcontract.framework.jar"]
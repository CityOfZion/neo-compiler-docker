FROM python:3.5
LABEL maintainer="@revett"

WORKDIR /compile
COPY compile.py /compile

RUN pip install neo-boa

ENTRYPOINT ["python", "/compile/compile.py"]
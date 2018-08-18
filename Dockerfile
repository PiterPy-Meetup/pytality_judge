FROM python:alpine3.7

COPY judge.py /judge/

WORKDIR /judge

ENTRYPOINT [ "python", "judge.py" ]
# Dockerfile for building copy

FROM python:bookworm

COPY *.py .
RUN pip install pyinstaller 
RUN python3 build.py
FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app

COPY extract_outline.py .

RUN pip install pymupdf

ENTRYPOINT ["python", "extract_outline.py"]

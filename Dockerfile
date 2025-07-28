FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app

COPY extract_entities.py .

# Install PyMuPDF and spaCy
RUN pip install pymupdf spacy \
 && python -m spacy download en_core_web_sm

ENTRYPOINT ["python", "extract_entities.py"]

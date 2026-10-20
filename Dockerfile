FROM python:3.12-alpine
WORKDIR /app/src
COPY LICENSE NOTICE THIRD-PARTY-NOTICES.md /app/
COPY src/ /app/src/
ARG REGISTRY_SOURCE=config/registry.json
COPY ${REGISTRY_SOURCE} /app/config/registry.json
COPY web/ /app/web/
COPY catalog/ /app/catalog/
COPY trust/huebridge-ca.pem /app/trust/huebridge-ca.pem
USER 10001:10001
EXPOSE 8443
CMD ["python", "-u", "app.py"]

FROM python:3.12-alpine
WORKDIR /app
COPY LICENSE NOTICE THIRD-PARTY-NOTICES.md /app/
COPY lamp_types.py app.py hue_client.py color.py dashboard.py admin_auth.py loxone_export.py bridge_store.py bridge_admin.py scenes.py discovery.py request_monitor.py ./
ARG REGISTRY_SOURCE=registry.json
COPY ${REGISTRY_SOURCE} /app/registry.json
COPY web/ /app/web/
COPY catalog/ /app/catalog/
COPY trust/huebridge-ca.pem /app/trust/huebridge-ca.pem
USER 10001:10001
EXPOSE 8443
CMD ["python", "-u", "app.py"]

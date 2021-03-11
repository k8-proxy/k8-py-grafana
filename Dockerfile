FROM python:3.7-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app
RUN mkdir /var/log/py-grafana

EXPOSE 3000

ENTRYPOINT ["python3"]

CMD ["-m", "unittest", "dashboard-api.tests.test_grafana_dashboard.TestGrafanaDashboard.test_create_dashboard"]
CMD ["-m", "unittest", "dashboard-api.tests.test_grafana_dashboard.TestGrafanaDashboard.test_import_dashboard"]
CMD ["-m", "unittest", "dashboard-api.tests.test_grafana_dashboard.TestGrafanaDashboard.test_delete_dashboard"]


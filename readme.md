## Grafana api wrapper for dashboard interactions.

Create virtual environement

``` 
    cd .\packer\target\logtrixia\setup\dashboard\dashboard-api 
    python -m venv <your_env_name>
    <your_env_name>\Scripts\activate (for windows)
    source <your_env_name>/bin/activate (for linux) 
```

To install dependencies run command

```pip3 install -r requirements.txt```

## Run tests
``` cd .. ```

### Test dashboard creation
``` python -m unittest dashboard-api.tests.test_grafana_dashboard.TestGrafanaDashboard.test_create_dashboard ```

### Test dashboard deletion
``` python -m unittest dashboard-api.tests.test_grafana_dashboard.TestGrafanaDashboard.test_delete_dashboard ```

### Test dashboard export and import
- Export dashboard json into python object

``` python -m unittest dashboard-api.tests.test_grafana_dashboard.TestGrafanaDashboard.test_get_dashboard ```

- Update the env variable "dashboard_json" inside config.py with the json returned above.

- Pass the json object to import method to create a copy of the dashboard

``` python -m unittest dashboard-api.tests.test_grafana_dashboard.TestGrafanaDashboard.test_import_dashboard ```


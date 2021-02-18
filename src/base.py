from ..config import Config
from grafana_api.grafana_face import GrafanaFace


class Base:
    def __init__(self):
        self.__config = Config() 
        self.cross_server_import = self.__config.cross_server_import           
        self.__grafana_details = self.__config.graphana_api_details()
        self.__target_grafana_details = self.__config.target_grafana_api_details()

    def login(self, auth_type="key", target_server=True):
        print(self)
        print(self.__config, self.__grafana_details)

        # login to target/cross server if set to true
        if cross_server:
            self.__grafana_details = self.__target_grafana_details

        if auth_type == "key":
            self.grafana_api = GrafanaFace(
                auth=(self.__grafana_details["auth_key"]),
                host=self.__grafana_details["host"]
            )
        else:
            self.grafana_api = GrafanaFace(
                auth=(self.__grafana_details["username"], self.__grafana_details["password"]),
                host=self.__grafana_details["host"]
            )
        
        return self.grafana_api


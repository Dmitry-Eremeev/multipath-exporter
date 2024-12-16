import logging
import sys
import yaml

class WebConfig:
    def __init__(self, web_config_file=None):
        self._raw_config = self._load_config_file(web_config_file)
        self.tls_server_config = TLSServerConfig(self._raw_config)

    def get_tls_config_for_http_server(self):
        tls_settings = dict()
        tls_settings["certfile"] = self.tls_server_config.cert_file
        tls_settings["keyfile"] = self.tls_server_config.key_file
        tls_settings["client_cafile"] = self.tls_server_config.client_ca_file
        client_auth_type = self.tls_server_config.client_auth_type
        tls_settings["client_auth_required"] = client_auth_type == "RequireAndVerifyClientCert"
        return tls_settings

    @staticmethod
    def _load_config_file(web_config_file=None):
        if web_config_file:
            # test invalid yaml and path
            try:
                with open(web_config_file) as file:
                    return yaml.safe_load(file)
            except FileNotFoundError:
                logging.error("web config file %s was not found." % web_config_file)
                sys.exit(1)
            except yaml.YAMLError:
                logging.error("web config file %s is invalid YAML file." % web_config_file)
                sys.exit(1)


class TLSServerConfig:
    def __init__(self, raw_config):
        self._tls_config = raw_config.get("tls_server_config", dict()) if raw_config else dict()
        self.cert_file = self._tls_config.get("cert_file")
        self.key_file = self._tls_config.get("key_file")
        self.client_auth_type = self._tls_config.get("client_auth_type", "NoClientCert")
        self.client_ca_file = self._tls_config.get("client_ca_file")

# multipath_exporter

Linux FC multipath exporter on Python

```sh
pip install -r requirements.txt --no-deps
./multipath_exporter/main.py
```

## TLS

The Multipath Exporter supports TLS.

To use TLS, you need to pass a configuration file
using the `--web.config.file` parameter. The format of the file is described
[in the exporter-toolkit repository](https://github.com/prometheus/exporter-toolkit/blob/master/docs/web-configuration.md).
Supported config options: 'client_ca_file', 'cert_file' 'key_file', 'client_auth_type' in section 'tls_server_config'.

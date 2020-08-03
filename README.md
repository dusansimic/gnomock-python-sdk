# gnomock-python-sdk
`gnomock` is an HTTP wrapper for [Gnomock](https://github.com/orlangure/gnomock) integration and end-to-end testing toolkit. It allows to use Gnomock outside of Go ecosystem. Not all Gnomock features exist in this wrapper, but official presets, as well as basic general configuration, are supported.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.4.1
- Package version: 1.4.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/orlangure/gnomock/](https://github.com/orlangure/gnomock/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/orlangure/gnomock-python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/orlangure/gnomock-python-sdk.git`)

Then import the package:
```python
import gnomock
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import gnomock
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import gnomock
from gnomock.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:23042
# See configuration.py for a list of all supported configuration parameters.
configuration = gnomock.Configuration(
    host = "http://127.0.0.1:23042"
)



# Enter a context with an instance of the API client
with gnomock.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gnomock.PresetsApi(api_client)
    localstack_request = gnomock.LocalstackRequest() # LocalstackRequest | 

    try:
        # Start a new Gnomock Localstack container
        api_response = api_instance.start_localstack(localstack_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PresetsApi->start_localstack: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *http://127.0.0.1:23042*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PresetsApi* | [**start_localstack**](docs/PresetsApi.md#start_localstack) | **POST** /start/localstack | Start a new Gnomock Localstack container
*PresetsApi* | [**start_memcached**](docs/PresetsApi.md#start_memcached) | **POST** /start/memcached | Start a new Gnomock Memcached container
*PresetsApi* | [**start_mongo**](docs/PresetsApi.md#start_mongo) | **POST** /start/mongo | Start a new Gnomock MongoDB container
*PresetsApi* | [**start_mssql**](docs/PresetsApi.md#start_mssql) | **POST** /start/mssql | Start a new Gnomock Microsoft SQL Server container
*PresetsApi* | [**start_mysql**](docs/PresetsApi.md#start_mysql) | **POST** /start/mysql | Start a new Gnomock MySQL container
*PresetsApi* | [**start_postgres**](docs/PresetsApi.md#start_postgres) | **POST** /start/postgres | Start a new Gnomock Postgres container
*PresetsApi* | [**start_rabbit_mq**](docs/PresetsApi.md#start_rabbit_mq) | **POST** /start/rabbitmq | Start a new Gnomock RabbitMQ container
*PresetsApi* | [**start_redis**](docs/PresetsApi.md#start_redis) | **POST** /start/redis | Start a new Gnomock Redis container
*PresetsApi* | [**start_splunk**](docs/PresetsApi.md#start_splunk) | **POST** /start/splunk | Start a new Gnomock Splunk container
*PresetsApi* | [**stop**](docs/PresetsApi.md#stop) | **POST** /stop | Stop an existing Gnomock container


## Documentation For Models

 - [Container](docs/Container.md)
 - [InvalidStartRequest](docs/InvalidStartRequest.md)
 - [InvalidStopRequest](docs/InvalidStopRequest.md)
 - [Localstack](docs/Localstack.md)
 - [LocalstackRequest](docs/LocalstackRequest.md)
 - [Memcached](docs/Memcached.md)
 - [MemcachedRequest](docs/MemcachedRequest.md)
 - [Mongo](docs/Mongo.md)
 - [MongoRequest](docs/MongoRequest.md)
 - [Mssql](docs/Mssql.md)
 - [MssqlRequest](docs/MssqlRequest.md)
 - [Mysql](docs/Mysql.md)
 - [MysqlRequest](docs/MysqlRequest.md)
 - [Options](docs/Options.md)
 - [Postgres](docs/Postgres.md)
 - [PostgresRequest](docs/PostgresRequest.md)
 - [Rabbitmq](docs/Rabbitmq.md)
 - [RabbitmqRequest](docs/RabbitmqRequest.md)
 - [Redis](docs/Redis.md)
 - [RedisRequest](docs/RedisRequest.md)
 - [Splunk](docs/Splunk.md)
 - [SplunkRequest](docs/SplunkRequest.md)
 - [SplunkValues](docs/SplunkValues.md)
 - [StartFailed](docs/StartFailed.md)
 - [StopFailed](docs/StopFailed.md)
 - [StopRequest](docs/StopRequest.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author





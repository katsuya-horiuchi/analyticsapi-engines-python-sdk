# fds.analyticsapi.engines.DocumentsApi

All URIs are relative to *https://api.factset.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pa3_documents**](DocumentsApi.md#get_pa3_documents) | **GET** /analytics/lookups/v2/engines/pa/documents/{path} | Get PA3 documents and sub-directories in a directory
[**get_spar3_documents**](DocumentsApi.md#get_spar3_documents) | **GET** /analytics/lookups/v2/engines/spar/documents/{path} | Gets SPAR3 documents and sub-directories in a directory
[**get_vault_documents**](DocumentsApi.md#get_vault_documents) | **GET** /analytics/lookups/v2/engines/vault/documents/{path} | Get Vault documents and sub-directories in a directory


# **get_pa3_documents**
> DocumentDirectories get_pa3_documents(path)

Get PA3 documents and sub-directories in a directory

This endpoint looks up all PA3 documents and sub-directories in a given directory.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import fds.analyticsapi.engines
from fds.analyticsapi.engines.rest import ApiException
from pprint import pprint
configuration = fds.analyticsapi.engines.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://api.factset.com
configuration.host = "https://api.factset.com"
# Create an instance of the API class
api_instance = fds.analyticsapi.engines.DocumentsApi(fds.analyticsapi.engines.ApiClient(configuration))
path = 'path_example' # str | The directory to get the documents and sub-directories in

try:
    # Get PA3 documents and sub-directories in a directory
    api_response = api_instance.get_pa3_documents(path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get_pa3_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The directory to get the documents and sub-directories in | 

### Return type

[**DocumentDirectories**](DocumentDirectories.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response, returns a list of PA3 documents and directories |  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  |
**400** | Invalid query parameter or value provided |  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  |
**401** | Missing or invalid authentication |  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  |
**403** | User is forbidden with current credentials |  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  |
**404** | Path not found |  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  |
**406** | Unsupported Accept header.  Header needs to be set to application/json |  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  |
**500** | Server error. Log the X-DataDirect-Request-Key header to assist in troubleshooting |  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  |
**503** | Request timed out. Retry the request in some time |  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spar3_documents**
> DocumentDirectories get_spar3_documents(path)

Gets SPAR3 documents and sub-directories in a directory

This endpoint looks up all SPAR3 documents and sub-directories in a given directory.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import fds.analyticsapi.engines
from fds.analyticsapi.engines.rest import ApiException
from pprint import pprint
configuration = fds.analyticsapi.engines.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://api.factset.com
configuration.host = "https://api.factset.com"
# Create an instance of the API class
api_instance = fds.analyticsapi.engines.DocumentsApi(fds.analyticsapi.engines.ApiClient(configuration))
path = 'path_example' # str | The directory to get the documents in

try:
    # Gets SPAR3 documents and sub-directories in a directory
    api_response = api_instance.get_spar3_documents(path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get_spar3_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The directory to get the documents in | 

### Return type

[**DocumentDirectories**](DocumentDirectories.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response, returns a list of SPAR3 documents and directories |  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  |
**400** | Invalid query parameter or value provided |  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  |
**401** | Missing or invalid authentication |  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  |
**403** | User is forbidden with current credentials |  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  |
**404** | Path not found |  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  |
**406** | Unsupported Accept header.  Header needs to be set to application/json |  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  |
**500** | Server error. Log the X-DataDirect-Request-Key header to assist in troubleshooting |  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  |
**503** | Request timed out. Retry the request in some time |  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_documents**
> DocumentDirectories get_vault_documents(path)

Get Vault documents and sub-directories in a directory

This endpoint looks up all Vault documents and sub-directories in a given directory.

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import fds.analyticsapi.engines
from fds.analyticsapi.engines.rest import ApiException
from pprint import pprint
configuration = fds.analyticsapi.engines.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://api.factset.com
configuration.host = "https://api.factset.com"
# Create an instance of the API class
api_instance = fds.analyticsapi.engines.DocumentsApi(fds.analyticsapi.engines.ApiClient(configuration))
path = 'path_example' # str | The directory to get the documents in

try:
    # Get Vault documents and sub-directories in a directory
    api_response = api_instance.get_vault_documents(path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get_vault_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The directory to get the documents in | 

### Return type

[**DocumentDirectories**](DocumentDirectories.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response, returns a list of Vault documents and directories |  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  |
**400** | Invalid query parameter or value provided |  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  |
**401** | Missing or invalid authentication |  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  |
**403** | User is forbidden with current credentials |  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  |
**404** | Path not found |  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  |
**406** | Unsupported Accept header.  Header needs to be set to application/json |  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  |
**500** | Server error. Log the X-DataDirect-Request-Key header to assist in troubleshooting |  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  |
**503** | Request timed out. Retry the request in some time |  * X-RateLimit-Remaining - Number of requests left for the time window. <br>  * X-FactSet-Api-Request-Key - Key to uniquely identify an Analytics API request. Only available after successful authentication. <br>  * X-RateLimit-Reset - Number of seconds remaining till rate limit resets. <br>  * X-RateLimit-Limit - Number of allowed requests for the time window. <br>  * X-DataDirect-Request-Key - FactSet&#39;s request key header. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


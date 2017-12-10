# swagger_client.ServletApi

All URIs are relative to *http://&lt;host&gt;/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_loaded_servlets**](ServletApi.md#get_loaded_servlets) | **GET** /servlet | Loaded servlets


# **get_loaded_servlets**
> ServletsResponse get_loaded_servlets()

Loaded servlets

Get a map of all the servlets loaded on the server. The key is the path under which the servlet is available, and the value is the class name of the implementing class of the servlet.  > Required permission: servlet.list 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerKey
swagger_client.configuration.api_key['x-webapi-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['x-webapi-key'] = 'Bearer'
# Configure API key authorization: queryKey
swagger_client.configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ServletApi()

try: 
    # Loaded servlets
    api_response = api_instance.get_loaded_servlets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServletApi->get_loaded_servlets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServletsResponse**](ServletsResponse.md)

### Authorization

[headerKey](../README.md#headerKey), [queryKey](../README.md#queryKey)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

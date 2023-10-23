
# HTTP Status Codes
From ChatGPT. The italicized ones are less common
## 1xx Informational Responses
- **100 Continue**
  - The server has received the initial part of the request and the client should proceed to send the remainder of the request.
  - Use when the server wants to confirm that the client can continue with the request.

- *101 Switching Protocols*
  - The requester has asked the server to switch protocols.
  - Use when the client requests a protocol change, such as switching to WebSocket.

## 2xx Success
- **200 OK**
  - The request was successful, and the server has fulfilled the request.
  - Use for successful GET or POST requests.

- **201 Created**
  - The request was successful, and a new resource was created as a result.
  - Use when a new resource is successfully created as a result of a POST request.

- **204 No Content**
  - The server successfully processed the request, but there is no content to send in the response.
  - Use when you want to acknowledge a request without sending any data in the response body.

- *205 Reset Content*
  - The server successfully processed the request, but the client should reset the document view.
  - Rarely used in practice.

## 3xx Redirection
- **301 Moved Permanently**
  - The requested resource has been permanently moved to a different URL.
  - Use when a resource has been moved permanently to a new location.

- **302 Found**
  - The requested resource has been temporarily moved to a different URL.
  - Use for temporary redirects. Note: Consider using 303 or 307 for POST requests.

- *303 See Other*
  - The response to the request can be found under a different URL.
  - Use to direct the client to a different resource after a POST request.

- *304 Not Modified*
  - Indicates that the resource has not been modified since the version specified by the request headers.
  - Use to reduce server load by instructing the client to use its cached copy of the resource.

## 4xx Client Errors
- **400 Bad Request**
  - The server could not understand the request due to malformed syntax.
  - Use when the client sends a request that cannot be understood by the server, such as invalid JSON format.

- **401 Unauthorized**
  - The client must authenticate itself to get the requested response.
  - Use when authentication is required and has failed or has not been provided.

- **403 Forbidden**
  - The client does not have access rights to the content.
  - Use when the client is authenticated but does not have permission to access the requested resource.

- **404 Not Found**
  - The server cannot find the requested resource.
  - Use when the requested resource is not available on the server.
- *418 I'm a teapot (not a part of the official HTTP/1.1 standard)*
  - Any attempt to brew coffee with a teapot should result in the error code "418 I'm a teapot".
  - This code was defined in 1998 as one of the traditional IETF April Fools' jokes, in RFC 2324, Hyper Text Coffee Pot Control Protocol.
  - Use this status code when you want to add a touch of humor to an otherwise straightforward HTTP response, especially if you're dealing with a teapot or any other device humorously pretending to be a teapot.


- **429 Too Many Requests**
  - The user has sent too many requests in a given amount of time.
  - Use to indicate that the client has exceeded the rate limits imposed by the server.

## 5xx Server Errors
- **500 Internal Server Error**
  - A generic error message returned when an unexpected condition was encountered.
  - Use when an unknown error occurred on the server side.

- **503 Service Unavailable**
  - The server is not ready to handle the request. Common causes are a server that is down for maintenance or that is overloaded.
  - Use when the server is temporarily unable to handle the request due to maintenance or high load.

- *504 Gateway Timeout*
  - The server, while acting as a gateway or proxy, did not receive a timely response from the upstream server or application.
  - Use when a server acting as a gateway or proxy does not receive a timely response from the upstream server.

- *505 HTTP Version Not Supported*
  - The server does not support the HTTP protocol version used in the request.
  - Use when the server does not support the HTTP protocol version used in the request.

- *511 Network Authentication Required*
  - The client needs to authenticate to gain network access.
  - Use when a network requires the client to authenticate to gain the network access permission.

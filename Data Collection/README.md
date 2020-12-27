# Get Verification Code from a Picture

# Getting to Know Web Crawlers

## Key steps of web crawling:
1. Acquiring data from API
 - If the data is not shown, use the web developer tool in the browser, check Network->XHR, if nothing's there try to search for data in multiple responses and find the accurate url.
 - If data in script of the page, grab it with regex.
2. Store data properly
3. Extract necessary data

## HTTP
A type of client server interaction

### Most frequently used request header info:
1. User-Agent: label of the request body
2. Connection: check whether is still connected after request
    - Status Code:
    1) 2xx successfully connected with server
    2) 3xx redirected
    3) 4xx client malfunction
    4) 5xx server side error

### Most frequently used response header info:
1. Content-Type: Data type of the response from server to client

## HTTPS

## Techniques used:
1. Using requests to capture the entire web page. 
2. Using regex for fetching data
3. Using bs4 for fetching data
4. Using xpath for fetching data

# Async Web Crawlers
Since requests.get() would jam the traffic, we need to use async based on concurrency programming in order to get pass a get method when it is stuck at a certain place.

1. Using concurrency:
 - Pros: Get pass certain stucked execution
 - Cons: Cannot open up as many different threads as we want 

2. Using thread pool with multiprocessing module:
 - Pros: Lower the cost of system
 - Cons: Still have some limits

3. Single thread + Concurrency:
  1) event_loop: infinite loop to execute
  2) coroutine: async object
  3) task: return the status of the task
  4) future: meaning the task have not yet been executed
  5) async: define a thread
  6) await: put aside the stuck task
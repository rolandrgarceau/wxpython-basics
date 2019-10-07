# Nasa API for [images](https://images.nasa.gov/docs/images.nasa.gov_api_docs.pdf)

We have a [tutorial]() to help guide us through creating an interface with NASA's API. We have another separate [tutorial](https://realpython.com/python-requests/) to guide us through requests and the convenience of using this. The first tutorial is explained in this readme. The requests explinations are in its own directory.

## Environment considerations for NASA application API interfacing

Ipython version 7.2.0 allows import urllib, urllib3 and requests. We can test our scripts prior to wxPython integration this way.

## Nasa investigation of API consumption

Read their REST documentation first.

* resource oriented URLS
* HTTP response codes for API errors
* built­in HTTP features, like HTTP authentication and HTTP verbs work with off the shelf clients
* supports CORS for client side web app interactions
* JSON format responses, including errors

### NASA API Usage for [images.nasa.gov_api_docs.pdf](https://images.nasa.gov/docs/images.nasa.gov_api_docs.pdf)

* endpoint examples use `curl`, unix pipes, with python to output API responses
* must remove newlines to run examples

### [GET /search?q={q}](https://images.nasa.gov/docs/images.nasa.gov_api_docs.pdf)

This will return a Collection + JSON result, and from within the JSON a collection that contains a href that repeats the call you just used with curl, and an array of items and possibly a data array of information pertaining to the search parameter used.

### [GET /asset/{nasa id}](https://images.nasa.gov/docs/images.nasa.gov_api_docs.pdf)

Retrieving a media asset’s manifest like so:

```sh
curl https://images-api.nasa.gov/asset/as11-40-5874 |
        python -m json.tool
```

This will return a manifest result in JSON with a collection that contains a href that repeats the call you just used with curl, and an array of items- in this case a "list" of jpg's from within the href.

### [GET /metadata/{nasa id}](https://images.nasa.gov/docs/images.nasa.gov_api_docs.pdf)

Retrieving a media asset’s metadata location. use the returned location to download the actual metadata.

### [GET /captions/{nasa id}](https://images.nasa.gov/docs/images.nasa.gov_api_docs.pdf)

GET video asset’s captions, returns "location" URL. Then download the VTT os SRT file at that returned location value to see the video's captions.

### [GET /album/{album_name}](https://images.nasa.gov/docs/images.nasa.gov_api_docs.pdf)

Most HTTP libraries ([Python's Here](https://docs.python.org/3/library/http.client.html))take care of this for you (glance to make sure):

* At least one param is required, all are optional
* All parameter values must be URL­encoded

#### Making curl requests

Use --data-urlencode to encode values using curl:
```sh
   curl -G https://images-api.nasa.gov/search
       --data-urlencode "q=apollo 11"
       --data-urlencode "description=moon landing"
       --data-urlencode "media_type=image" |
       python -m json.tool
```

Will often look more like the equivalent pre­encoded request:

```sh
curl "https://images-api.nasa.gov/search
       ?q=apollo%2011
       &description=moon%20landing
       &media_type=image" |
       python -m json.tool
```

The response is with a [Collection+JSON](https://github.com/collection-json/spec) Document that is returned, which contains one or more item objects in an array. The response may describe all, or only a partial list, of the items in a collection. We get back a HTTP header, and then the collection (this case in JSON format).

### Handling Errors
 
Code | Explanation
|---|---|
200 - OK | Everything worked as expected.
400 ­- Bad Request | The request was unacceptable, often due to missing a required parameter.
404 ­- Not Found | The requested resource doesn’t exist.
500, 502, 503, 504 ­- Server Errors | Something went wrong on the API’s (NASA's) end.

Write code for all HTTP error responses above. These may occur for many reasons, such as a failed search query, invalid parameters, a query for a non­ existent media asset, and network unavailability.

# Move on to the wxPython application to use this API
From the realization that our application will interface the NASA's API, and that we may not want to reinvent wheels that are already out there, we can design more effective pieces quicker using wrappers.

## Check Python for any API wrapper

See if Python has an already written package for a wrapper to their (NASA's) API. This means we write to Pythons interface module instead of creating our own to interface directly to NASA's site.

* Nasa site has rate limiting (1000 per hour) in place for those without the API key, so we can still perform GETs without the key- but we already got one (see the sign-up notes)

## The Docs aren't so clear

* The API documentation disagrees with NASA’s Image API documentation about which endpoints to hit.

API documentation states to use this URL:

https://api.nasa.gov/planetary/apod?api_key=API_KEY_GOES_HERE
But in the Image API documentation, the API root is:

https://images-api.nasa.gov
We will be using the latter.
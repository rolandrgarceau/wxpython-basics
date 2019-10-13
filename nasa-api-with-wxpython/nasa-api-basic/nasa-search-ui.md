# UI Basics
 
## Features:

* Search bar
* widget to hold search results
  * watch the "sub-zero" from api_req.py. It is dealing only with one item- the first of many
* Display mechanism when the result is chosen
  * this will affect how we make use of the sub-zero, sub-one, sub-two, as loop or individually (in a minute)

## Fields we may need

* Title
* Thumbnail URL
* Location of image
* NASA’s internal ID
* Description of the photo
* The photographer’s name
* The date the image was created


## Deal with layout after you get funding
Series of nested sizers will put them in there for you, but that learning curve was a little hecktick- see the wxpython note basics for their descriptions on nesting. Some immediate considerations is what happens when your initial application size is overfilled with too many onjects added to the sizer? Specifically if we are from a HTML/CSS/JS background- how do we address a scrollable window, or can we add in an auto-resize of the entire app? Resize may look like shrinking the widgets added to the sizer to fit, or even growing the "size" of the application to handle the overloaded sizer. I tested this out just because it was a problem I have seen before in other frameworks and how to deal with these design considerations quickly (are you on a sprint with deadline too?) often result in SEO per keyphrase lookup. 

## NASA specific imports and classes 

* imports from `urllib.parse` may be used for encoding URL parameters.
* `DownloadDialog` is a class for a small dialog that you will be creating for downloading NASA images.

## Result class and ObjectListView

We need a class to represent the objects in that widget. The Result class is what we use to hold data that makes up each row in your ObjectListView. The item parameter is a portion of JSON that is receiving from NASA as a response to our query. In this class, we need to parse out the information required.

## Main Panel

The MainPanel is where the majority of the code lies. Housekeeping creates a search_results here to hold a list of `Result` objects when the user does a search. We also can set the max_size of the thumbnail image, the font to be used, the sizer and we get selective `StandardPaths` as well.

wx.SearchCtrl is like a wx.TextCtrl but has special buttons built into it. We can bind the search button’s click event (EVT_SEARCHCTRL_SEARCH_BTN) and EVT_TEXT_ENTER to a search related event handler (on_search).

Then we add the search results widget with the ObjectListView. We customize the empty message by calling SetEmptyListMsg() and also bind the widget to EVT_LIST_ITEM_SELECTED so that we do something when the user selects a search result.

also add a download button to allow the user to select which image size they would like to download- this is the first on_download event handler in which we get the user’s selection.

If the user hasn’t selected anything, then this method exits. On the other hand, if the user has selected an item, then you instantiate the DownloadDialog and show it to the user to allow them to download something.

Then the next event handler on_search will get the string that the user has entered into the search control or return an empty string. Assuming that the user actually enters something to search for, you use NASA’s general search query, q and hard code the media_type to image. Then you encode the query into a properly formatted URL and use requests.get() to request a JSON response.

Next you attempt to loop over the results of the search. Note that is no data is returned, this code will fail and cause an exception to be thrown. But if you do get data, then you will need to parse it to get the bits and pieces you need.

You will skip items that don’t have the title field set. Otherwise you will create a Result object and add it to the search_results list. At the end of the method, you tell your UI to update the search results.

Before we get to that function, you will need to create on_selection(). With this method you get the selected item, but this time you take that selection and update the title text control with the selection’s title text. Then you check to see if there is a thumbnail and update that accordingly if there is one. When there is no thumbnail, you set it back to an empty image as you do not want it to keep showing a previously selected image.

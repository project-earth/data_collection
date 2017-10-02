# Landsat Search, Download, and Preprocessing
The following library provides to for conducting search and downloading of NASA Landsat 8 data via the AWS api as well as the tools needed to properly process the `tar.gz` raw data into a easily workable format. Substantial code is sourced from the [landsat-util](https://github.com/developmentseed/landsat-util) library by Scisco, Marc Farra, Drew Bollinger, Sean Gillies, and Alex Kappel.



## The Search Library
The Search library defines the `Search` class and pertinant functions.


### Classes
- `class Search()`

	##### Objects
	- `Search.api_url`

	##### Methods
	- `Search.search(paths_rows=None, lat=None, lon=None, address=None, end_date=None, cloud_min=None, cloud_max=None, limit=1)` - takes a collection of search parameters and returns a dictionary object contiaining corresponding search results.
		- `paths_rows=None` is a string in the format: `'003,003,004,004'` which gives a landsat path/row reference.
		- `lat=None` is a string, float, or integer denoting a latitude.
		- `lon=None` is a string, float, or integer denoting a longitude.
		- `address=None` is a string denoting an address.
		- `start_date=None` is a date string in format YYY-MM-DD denoting a start date.
		- `end_date=None`  is a date string in format YYY-MM-DD denoting an end date.
		- `cloud_min` is a float denoting the minimal cloud coverage.
		- `cloud_max` is a float denoting the maximal cloud coverage.
		- `limit` is an integer which gives the maximum number of search results returned.

		`Search.search` is the main front facing function of the `Search` class. The function returns a dictionary with the requested search results like the following:

			{
				'status': u'SUCCESS',
				'total_returned': 1,
				'total': 1,
				'limit': 1
				'results': [
					{
							'sat_type': u'L8',
							'sceneID': u'LC80030032014142LGN00',
							'date': u'2014-05-22',
							'path': u'003',
							'thumbnail': u'http://....../landsat_8/2014/003/003/LC80030032014142LGN00.jpg',
							'cloud': 33.36,
							'row': u'003
					}
				]
			}
	- **_Other methods are used internally only_**



## The Download Library
The Download library defines the `Download` class and pertinant functions.


### Classes
- `class Download()`
	
	##### Objects
	- `Download.status` - gives a handle for download object status. This can take either be the string `'IDLE'` if no downloads are currently active or this can be a `DownloadStatus` object.
	- `Download.google`
	- `Download.s3`
		
	##### Methods
	- `Download.download(scene, status=None)` - takes a landsat scene id string and downloads the file to the appropriate data directory given by `DATA_DIR` in `.../src/settings.py`.
		- `scene` is a string denoting a scene ID to download
		- `status` allows us to pass a `DownloadStatus` object to keep track of the status of the download. If one is not passed in, then one will be created. This object can be accessed through `Download.status` regardless of whether it was passed in or created.

		The function attempts to download the file requested using either the aws or google s3 landsat service (currently only aws is implemented). If it is successful, the function returns a tuple consisting of the scene id paired with the source they were downloaded from (`'amazon'` or `'google'`). In the event of a failure, the function will raise an exception without handling it.
	- **_Other methods are used internally only_**



## Bugs
- SQL server object closes after 8 hours

## Todo
- Expand preprocessing options
- Manual insertion through remote connection
- More window flexible interface
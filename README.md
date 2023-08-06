# savepagenow_client

This is work in progress Python wrapper for archive.org’s Save Page Now API.

The is deeply inspired by [palewire/savepagenow](https://github.com/palewire/savepagenow) library. The [palewire/savepagenow](https://github.com/palewire/savepagenow) library only calls the save endpoint. If you want to access status, outlinks, and first_archive, you need to call the status endpoint as well.

This will increase the complexity of the library, as we will need to wait until the request is processed.

I am currently dogfooding the API, and it not currently stable. If you don't need these attributes, you should use the [palewire/savepagenow](https://github.com/palewire/savepagenow) library.

Read More
- [Save Page Now 2 Public API Docs Draft](https://docs.google.com/document/d/1Nsv52MvSjbLb2PCpHlat0gkzw0EvtSgpKHu4mk0MnrA/edit#heading=h.1gmodju1d6p0)
- [Save Page Now 2 Change Log](https://docs.google.com/document/d/19RJsRncGUw2qHqGGg9lqYZYf7KKXMDL1Mro5o1Qw6QI/edit)
- [ias3 Internet archive S3-like API](https://archive.org/developers/ias3.html)
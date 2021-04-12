# 2021_Election_Data

1. candidate_item.py - This is the main python code to scrap the data from https://affidavit.eci.gov.in/. without any file download.

2. full_candidate.py - This is also the main python code to scrap the data from https://affidavit.eci.gov.in/, here file download code is integrated. So the affidavit of the candidate will be downloaded as per the settings in settings.py. 

The main issue in this file is that the name of the file is SHA1 of the URL. I want to rename the file while downloading.

More information about the downloading code.
1. doc_spider.py code specifically download the file, it does not scrap contain any other data.


Now, as in the browser, once you click on a candidate it takes you to their profile page and I wanted to download affidavit file from that page. 

After inspecting this candidate page (https://affidavit.eci.gov.in/show-profile/MTY5MDY=/MTY=/MTA=/Mw==/QUM=), I figured out that once you click on download button, a GET request is sent to download the file. The name of the file is in the hidden field as shown here.

	<div class="aside-af">
	       <h4 class="pull-left">Affidavit</h4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
				   <input type="hidden" value="aHR0cHM6Ly9zdXZpZGhhLmVjaS5nb3YuaW4vdXBsb2FkczEvYWNhZmZpZGF2aXQvRTEwLzIwMjEvQUMvUzI1LzE2MC9TMjVfMTY5MDZfMTEzMzlfMjAyMTA0MDcwODEyMTYxNjE3ODA2NTM2LnBkZg==" id="pdfUrl" name="pdfUrl">
		  <a href="javascript:void(0);" id="vvvvvvv"><button type="button" onclick="return increaseDownloadCount();" class="btn orng pull-right">Download <i class="fa fa-download"></i></button></a>                     <div class="clearfix"></div>
		    <div class="info">
			  <p><span><strong>Download Count</strong></span> <span id="updateCount">71</span></p> 
			  <p><span><strong>Affidavit Uploaded : </strong></span> <span>7th April, 2021   </span></p>                   
			</div>
		    </div>


The URL in GET request as per the Javascript file is 
https://affidavit.eci.gov.in/affidavit-pdf-download/aHR0cHM6Ly9zdXZpZGhhLmVjaS5nb3YuaW4vdXBsb2FkczEvYWNhZmZpZGF2aXQvRTEwLzIwMjEvQUMvUzI1LzE2MC9TMjVfMTY5MDZfMTEzMzlfMjAyMTA0MDcwODEyMTYxNjE3ODA2NTM2LnBkZg=='

So to test it out, I wrote a python code to download this file directly.
The python code is in doc_spider.py


As per the this document (https://docs.scrapy.org/en/latest/topics/media-pipeline.html). I used the default FilesPipeline code as you can see in the settings.py (default = 'scrapy.pipelines.files.FilesPipeline'). If I use this, then the file is downloaded but as per source code (https://docs.scrapy.org/en/latest/_modules/scrapy/pipelines/files.html?highlight=scrapy.pipelines.files#) the file name is SHA1 of the URL. 

Now, as given in the document (https://docs.scrapy.org/en/latest/topics/media-pipeline.html#module-scrapy.pipelines.files) I extended the pipeline code in pipelines.py. It is a very basic test code. Once I ran the crawl, this code is not triggered and nothing happens.

I want your help in this part. Thank You :) 




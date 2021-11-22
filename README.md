# WebScraper-GoogleImageDownloader

This is a program I created with 2 objectives in mind
  1. To start learning how to use Selenium
  2. Create a tool to facilitate easy collection of datasets for the future when I start exploring Machine Learning

I think the code is quite readable and it does...what it says, however let me quickly state that:
  - The program can be run either in PyCharm or other python interpreters, in which case it will search google images for exactly the string contained in the variable "downloaded_image_type", and will atempt to download the number of pictures dictated by the value of "amount_downloaded"
  
  - Or the program can be run from the command line as such : <<python WebScraper.py "pictures of dogs" 5>>, in which case, the value of the aformentioned "downloaded_image_type" will be overwritten by, in this case, "pictures of dogs", and the program will atempt to download 5 results of this from google images.
    - make sure to contain the string in quotes. If you run, for example, the command <<python WebScraper.py pictures of dogs 12>> expecting to download 12 pictures of dogs, what you will instead download is only 5 image results of "pictures". The program will atempt to get the count as the 2nd input, but, since a TypeError will occur when trying to do int("of"), the program will handle this error and will instead leave the amount of downloaded images at the default value of 5.


Images are saved as .jpeg files.
If there already exists a folder with the name given by the variable "downlaoded_image_type" the program will error out

**TODO: ^handle this^**

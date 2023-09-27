# How to set up a new domain online
The goal of this doc is to explain how to deploy a static website to the internet to be accessed via HTTPS at a purchased domain name.
## Assumptions
 - Domain name purchased from [GoDaddy](https://www.godaddy.com/)
 - Site served via AWS (S3, Cloudfront, Route53)
## Steps
1. Purchase domain name from GoDaddy. They make this pretty straightforward.
   1. For the rest of this tutorial I'm going to assume our domain is example.com
   2. It's not hard to find a domain for less than $5
2. Go into AWS S3 bucket and follow [this tutorial](https://www.youtube.com/watch?v=fm6FPQMZ_WI). The UI has changed, but the video is still accurate. Don't do the Route53 stuff yet, that comes later and will be *slightly* different because we are using Cloudfront
   1. I call my S3 bucket by the name of the domain (i.e. example.com)
   2. S3 buckets are for general cloud storage, not just websites.
3. Go to AWS Certificate Manager
   1.  Click the **Request** button (at the time of writing it's 🟠)
   2.  Select **Request a public certificate** and hit **Next**
   3.  Fill out the form (you'll notice we keep pretty much all of the defaults)
       1.  Enter the domain name *example.com*
       2.  Select **DNS validation** which just so happens to not only be recommended by me but by Jeff (Mr. Bezos, his friends call him Jeff 😎)
       3.  Select **RSA 2048**
       4.  Don't add any tags
   4.  Hit **Request**
   5.  Click on the certificate you just made. We need to find the CNAME.
       1.  Scroll till you see the section **Domains**. You'll notice we're not approved yet. Copy the CNAME name and the CNAME value and store them somewhere (like in a txt file, or just keep this tab open) These values and the NS Records are what we need to put into GoDaddy later
4.  Go to GoDaddy
    1.  Click the profile icon (looks like an outlined 👨🏾‍⚕️) and then click **My Products**
    2.  Select **example.com**
    3.  Select **Domain**
    4.  Select **Manage DNS**
    5.  Select **Nameservers**
    6.  DNS Records and change the **CNAME name** and the **CNAME value** to what you had from the certificate. <!--This step is one I haven't verified. I did it yesterday though-->
        1.  You want to do this *before* setting up Route53 because you *can't* change the CNAME when you've started using other nameservers. Then you have to validate by Email, which idk how to do yet (I'm sure using this loophole will bite me later 😆). 
    7.  Go back to the AWS Certificate Manager and ensure the certificate is granted. You NEED this to happen before moving on <!--This is again something I didn't test while writing this guide, but I did it yesterday too-->
5.  Create a Cloudfront distribution (this is necessary to be listed as secure in the browser (using HTTPS))
    1.  Click **Create distribution** (also in 🟠)
    2.  Click **Use website endpoint** in the popup
    3.  Keep all the settings the same except the following
        1.  Under **Viewer protocol policy** select **Redirect HTTP to HTTPS**
        2.  Select the **Custom SSL certificate** you just made
        3.  Hit **Add item** to alternate domain name and enter **example.com**
            1.  This won't work until the **Custom SSL certificate** is selected
    4.  Click **Create distribution**
6.  Go to AWS Route 53
    1.  Click on **Hosted zones**
    2.  Click **Create new hosted zone**
    3.  Enter the **Domain Name**
    4.  Click **Create new hosted zone**
    5.  Click on the Hosted zone (**example.com**)
    6.  Click **Create Record**
    7.  Select **Record type** **A Record** (this should be the default selection)
    8.  Click the **Alias** slider to say you're Aliasing something else in AWS (It'll be the cloudfront dist)
    9.  Under **Route Traffic Too**
        1.  For **Choose Endpoint** select **Alias to Cloudfront Distribution**
        2.  **Choose Region** will have a default. Cloudfront distributions are international, so they all have the same region.
        3.  for **Choose Distribution** select the distribution you made
    10. Click **Create Records**
    11. You should now have 3 records in AWS all with name **example.com**, but each with different types: A, NS, and SOA.
    12. Copy the urls under **Value/Route traffic to** for the NS record. These will be put in GoDaddy. Let *n* be the number of URLS you copied.

Almost done don't worry. One more step

7.  Go back to the GoDaddy DNS area as described in Step 4 above
    1.  Click **Nameservers**
    2.  Click **Change Nameservers**
    3.  Select **I'll use my own nameservers**
    4.  Add nameservers until you have *4* (you should have started with two)
    5.  Replace the text of the nameservers with the strings you got in step 6.12. Delete the period after each of the URLS (i.e. change **randomstring.co.uk.** to **randomstring.co.uk**).
8. All done! Go to your domain and see if this tutorial works. If it didn't and you figure out why, open a pull request and fix it 😁





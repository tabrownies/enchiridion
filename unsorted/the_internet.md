<div id="kl_wrapper_3" class="kl_flat_sections kl_wrapper">
<div id="kl_banner" class="" style="background-color: #ffffff; color: #000000; margin-bottom: 0px; padding-bottom: 0px;">
<h2 class="" style="background-color: #a2c7b0; color: #000000; border-width: 5px 0px; border-style: solid; border-color: #ffffff; margin-top: -15px; margin-bottom: 0px;">
<span id="kl_banner_left" class="" style="background-color: #a2c7b0; color: #000000; border: 5px solid #ffffff;"><span class="kl_mod_text" style="color: #000000; background-color: #a2c7b0; margin-top: -2px;">Unit 1</span></span><span id="kl_banner_right" class="" style="margin-bottom: 0px; margin-top: 0px; background-color: #a2c7b0; color: #000000;">The Internet&nbsp;</span>
</h2>
</div>
<div id="kl_custom_block_0" class="">
<h3 style="text-align: center;">History and Overview</h3>
<p>The Internet is a communications network that spans billions of devices. It started as a project funded by the U.S. defense department and was originally known as the ARPANET. This is what it looked like in 1969:</p>
<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://byu.instructure.com/courses/7682/files/1965959/download?wrap=1" alt="december-1969.jpg" data-api-endpoint="https://byu.instructure.com/api/v1/courses/7682/files/1965959" data-api-returntype="File"></p>
<p>and this is what it looked like in 1977:</p>
<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://byu.instructure.com/courses/7682/files/1965960/download?wrap=1" alt="july-1977.jpg" data-api-endpoint="https://byu.instructure.com/api/v1/courses/7682/files/1965960" data-api-returntype="File"><br>It's nearly impossible to visualize what the Internet looks like today, but here is a good try:</p>
<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://byu.instructure.com/courses/7682/files/1965943/download?wrap=1" alt="opte.png" data-api-endpoint="https://byu.instructure.com/api/v1/courses/7682/files/1965943" data-api-returntype="File"></p>
<p>There are billions of devices connected to the Internet. These include consumer devices, such as computers, smartphones, tablets, and smart home devices (speakers, thermostats, refrigerators). The Internet also includes a lot of infrastructure needed for these devices to communicate, including routers, switches, and cell phone towers.</p>
<p>Since its early development as a U.S. government project, the Internet has since been both internationalized and commercialized, so that different parts of the network are owned by different companies and reside in different countries. Some countries (such as China) have nationalized infrastructure, whereas many others rely on the private sector to operate the network.</p>
<p>A single company can run its own global network. For example, here is what Level 3's network looked like recently:</p>
<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://byu.instructure.com/courses/7682/files/1965954/download?wrap=1" alt="level3.png" data-api-endpoint="https://byu.instructure.com/api/v1/courses/7682/files/1965954" data-api-returntype="File"></p>
<p>The Internet contains many of these networks, all interconnected to each other.&nbsp;</p>
<p>Another fascinating part of the Internet is that there are many cables running oceans and seas that connect parts of the network. Here is a map of some undersea cables:</p>
<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://byu.instructure.com/courses/7682/files/1965956/download?wrap=1" alt="submarine-cable-map-2012.jpg" data-api-endpoint="https://byu.instructure.com/api/v1/courses/7682/files/1965956" data-api-returntype="File"></p>
</div>
<div id="kl_custom_block_1" class="">
<h3 style="text-align: center;">How the Internet Works, Briefly</h3>
<p>Most applications on the Internet use client-server communication. As shown below, a client connects to a server, sends one or more requests to the server, and receives responses for each request. Examples of this kind of communication include a web browser connecting to a web server (e.g. amazon.com), the Twitter app connecting to the Twitter service, an instant messaging application connecting to the instant messaging server, and so on.</p>
<p>&nbsp;<img style="display: block; margin-left: auto; margin-right: auto;" src="https://byu.instructure.com/courses/7682/files/1965947/download?wrap=1" alt="internet-connection-1.png" width="671" height="209" data-api-endpoint="https://byu.instructure.com/api/v1/courses/7682/files/1965947" data-api-returntype="File"></p>
</div>
<div id="kl_custom_block_2" class="">
<h3 style="text-align: center;">DNS</h3>
<p>The first step for a client usually involves figuring out what server to connect to. Out of all the billions of devices on the Internet, the client needs to specify&nbsp;<em>which</em>&nbsp;other device it wants to connect to and which service it wants to use when connecting to that server (e.g. web, email, or some other application).</p>
<p>To do this, clients use the Domain Name Service (DNS). The client specifies the&nbsp;<em>name</em>&nbsp;of the server it wants to connect to (e.g. amazon.com), and asks DNS to return the&nbsp;<em>IP address</em>&nbsp;of this server (e.g.&nbsp;176.32.98.166).&nbsp;</p>
</div>
<div id="kl_custom_block_3" class="">
<h3 style="text-align: center;">TCP</h3>
<p>The next step for a client is to use the Transmission Control Protocol (TCP) to make a connection to the server. To do this, the client specifies the IP address it learned from DNS, plus the&nbsp;<em>port&nbsp;</em>number of the service it wants to connect to.&nbsp;For example, the&nbsp;port number for a web server is 80 (HTTP) or 443 (HTTPS), for email it is 25 or 465 or various other ports, and for SSH it is 22.</p>
<p>Once TCP makes a connection between the client and the server, the client can send requests to the server ("send this web page", "retrieve this email message"), and the server can send responses. The format of these messages depends on the application<em><strong>&nbsp;</strong></em>being used. TCP ensures that the connection between the client is&nbsp;<em>reliable---</em>any message the client sends is received by the server and&nbsp;vice versa. The only reason messages will not go through is if the network is not working. TCP does&nbsp;<em>not</em>&nbsp;guarantee anything about performance. The messages exchanged by the client and server will be delivered, but they might be delivered slowly or quickly, depending on a variety of factors.</p>
</div>
<div id="kl_custom_block_4" class="">
<h3 style="text-align: center;">Routing and IP</h3>
<p>Whenever TCP sends a message from a client to a server, it divides the message into a series of packets and sends each one individually. Each packet must find a way across the Internet from the client to the server. As shown below, the connection between the client and server traverses a particular&nbsp;<em>path&nbsp;</em>through the Internet. This path consists of a series of routers that are determined by a collection of routing protocols.&nbsp;</p>
<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://byu.instructure.com/courses/7682/files/1965957/download?wrap=1" alt="internet-internals.png" data-api-endpoint="https://byu.instructure.com/api/v1/courses/7682/files/1965957" data-api-returntype="File"></p>
<p>At each step in this path, the packet is sent to the next hop using the Internet Protocol (IP). At each hop, IP sends packets as fast as it can. If a router receives packets faster than it can send them, packets can be delayed (because they have to wait in a buffer before being sent to the next router) or dropped (because the buffer is full). The effects of delay and dropping are often called&nbsp;<em>congestion</em>. TCP will re-send any packets that are dropped, but it will also slow down when loss occurs.</p>
</div>
<div id="kl_custom_block_5" class="">
<h3 style="text-align: center;">Layers and Standards</h3>
<p>TCP and IP are the primary&nbsp;<em>protocols</em>&nbsp;used to send data across the Internet, although there are many more. The protocols that are used are often arranged in&nbsp;<em>layers</em>,&nbsp;from top to bottom, as shown below. The application layer is at the top (e.g. HTTP for a web browser), followed by the transport layer (e.g. TCP), the network layer (e.g. IP), and the link and physical layers (e.g. WiFi or Ethernet).</p>
<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://byu.instructure.com/courses/7682/files/1965941/download?wrap=1" alt="internet-architecture.png" width="182" height="218" data-api-endpoint="https://byu.instructure.com/api/v1/courses/7682/files/1965941" data-api-returntype="File"></p>
<p>These protocols are standardized by a variety of organizations:</p>
<ul>
<li>W3C: standardizes web protocols, such as HTML and CSS.</li>
<li>IETF: standardizes Internet protocols, such as HTTP, TCP, and IP.</li>
<li>IEEE: standardizes link protocols, such as WiFi and Ethernet.</li>
</ul>
<p>It's important to standardize protocols so that all the different devices on the Internet can interoperate. The alternative is to use proprietary protocols, which then only work with devices&nbsp;or software from one or several manufacturers.</p>
</div>
<div id="kl_custom_block_6" class="">
<h3 style="text-align: center;">Learn More</h3>
<p>If you want to learn more about how the Internet works,&nbsp;<a class="external" href="https://www.amazon.com/Computer-Networking-Top-Down-Approach-7th/dp/0133594149" target="_blank"><em>Computer Networking: A Top-Down Approach (7th Edition)</em><span class="screenreader-only">&nbsp;(Links to an external site.)</span><span class="ui-icon ui-icon-extlink ui-icon-inline" title="Links to an external site."><span class="screenreader-only">Links to an external site.</span></span></a>, by Kurose and Ross, is an excellent networking textbook. This is the book currently used for CS 460.</p>
</div>
</div>
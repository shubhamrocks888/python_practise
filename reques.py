import requests
#
# # r= requests.get('https://xkcd.com/')
# # print (r)
# # o/p is      --->        <Response [200]>

# r= requests.get( )
# print (r.text)        ----> response in unicode format i.e, in string format
# # o/p is:

# <!DOCTYPE html>
# <html>
# <head>
# <link rel="stylesheet" type="text/css" href="/s/b0dcca.css" title="Default"/>
# <title>xkcd: Phylogenetic Tree</title>
# <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
# <link rel="shortcut icon" href="/s/919f27.ico" type="image/x-icon"/>
# <link rel="icon" href="/s/919f27.ico" type="image/x-icon"/>
# <link rel="alternate" type="application/atom+xml" title="Atom 1.0" href="/atom.xml"/>
# <link rel="alternate" type="application/rss+xml" title="RSS 2.0" href="/rss.xml"/>
# <script type="text/javascript" src="/s/b66ed7.js" async></script>
# <script type="text/javascript" src="/s/1b9456.js" async></script>
#
# <meta property="og:site_name" content="xkcd">
#
# <meta property="og:title" content="Phylogenetic Tree">
# <meta property="og:url" content="https://xkcd.com/2269/">
# <meta property="og:image" content="https://imgs.xkcd.com/comics/phylogenetic_tree_2x.png">
# <meta name="twitter:card" content="summary_large_image">
#
# </head>
# <body>
# <div id="topContainer">
# <div id="topLeft">
# <ul>
# <li><a href="/archive">Archive</a></li>
# <li><a href="http://what-if.xkcd.com">What If?</a></li>
# <li><a href="http://blag.xkcd.com">Blag</a></li>
# <li><a href="/how-to/">How To</a></li>
# <li><a href="http://store.xkcd.com/">Store</a></li>
# <li><a rel="author" href="/about">About</a></li>
# <li><a href="/atom.xml">Feed</a> &bull; <a href="/newsletter/">Email</a></li>
# </ul>
# </div>
# <div id="topRight">
# <div id="masthead">
# <span><a href="/"><img src="/s/0b7742.png" alt="xkcd.com logo" height="83" width="185"/></a></span>
# <span id="slogan">A webcomic of romance,<br/> sarcasm, math, and language.</span>
# </div>
# <div id="news">
# <div id="htNews">
# <a href="https://xkcd.com/how-to/"><img border=0 src="//imgs.xkcd.com/static/howto_release_49b1.png"></a><br />
# You can get it here:<br />
# <a href="https://www.amazon.com/How-Absurd-Scientific-Real-World-Problems/dp/0525537090/">Amazon</a>,
#     <a href="http://links.penguinrandomhouse.com/type/affiliate/isbn/9780525537090/siteID/8001/retailerid/2/trackingcode/PRH5522E62429">B&N</a>,
#     <a href="http://links.penguinrandomhouse.com/type/affiliate/isbn/9780525537090/siteID/8001/retailerid/6/trackingcode/penguinrandom">IndieBound</a>,
#     <a href="https://itunes.apple.com/us/book/how-to/id1451461524?mt=11">Apple</a>,
#     <a href="https://www.audible.com/search?advsearchKeywords=How+To+Randall+Munroe&source_code=COMA0213WS031709&SID=PRHA9A5E24CFB--9780525635680">Audible</a>,
#     <a href="http://links.penguinrandomhouse.com/type/affiliate/isbn/9780525537090/siteID/8001/retailerid/23/trackingcode/PRH3D17167A3B">Target</a>
# </div>
# <script>
# var client = new XMLHttpRequest();
# client.open("GET", "//c.xkcd.com/how-to/news", true);
# client.send();
# client.onreadystatechange = function() {
#   if(client.readyState == 4 && client.status == 200) {
#     document.getElementById("htNews").innerHTML = client.responseText;
#   }
# }
# </script>
#
# </div>
# </div>
# <div id="bgLeft" class="bg box"></div>
# <div id="bgRight" class="bg box"></div>
# </div>
# <div id="middleContainer" class="box">
#
# <div id="ctitle">Phylogenetic Tree</div>
# <ul class="comicNav">
# <li><a href="/1/">|&lt;</a></li>
# <li><a rel="prev" href="/2268/" accesskey="p">&lt; Prev</a></li>
# <li><a href="//c.xkcd.com/random/comic/">Random</a></li>
# <li><a rel="next" href="#" accesskey="n">Next &gt;</a></li>
# <li><a href="/">&gt;|</a></li>
# </ul>
# <div id="comic">
# <img src="//imgs.xkcd.com/comics/phylogenetic_tree.png" title="And I was kicked out of my March Madness pool because I wouldn&#39;t shut up about the evidence for NBA/ABA endosymbiosis." alt="Phylogenetic Tree" srcset="//imgs.xkcd.com/comics/phylogenetic_tree_2x.png 2x"/>
# </div>
# <ul class="comicNav">
# <li><a href="/1/">|&lt;</a></li>
# <li><a rel="prev" href="/2268/" accesskey="p">&lt; Prev</a></li>
# <li><a href="//c.xkcd.com/random/comic/">Random</a></li>
# <li><a rel="next" href="#" accesskey="n">Next &gt;</a></li>
# <li><a href="/">&gt;|</a></li>
# </ul>
# <br />
# Permanent link to this comic: https://xkcd.com/2269/<br />
# Image URL (for hotlinking/embedding): https://imgs.xkcd.com/comics/phylogenetic_tree.png
# <div id="transcript" style="display: none"></div>
# </div>
# <div id="bottom" class="box">
# <img src="//imgs.xkcd.com/s/a899e84.jpg" width="520" height="100" alt="Selected Comics" usemap="#comicmap"/>
# <map id="comicmap" name="comicmap">
# <area shape="rect" coords="0,0,100,100" href="/150/" alt="Grownups"/>
# <area shape="rect" coords="104,0,204,100" href="/730/" alt="Circuit Diagram"/>
# <area shape="rect" coords="208,0,308,100" href="/162/" alt="Angular Momentum"/>
# <area shape="rect" coords="312,0,412,100" href="/688/" alt="Self-Description"/>
# <area shape="rect" coords="416,0,520,100" href="/556/" alt="Alternative Energy Revolution"/>
# </map>
# <br />
# <a href="//xkcd.com/1732/"><img border=0 src="//imgs.xkcd.com/s/temperature.png" width="520" height="100" alt="Earth temperature timeline"></a>
# <br />
# <div>
# <!--
# Search comic titles and transcripts:
# <script type="text/javascript" src="//www.google.com/jsapi"></script>
# <script type="text/javascript">google.load('search', '1');google.setOnLoadCallback(function() {google.search.CustomSearchControl.attachAutoCompletion('012652707207066138651:zudjtuwe28q',document.getElementById('q'),'cse-search-box');});</script>
# <form action="//www.google.com/cse" id="cse-search-box">
# <div>
# <input type="hidden" name="cx" value="012652707207066138651:zudjtuwe28q"/>
# <input type="hidden" name="ie" value="UTF-8"/>
# <input type="text" name="q" id="q" size="31"/>
# <input type="submit" name="sa" value="Search"/>
# </div>
# </form>
# <script type="text/javascript" src="//www.google.com/cse/brand?form=cse-search-box&amp;lang=en"></script>
# -->
# <a href="/rss.xml">RSS Feed</a> - <a href="/atom.xml">Atom Feed</a> - <a href="/newsletter/">Email</a>
# </div>
# <br />
# <div id="comicLinks">
# Comics I enjoy:<br/>
#         <a href="http://threewordphrase.com/">Three Word Phrase</a>,
#         <a href="http://www.smbc-comics.com/">SMBC</a>,
#         <a href="http://www.qwantz.com">Dinosaur Comics</a>,
#         <a href="http://oglaf.com/">Oglaf</a> (nsfw),
#         <a href="http://www.asofterworld.com">A Softer World</a>,
#         <a href="http://buttersafe.com/">Buttersafe</a>,
#         <a href="http://pbfcomics.com/">Perry Bible Fellowship</a>,
#         <a href="http://questionablecontent.net/">Questionable Content</a>,
#         <a href="http://www.buttercupfestival.com/">Buttercup Festival</a>,
#         <a href="http://www.mspaintadventures.com/?s=6&p=001901">Homestuck</a>,
# 	<a href="http://www.jspowerhour.com/">Junior Scientist Power Hour</a>
# </div>
# <br />
# <div id="comicLinks">
# Other things:<br/>
#         <a href="https://medium.com/civic-tech-thoughts-from-joshdata/so-you-want-to-reform-democracy-7f3b1ef10597">Tips on technology and government</a>,<br />
#         <a href="https://www.nytimes.com/interactive/2017/climate/what-is-climate-change.html">Climate FAQ</a>,
# 	<a href="https://twitter.com/KHayhoe">Katharine Hayhoe</a>
# </div>
# <br />
# <center>
# <div id="footnote" style="width:70%">xkcd.com is best viewed with Netscape Navigator 4.0 or below on a Pentium 3&plusmn;1 emulated in Javascript on an Apple IIGS<br />at a screen resolution of 1024x1. Please enable your ad blockers, disable high-heat drying, and remove your device<br />from Airplane Mode and set it to Boat Mode. For security reasons, please leave caps lock on while browsing.</div>
# </center>
# <div id="licenseText">
# <p>
# This work is licensed under a
# <a href="http://creativecommons.org/licenses/by-nc/2.5/">Creative Commons Attribution-NonCommercial 2.5 License</a>.
# </p><p>
# This means you're free to copy and share these comics (but not to sell them). <a rel="license" href="/license.html">More details</a>.</p>
# </div>
# </div>
# </body>
# <!-- Layout by Ian Clasbey, davean, and chromakode -->
# </html>

# r= requests.get('https://xkcd.com/')
# print (r.request)               --->    <PreparedRequest [GET]>
# print (r.ok)                        --->        True
# print(r.content)            --->response in  bytes
# o/p is --->  b'<!DOCTYPE html>\n<html>\n<head>\n<link rel="stylesheet" type="text/css" href="/s/b0dcca.css" title="Default"/>\n<title>xkcd: Phylogenetic Tree</title>\n<meta http-equiv="X-UA-Compatible" content="IE=edge"/>\n<link rel="shortcut icon" href="/s/919f27.ico" type="image/x-icon"/>\n<link rel="icon" href="/s/919f27.ico" type="image/x-icon"/>\n<link rel="alternate" type="application/atom+xml" title="Atom 1.0" href="/atom.xml"/>\n<link rel="alternate" type="application/rss+xml" title="RSS 2.0" href="/rss.xml"/>\n<script type="text/javascript" src="/s/b66ed7.js" async></script>\n<script type="text/javascript" src="/s/1b9456.js" async></script>\n\n<meta property="og:site_name" content="xkcd">\n\n<meta property="og:title" content="Phylogenetic Tree">\n<meta property="og:url" content="https://xkcd.com/2269/">\n<meta property="og:image" content="https://imgs.xkcd.com/comics/phylogenetic_tree_2x.png">\n<meta name="twitter:card" content="summary_large_image">\n\n</head>\n<body>\n<div id="topContainer">\n<div id="topLeft">\n<ul>\n<li><a href="/archive">Archive</a></li>\n<li><a href="http://what-if.xkcd.com">What If?</a></li>\n<li><a href="http://blag.xkcd.com">Blag</a></li>\n<li><a href="/how-to/">How To</a></li>\n<li><a href="http://store.xkcd.com/">Store</a></li>\n<li><a rel="author" href="/about">About</a></li>\n<li><a href="/atom.xml">Feed</a> &bull; <a href="/newsletter/">Email</a></li>\n</ul>\n</div>\n<div id="topRight">\n<div id="masthead">\n<span><a href="/"><img src="/s/0b7742.png" alt="xkcd.com logo" height="83" width="185"/></a></span>\n<span id="slogan">A webcomic of romance,<br/> sarcasm, math, and language.</span>\n</div>\n<div id="news">\n<div id="htNews">\n<a href="https://xkcd.com/how-to/"><img border=0 src="//imgs.xkcd.com/static/howto_release_49b1.png"></a><br />\nYou can get it here:<br />\n<a href="https://www.amazon.com/How-Absurd-Scientific-Real-World-Problems/dp/0525537090/">Amazon</a>,\n    <a href="http://links.penguinrandomhouse.com/type/affiliate/isbn/9780525537090/siteID/8001/retailerid/2/trackingcode/PRH5522E62429">B&N</a>,\n    <a href="http://links.penguinrandomhouse.com/type/affiliate/isbn/9780525537090/siteID/8001/retailerid/6/trackingcode/penguinrandom">IndieBound</a>,\n    <a href="https://itunes.apple.com/us/book/how-to/id1451461524?mt=11">Apple</a>,\n    <a href="https://www.audible.com/search?advsearchKeywords=How+To+Randall+Munroe&source_code=COMA0213WS031709&SID=PRHA9A5E24CFB--9780525635680">Audible</a>,\n    <a href="http://links.penguinrandomhouse.com/type/affiliate/isbn/9780525537090/siteID/8001/retailerid/23/trackingcode/PRH3D17167A3B">Target</a>\n</div>\n<script>\nvar client = new XMLHttpRequest();\nclient.open("GET", "//c.xkcd.com/how-to/news", true);\nclient.send();\nclient.onreadystatechange = function() {\n  if(client.readyState == 4 && client.status == 200) {\n    document.getElementById("htNews").innerHTML = client.responseText;\n  }\n}\n</script>\n\n</div>\n</div>\n<div id="bgLeft" class="bg box"></div>\n<div id="bgRight" class="bg box"></div>\n</div>\n<div id="middleContainer" class="box">\n\n<div id="ctitle">Phylogenetic Tree</div>\n<ul class="comicNav">\n<li><a href="/1/">|&lt;</a></li>\n<li><a rel="prev" href="/2268/" accesskey="p">&lt; Prev</a></li>\n<li><a href="//c.xkcd.com/random/comic/">Random</a></li>\n<li><a rel="next" href="#" accesskey="n">Next &gt;</a></li>\n<li><a href="/">&gt;|</a></li>\n</ul>\n<div id="comic">\n<img src="//imgs.xkcd.com/comics/phylogenetic_tree.png" title="And I was kicked out of my March Madness pool because I wouldn&#39;t shut up about the evidence for NBA/ABA endosymbiosis." alt="Phylogenetic Tree" srcset="//imgs.xkcd.com/comics/phylogenetic_tree_2x.png 2x"/>\n</div>\n<ul class="comicNav">\n<li><a href="/1/">|&lt;</a></li>\n<li><a rel="prev" href="/2268/" accesskey="p">&lt; Prev</a></li>\n<li><a href="//c.xkcd.com/random/comic/">Random</a></li>\n<li><a rel="next" href="#" accesskey="n">Next &gt;</a></li>\n<li><a href="/">&gt;|</a></li>\n</ul>\n<br />\nPermanent link to this comic: https://xkcd.com/2269/<br />\nImage URL (for hotlinking/embedding): https://imgs.xkcd.com/comics/phylogenetic_tree.png\n<div id="transcript" style="display: none"></div>\n</div>\n<div id="bottom" class="box">\n<img src="//imgs.xkcd.com/s/a899e84.jpg" width="520" height="100" alt="Selected Comics" usemap="#comicmap"/>\n<map id="comicmap" name="comicmap">\n<area shape="rect" coords="0,0,100,100" href="/150/" alt="Grownups"/>\n<area shape="rect" coords="104,0,204,100" href="/730/" alt="Circuit Diagram"/>\n<area shape="rect" coords="208,0,308,100" href="/162/" alt="Angular Momentum"/>\n<area shape="rect" coords="312,0,412,100" href="/688/" alt="Self-Description"/>\n<area shape="rect" coords="416,0,520,100" href="/556/" alt="Alternative Energy Revolution"/>\n</map>\n<br />\n<a href="//xkcd.com/1732/"><img border=0 src="//imgs.xkcd.com/s/temperature.png" width="520" height="100" alt="Earth temperature timeline"></a>\n<br />\n<div>\n<!--\nSearch comic titles and transcripts:\n<script type="text/javascript" src="//www.google.com/jsapi"></script>\n<script type="text/javascript">google.load(\'search\', \'1\');google.setOnLoadCallback(function() {google.search.CustomSearchControl.attachAutoCompletion(\'012652707207066138651:zudjtuwe28q\',document.getElementById(\'q\'),\'cse-search-box\');});</script>\n<form action="//www.google.com/cse" id="cse-search-box">\n<div>\n<input type="hidden" name="cx" value="012652707207066138651:zudjtuwe28q"/>\n<input type="hidden" name="ie" value="UTF-8"/>\n<input type="text" name="q" id="q" size="31"/>\n<input type="submit" name="sa" value="Search"/>\n</div>\n</form>\n<script type="text/javascript" src="//www.google.com/cse/brand?form=cse-search-box&amp;lang=en"></script>\n-->\n<a href="/rss.xml">RSS Feed</a> - <a href="/atom.xml">Atom Feed</a> - <a href="/newsletter/">Email</a>\n</div>\n<br />\n<div id="comicLinks">\nComics I enjoy:<br/>\n        <a href="http://threewordphrase.com/">Three Word Phrase</a>,\n        <a href="http://www.smbc-comics.com/">SMBC</a>,\n        <a href="http://www.qwantz.com">Dinosaur Comics</a>,\n        <a href="http://oglaf.com/">Oglaf</a> (nsfw),\n        <a href="http://www.asofterworld.com">A Softer World</a>,\n        <a href="http://buttersafe.com/">Buttersafe</a>,\n        <a href="http://pbfcomics.com/">Perry Bible Fellowship</a>,\n        <a href="http://questionablecontent.net/">Questionable Content</a>,\n        <a href="http://www.buttercupfestival.com/">Buttercup Festival</a>,\n        <a href="http://www.mspaintadventures.com/?s=6&p=001901">Homestuck</a>,\n\t<a href="http://www.jspowerhour.com/">Junior Scientist Power Hour</a>\n</div>\n<br />\n<div id="comicLinks">\nOther things:<br/>\n        <a href="https://medium.com/civic-tech-thoughts-from-joshdata/so-you-want-to-reform-democracy-7f3b1ef10597">Tips on technology and government</a>,<br /> \n        <a href="https://www.nytimes.com/interactive/2017/climate/what-is-climate-change.html">Climate FAQ</a>,\n\t<a href="https://twitter.com/KHayhoe">Katharine Hayhoe</a>\n</div>\n<br />\n<center>\n<div id="footnote" style="width:70%">xkcd.com is best viewed with Netscape Navigator 4.0 or below on a Pentium 3&plusmn;1 emulated in Javascript on an Apple IIGS<br />at a screen resolution of 1024x1. Please enable your ad blockers, disable high-heat drying, and remove your device<br />from Airplane Mode and set it to Boat Mode. For security reasons, please leave caps lock on while browsing.</div>\n</center>\n<div id="licenseText">\n<p>\nThis work is licensed under a\n<a href="http://creativecommons.org/licenses/by-nc/2.5/">Creative Commons Attribution-NonCommercial 2.5 License</a>.\n</p><p>\nThis means you\'re free to copy and share these comics (but not to sell them). <a rel="license" href="/license.html">More details</a>.</p>\n</div>\n</div>\n</body>\n<!-- Layout by Ian Clasbey, davean, and chromakode -->\n</html>\n\n'

# now we use r.content for saving a image

# r = requests.get('https://imgs.xkcd.com/comics/phylogenetic_tree.png')
# with open('comic.png','wb') as f:
#     f.write(r.content)
#o/p is --->        saving this image in current directory in file comic.png

# r= requests.get('https://xkcd.com/')
# print (r.status_code)           ---->   o/p is     200

# print(r.ok)             ----> o/p is 200
# print (r.headers)
# o/p is          {'Server': 'nginx', 'Content-Type': 'text/html', 'Last-Modified': 'Mon, 17 Feb 2020 05:00:03 GMT', 'ETag': 'W/"5e4a1dd3-1e46"', 'Expires': 'Mon, 17 Feb 2020 05:05:49 GMT', 'Cache-Control': 'max-age=300', 'Content-Encoding': 'gzip', 'Content-Length': '3077', 'Accept-Ranges': 'bytes', 'Date': 'Mon, 17 Feb 2020 08:18:26 GMT', 'Via': '1.1 varnish', 'Age': '141', 'Connection': 'keep-alive', 'X-Served-By': 'cache-maa18326-MAA', 'X-Cache': 'HIT', 'X-Cache-Hits': '1', 'X-Timer': 'S1581927506.422291,VS0,VE0', 'Vary': 'Accept-Encoding'}

# payload = {'page':2}
# r = requests.get('https://httpbin.org/get',params=payload)
# print (r.url)           --->        https://httpbin.org/get?page=2
# print (r.text)
#o/p is

# {
#   "args": {
#     "page": "2"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.22.0",
#     "X-Amzn-Trace-Id": "Root=1-5e4a4dc2-c0260f509bc4e020298c4660"
#   },
#   "origin": "45.127.46.192",
#   "url": "https://httpbin.org/get?page=2"
# }

# payload = {'username':'monty','password':12345}
# r = requests.post('https://httpbin.org/post',data=payload)
# print (r.text)
# o/p is :
# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {
#     "password": "12345",
#     "username": "monty"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Length": "29",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.22.0",
#     "X-Amzn-Trace-Id": "Root=1-5e4a4e67-d118e406a633c938aa0523c4"
#   },
#   "json": null,
#   "origin": "45.127.46.192",
#   "url": "https://httpbin.org/post"
# }
# print (r.url)           --->        https://httpbin.org/post

# payload = {'username':'monty','password':12345}
# r = requests.post('https://httpbin.org/post',data=payload)
# r_dict = r.json()       ---> convert json string into a python dictionary
# print (r_dict['form'])

#authentication bya basic-auth-route

# r = requests.get('https://httpbin.org/basic-auth/monty/12345',auth=('monty',12345))
# print(r.text)
# o/p is :
# {
#   "authenticated": true,
#   "user": "monty"
# }

# response = requests.get(
#     'https://api.github.com/search/repositories',
#     params={'q': 'requests+language:python'},
#     headers={'Accept': 'application/vnd.github.v3.text-match+json'},
# )

# requests.post('https://httpbin.org/post', data={'key':'value'})
# >>> requests.put('https://httpbin.org/put', data={'key':'value'})
# >>> requests.delete('https://httpbin.org/delete')
# >>> requests.head('https://httpbin.org/get')
# >>> requests.patch('https://httpbin.org/patch', data={'key':'value'})
# >>> requests.options('https://httpbin.org/get')

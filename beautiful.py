# from bs4 import BeautifulSoup
# import requests

# # source = requests.get('http://coreyms.com').text
# #  print (source)
#
# # o/p :
#
# # <!DOCTYPE html>
# # <html lang="en-US">
# # <head >
# # <meta charset="UTF-8" />
# # <meta name="viewport" content="width=device-width, initial-scale=1" />
# # <title>CoreyMS - Development, Design, DIY, and more</title>
# #
# # <!-- This site is optimized with the Yoast SEO plugin v13.0 - https://yoast.com/wordpress/plugins/seo/ -->
# # <meta name="description" content="Development, Design, DIY, and more"/>
# # <meta name="robots" content="max-snippet:-1, max-image-preview:large, max-video-preview:-1"/>
# # <link rel="canonical" href="https://coreyms.com/" />
# # <link rel="next" href="http://coreyms.com/page/2" />
# # <meta property="og:locale" content="en_US" />
# # <meta property="og:type" content="website" />
# # <meta property="og:title" content="CoreyMS - Development, Design, DIY, and more" />
# # <meta property="og:description" content="Development, Design, DIY, and more" />
# # <meta property="og:url" content="https://coreyms.com/" />
# # <meta property="og:site_name" content="CoreyMS" />
# # <meta property="og:image" content="https://coreyms.com/wp-content/uploads/2014/11/SocialIcon.png" />
# # <meta property="og:image:secure_url" content="https://coreyms.com/wp-content/uploads/2014/11/SocialIcon.png" />
# # <meta property="og:image:width" content="800" />
# # <meta property="og:image:height" content="800" />
# # <meta name="twitter:card" content="summary_large_image" />
# # <meta name="twitter:description" content="Development, Design, DIY, and more" />
# # <meta name="twitter:title" content="CoreyMS - Development, Design, DIY, and more" />
# # <meta name="twitter:site" content="@CoreyMSchafer" />
# # <meta name="twitter:image" content="http://coreyms.com/wp-content/uploads/2014/11/SocialIcon.png" />
# # <meta name="msvalidate.01" content="69D01EB6520B2918B78685B21805C977" />
# # <meta name="google-site-verification" content="cWGcd5qKYyguo-9DC8wgwnOjN0_P9bBazUyRTtHohMU" />
# # <script type='application/ld+json' class='yoast-schema-graph yoast-schema-graph--main'>{"@context":"https://schema.org","@graph":[{"@type":"WebSite","@id":"https://coreyms.com/#website","url":"https://coreyms.com/","name":"CoreyMS","description":"Development, Design, DIY, and more","potentialAction":{"@type":"SearchAction","target":"https://coreyms.com/?s={search_term_string}","query-input":"required name=search_term_string"}},{"@type":"CollectionPage","@id":"https://coreyms.com/#webpage","url":"https://coreyms.com/","inLanguage":"en-US","name":"CoreyMS - Development, Design, DIY, and more","isPartOf":{"@id":"https://coreyms.com/#website"},"description":"Development, Design, DIY, and more"}]}</script>
# # <!-- / Yoast SEO plugin. -->
# #
# # <link rel='dns-prefetch' href='//fonts.googleapis.com' />
# # <link rel='dns-prefetch' href='//s.w.org' />
# # <link rel="alternate" type="application/rss+xml" title="CoreyMS &raquo; Feed" href="https://coreyms.com/feed" />
# # <link rel="alternate" type="application/rss+xml" title="CoreyMS &raquo; Comments Feed" href="https://coreyms.com/comments/feed" />
# # 		<script type="text/javascript">
# # 			window._wpemojiSettings = {"baseUrl":"https:\/\/s.w.org\/images\/core\/emoji\/12.0.0-1\/72x72\/","ext":".png","svgUrl":"https:\/\/s.w.org\/images\/core\/emoji\/12.0.0-1\/svg\/","svgExt":".svg","source":{"concatemoji":"https:\/\/coreyms.com\/wp-includes\/js\/wp-emoji-release.min.js?ver=5.3.2"}};
# # 			!function(e,a,t){var r,n,o,i,p=a.createElement("canvas"),s=p.getContext&&p.getContext("2d");function c(e,t){var a=String.fromCharCode;s.clearRect(0,0,p.width,p.height),s.fillText(a.apply(this,e),0,0);var r=p.toDataURL();return s.clearRect(0,0,p.width,p.height),s.fillText(a.apply(this,t),0,0),r===p.toDataURL()}function l(e){if(!s||!s.fillText)return!1;switch(s.textBaseline="top",s.font="600 32px Arial",e){case"flag":return!c([127987,65039,8205,9895,65039],[127987,65039,8203,9895,65039])&&(!c([55356,56826,55356,56819],[55356,56826,8203,55356,56819])&&!c([55356,57332,56128,56423,56128,56418,56128,56421,56128,56430,56128,56423,56128,56447],[55356,57332,8203,56128,56423,8203,56128,56418,8203,56128,56421,8203,56128,56430,8203,56128,56423,8203,56128,56447]));case"emoji":return!c([55357,56424,55356,57342,8205,55358,56605,8205,55357,56424,55356,57340],[55357,56424,55356,57342,8203,55358,56605,8203,55357,56424,55356,57340])}return!1}function d(e){var t=a.createElement("script");t.src=e,t.defer=t.type="text/javascript",a.getElementsByTagName("head")[0].appendChild(t)}for(i=Array("flag","emoji"),t.supports={everything:!0,everythingExceptFlag:!0},o=0;o<i.length;o++)t.supports[i[o]]=l(i[o]),t.supports.everything=t.supports.everything&&t.supports[i[o]],"flag"!==i[o]&&(t.supports.everythingExceptFlag=t.supports.everythingExceptFlag&&t.supports[i[o]]);t.supports.everythingExceptFlag=t.supports.everythingExceptFlag&&!t.supports.flag,t.DOMReady=!1,t.readyCallback=function(){t.DOMReady=!0},t.supports.everything||(n=function(){t.readyCallback()},a.addEventListener?(a.addEventListener("DOMContentLoaded",n,!1),e.addEventListener("load",n,!1)):(e.attachEvent("onload",n),a.attachEvent("onreadystatechange",function(){"complete"===a.readyState&&t.readyCallback()})),(r=t.source||{}).concatemoji?d(r.concatemoji):r.wpemoji&&r.twemoji&&(d(r.twemoji),d(r.wpemoji)))}(window,document,window._wpemojiSettings);
# # 		</script>
# # 		<style type="text/css">
# # img.wp-smiley,
# # img.emoji {
# # 	display: inline !important;
# # 	border: none !important;
# # 	box-shadow: none !important;
# # 	height: 1em !important;
# # 	width: 1em !important;
# # 	margin: 0 .07em !important;
# # 	vertical-align: -0.1em !important;
# # 	background: none !important;
# # 	padding: 0 !important;
# # }
# # </style>
# # 	<link rel="stylesheet" href="https://coreyms.com/wp-content/cache/minify/119a3.css" media="all" />
# #
# #
# # <style id='wp-block-library-inline-css' type='text/css'>
# # .has-text-align-justify{text-align:justify;}
# # </style>
# # <link rel="stylesheet" href="https://coreyms.com/wp-content/cache/minify/4c431.css" media="all" />
# #
# # <link rel='stylesheet' id='google-fonts-css'  href='//fonts.googleapis.com/css?family=Lato%3A300%2C400%2C700%7CVarela+Round&#038;ver=2.1.2' type='text/css' media='all' />
# # <link rel="stylesheet" href="https://coreyms.com/wp-content/cache/minify/95173.css" media="all" />
# #
# #
# # <script src="https://coreyms.com/wp-content/cache/minify/df983.js"></script>
# #
# #
# # <!--[if lt IE 9]>
# # <script type='text/javascript' src='https://coreyms.com/wp-content/themes/genesis/lib/js/html5shiv.min.js?ver=3.7.3'></script>
# # <![endif]-->
# # <link rel='https://api.w.org/' href='https://coreyms.com/wp-json/' />
# # <link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://coreyms.com/xmlrpc.php?rsd" />
# # <link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://coreyms.com/wp-includes/wlwmanifest.xml" />
# # <meta name="generator" content="WordPress 5.3.2" />
# # <style type="text/css"> .enews .screenread {
# # 	height: 1px;
# #     left: -1000em;
# #     overflow: hidden;
# #     position: absolute;
# #     top: -1000em;
# #     width: 1px; } </style>
# # <link rel='dns-prefetch' href='//v0.wordpress.com'/>
# # <link rel="pingback" href="https://coreyms.com/xmlrpc.php" />
# # <link rel="author" href="https://plus.google.com/+CoreySchafer44/posts" />
# #
# # <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-57x57.png">
# # <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114x114.png">
# # <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-72x72.png">
# # <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144x144.png">
# # <link rel="apple-touch-icon" sizes="60x60" href="/apple-touch-icon-60x60.png">
# # <link rel="apple-touch-icon" sizes="120x120" href="/apple-touch-icon-120x120.png">
# # <link rel="apple-touch-icon" sizes="76x76" href="/apple-touch-icon-76x76.png">
# # <link rel="apple-touch-icon" sizes="152x152" href="/apple-touch-icon-152x152.png">
# # <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon-180x180.png">
# # <link rel="icon" type="image/png" href="/favicon-192x192.png" sizes="192x192">
# # <link rel="icon" type="image/png" href="/favicon-160x160.png" sizes="160x160">
# # <link rel="icon" type="image/png" href="/favicon-96x96.png" sizes="96x96">
# # <link rel="icon" type="image/png" href="/favicon-16x16.png" sizes="16x16">
# # <link rel="icon" type="image/png" href="/favicon-32x32.png" sizes="32x32">
# # <meta name="msapplication-TileColor" content="#56616b">
# # <meta name="msapplication-TileImage" content="/mstile-144x144.png">
# #
# # <script>
# #   (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
# #   (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
# #   m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
# #   })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
# #   ga('create', 'UA-53634311-1', 'auto');
# #   ga('send', 'pageview');
# # </script></head>
# # <body class="home blog content-sidebar" itemscope itemtype="https://schema.org/WebPage"><div class="site-container"><header class="site-header" itemscope itemtype="https://schema.org/WPHeader"><div class="wrap"><div class="title-area">	<div class="site-avatar">
# # 		<a href="https://coreyms.com/"><svg class="site-avatar-svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Layer_1" x="0px" y="0px" width="150px" height="150px" viewBox="0 0 441.5 441.5" enable-background="new 0 0 441.5 441.5" xml:space="preserve">
# #                     <g class="site-avatar-background">
# #                         <path fill="#56616B" d="M79.178 390.133C30.781 349.639 0 288.789 0 220.75C0 98.833 98.833 0 220.75 0S441.5 98.833 441.5 220.75 c0 63.558-26.86 120.842-69.848 161.12"/>
# #                     </g>
# #                     <g class="site-avatar-foreground">
# #                         <path fill="#E3E0DD" d="M254.602 182.291c0 1.992-0.097 4 0 6c0.057 0.88-0.093 1.952 0.194 2.78c0.22 0.631 0.69 1.12 1.704 1.273 c2.009 0.3 3.436-1.062 4.384-2.719c0.712-1.244 0.863-3.376 1.843-3.807c1.612-0.712 2.646-1.537 3.276-2.44 c1.903-2.732 0.09-6.185-0.723-9.42c-0.29-1.157-1.995-2.036-0.556-3.456c0.801-0.789 1.711-0.981 2.717-0.718 c0.164 0.043 0.33 0.095 0.5 0.162c0.262 0.104 0.505 0.185 0.732 0.249c3.521 0.99 3.182-2.499 3.459-4.337 c0.262-1.728 0.411-3.561-0.128-5.161c-0.413-1.229-1.231-2.321-2.721-3.124c-0.345-0.187-1.271 0.296-1.683 0.7 C260.971 165 252.55 170.8 254.65 182.291H254.602z"/>
# #                         <path fill="#E3E0DD" d="M121.076 185.062c-0.633 2.075-1.555 4.107-1.326 6.3c1.215 11.7 4.9 22.7 10.4 32.958 c1.692 3.201 3.6 6.4 6.3 8.931c6.878 6.299 15.1 11.5 18.3 21.101c0.697 2.1 2.7 3.799 4.1 5.616c0.797 1.101 7.7 7.5 9.9 9.06 c5.75 4 12.2 2.399 18.3 2.701c3.969 0.19 7.635-0.422 10.23-2.799c1.496-1.371 2.638-3.322 3.271-6.056 c0.378-1.636 1.506-3.308 2.812-4.621c0.372-0.374 0.756-0.724 1.144-1.028c0.236-0.187 0.452-0.393 0.683-0.584 c2.745-2.268 5.197-4.824 7.772-7.193c0.196-0.182 0.395-0.361 0.593-0.541c0.263-0.235 0.516-0.484 0.783-0.715 c2.067-1.778 3.228-4.668 5.456-6.357c0.991-0.751 2.192-1.268 3.781-1.339c4.19-0.188 7.815-1.231 10.56-3.522 c2.112-1.764 3.703-4.267 4.627-7.693c0.437-1.615 2.252-2.815 3.221-4.342c1.367-2.154 1.631-5.814-0.541-5.996 c-5.594-0.462-3.601-4.181-3.784-6.851c-0.224-3.178 0.817-6.237 1.688-9.293c2.23-7.859 2.068-15.447-2.718-22.497 c-1.593-2.346-2.862-4.882-3.588-7.658c-0.304-1.159-0.571-2.27 0.562-2.565c0.258-0.067 0.584-0.093 1.002-0.067 c0.979 0.081 2.138 1.205 2.97 0.79c0.196-0.099 0.377-0.282 0.53-0.589c0.812-1.632-0.619-3.176-1.769-4.355 c-1.974-2.029-2.121-3.545 0.03-5.829c4.014-4.26 2.55-9.908-3.036-11.764c-3.315-1.103-5.812-2.844-8.128-5.404 c-3.221-3.559-7.302-6.113-12.188-4.117c-0.077 0.031-0.152 0.054-0.229 0.087c-4.316 1.881-8.25 4.641-12.839 7.3 c5.969 2.5 11.4 4 17.4 3.326c4.219-0.484 7.9 0.8 10.7 4.1c1.021 1.2 1.1 2.8 0.1 4.197c-0.256 0.386-0.549 0.657-0.873 0.774 c-0.367 0.132-0.774 0.069-1.225-0.274c-4.875-3.503-10.354-1.259-15.552-1.665c-1.768-0.138-4.002 0.686-5.052-1.229 c-0.998-1.819-2.014-2.475-3.065-2.466c-1.199 0.009-2.443 0.886-3.757 1.931c-0.647 0.515-1.219 1.372-2.061 1.577 c-0.304 0.074-0.642 0.067-1.033-0.077c-0.107-2.153 2.641-2.457 2.183-4.465c-2.788-0.657-5.483-0.628-8.281 0.466 c-0.928 0.363-1.869 0.849-2.827 1.464c-0.095 0.061-0.188 0.107-0.283 0.17c0.945-3.138 5.419-5.098 0.606-7.558 c-0.949-0.485 0.189-1.66 1.02-2.292c1.043-0.794 2.321-1.519 2.936-2.594c1.521-2.665 3.594-4.347 5.997-5.363 c1.868-0.791 3.936-1.18 6.098-1.316c4.041-0.255 7.759-1.711 11.647-2.479c0.852-0.168 1.606-0.458 2.265-0.854 c1.858-1.119 2.911-3.136 2.915-6.033c0.009-6.685-2.918-12.743-3.582-19.266c-0.12-1.184-1.234-3.36-3.023-2.574 c-3.523 1.548-5.289-0.921-6.55-2.962c-1.631-2.64-3.149-2.745-4.879-1.815c-0.514 0.276-1.045 0.64-1.605 1.06 c-1.044 0.784-1.544 2.183-2.749 2.872c-0.285 0.163-0.596 0.298-0.977 0.362c-0.388-1.862 1.36-2.985 1.44-4.602 c0.051-1.008-0.054-2.516-1.327-1.745c-0.018 0.011-0.031 0.012-0.05 0.024c-0.144 0.092-0.273 0.166-0.403 0.24 c-2.564 1.457-2.537-0.535-2.866-2.284c-0.325-1.727-1.001-3.345-2.837-3.741c-0.406-0.087-0.729-0.082-0.991-0.007 c-1.147 0.325-1.128 1.968-1.773 2.907c-1.611 2.263-3.115 4.664-6.599 7.237c-0.113 0.083-0.21 0.166-0.328 0.25 c2.371-4.847 3.656-8.487 0.458-12.642c-0.07-0.09-0.129-0.18-0.203-0.271c-0.833 4.386-1.515 8.2-4.973 10.605 c-0.093 0.064-0.18 0.133-0.277 0.195c-1.097-1.5 0.22-3.408-1.72-4.438c-0.012-0.006-0.021-0.014-0.032-0.02 c-0.35 0.452-0.84 0.881-1.076 1.4c-1.153 2.642-1.673 3.754-2.146 4.263c-0.381 0.41-0.731 0.431-1.355 0.537 c-3.99 0.632-4.702-1.837-5.834-4.938c-2.642-7.239-9.918-10.402-14.395-6.815c-0.378 0.303-0.743 0.637-1.077 1.039 c-2.435 2.929-4.771 6.612-5.835 10c-1.345 4.336-3.751 6.76-7.148 8.956c-5.305 3.428-8.463 7.855-7.026 14.6 c0.539 2.542-0.675 4.875-1.846 7.1c-1.875 3.597-0.992 5.7 3.3 5.997c1.991 0.1 4 0.5 6 0.553c4.777 0.2 8.7 1.7 12.6 5 c3.784 3.3 6.8 7.3 10.6 10.378c3.999 3.3 5.2 6.9 4.6 11.811c-0.675 6.117-1.21 12.273-1.305 18.4 c-0.06 3.896-0.854 6.795-4.75 8.389c-1.934 0.791-3.424 2.349-2.862 4.699c0.609 2.5 2.7 3.2 5 3.1 c0.5-0.016 1.015-0.126 1.496-0.042c2.554 0.4 5.5 0.6 2.8 4.468c-0.756 1.058-0.791 2.3 0.8 2.8c1.242 0.4 3 0.2 2.5 2.2 c-0.369 1.521-2.162 1.237-3.3 1.809c-0.792 0.397-1.632 0.577-2.505 0.667c-1.329 0.138-2.731 0.069-4.149 0.233 c-1.444 0.167-2.903 0.575-4.315 1.699c0.827 0.264 1.74 0.504 2.708 0.726c8.333 1.914 20.87 2.433 20.086 3.987 c-0.007 0.015-0.021 0.03-0.031 0.045c-0.02 0.031-0.033 0.061-0.063 0.092h0.009v0.051c-4.351 0.46-8.029 1.064-12.392 1.2 c-1.847 0.066-3.692-0.031-4.682 1.264c-0.246 0.323-0.441 0.728-0.568 1.247c-0.572 2.399 1.2 4.101 2.9 5.399 c1.688 1.302 3.7 2.302 5.3 3.7c2.363 1.9 1.9 4.699 0.9 6.913c-0.278 0.625-0.608 0.995-0.969 1.202 c-1.229 0.705-2.845-0.562-4.213-0.901c-3.906-1.047-5.531-4.397-7.769-7.324c-4.868-6.364-7.044-12.982-16.966-15.704 c-0.459-0.125-0.913-0.253-1.406-0.362c-1.632-0.36-1.601-0.026-1.583-2c0.017-1.846 4.917-0.833 6.5-1.333 c5.514-1.741 5.65-2.834 10.5-4.167c3.46-0.951 2.169-6.663 1.322-10.273c-0.003-0.014-0.007-0.029-0.01-0.043 c-0.104-0.441-0.179-0.878-0.232-1.312c-0.361-2.919 0.352-5.695 1.408-8.45c6.845-10.339 3.558-20.753 4.884-23.425 c0.777-1.565 1.148-2.989 1.094-4.267c-0.092-2.177-1.423-3.929-4.123-5.227c-7.634-3.67-15.45-6.876-23.707-8.9 c-1.792-0.439-3.357-0.107-4.359 1.482c-0.006 0.009-0.013 0.016-0.019 0.025c-1.01 1.628-1.361 3.475-0.355 5.2 c0.944 1.6 2.6 1 4 1c5.133-0.093 10.274-0.174 15.4 0.045c3.086 0.1 3.9 1.8 2.4 4.722c-0.343 0.664-0.82 1.233-1.384 1.709 c-2.594 2.19-7.13 2.328-10.065-0.209c-0.722-0.629-1.141-1.751-2.391-1.317c-0.15 0.052-0.262 0.125-0.365 0.204 c-0.378 0.292-0.477 0.754-0.492 1.357c-0.035 1.376-0.479 2.212-1.139 2.757c-1.51 1.246-4.167 0.963-5.775 2.043 c-1.373 0.908-3.125-1.413-3.536-3.282c-0.312-1.417-0.514-2.734-2.291-2.62c-0.586 0.038-1.049 0.236-1.412 0.534 c-0.625 0.514-0.948 1.329-1.06 2.166c-0.39 2.976-0.977 6.3 0.9 8.741C123.411 174.752 122.676 179.853 121.076 185.062z M211.68 211.557c0.16-0.005 0.319-0.011 0.479-0.017c0.196-0.006 0.401-0.005 0.61 0c1.39 0.026 2.971 0.134 3.738-1.328 c0.028-0.053 0.064-0.089 0.09-0.146c0.049-0.119 0.086-0.232 0.113-0.341c0.398-1.586-1.396-2.169-2.316-3.113 c-0.159-0.163-0.322-0.34-0.462-0.523c-0.389-0.508-0.595-1.069 0.001-1.558c0.515-0.422 1.704-0.564 2.294-0.258 c3.199 1.7 4.7 0.5 5.533-2.735c0.286-1.132 1.02-1.809 1.979-1.574c0.325 0.079 0.677 0.262 1.047 0.568 c2.446 2 4.8 4.2 5.601 7.437c0.483 2 0.5 4.07-1.045 5.7c-1.617 1.698-3.396 0.774-5.011-0.143 c-2.403-1.37-4.178-0.281-5.707 1.436c-3.979 4.466-8.223 8.75-11.737 13.601c-3.714 5.086-8.537 5.843-14.104 5.198 c-0.648-0.075-1.368-0.171-1.786-0.653c-0.114-0.131-0.209-0.285-0.27-0.482c-0.37-1.215 0.587-1.834 1.458-2.285 c2.948-1.527 5.975-2.908 8.896-4.486c1.887-1.021 3.851-2.061 5.402-3.496c1.875-1.738 5.248-3.51 4.134-6.221 c-0.141-0.343-0.323-0.6-0.535-0.794c-1.383-1.272-4.106 0.29-6.09 0.26c-4.13-0.028-8.242-0.928-12.342-0.218h-0.023v-0.073 c0.004-0.002 0.008-0.003 0.012-0.005c0.007-0.003 0.014-0.006 0.021-0.009c0.814-0.378 1.633-0.717 2.458-1.021 c2.471-0.91 4.987-1.504 7.531-1.902c0.032-0.005 0.064-0.011 0.096-0.016c0.033-0.005 0.065-0.009 0.098-0.014 C205.084 211.85 208.374 211.669 211.68 211.557z M194.177 187.948c3.15 2.3 4 6 2.9 6.258h-0.062 c-2.208-0.583-2.876-3.92-5.816-4.751c-0.006-0.001-0.012-0.005-0.018-0.007c-3.767-1.083-9.077-8.666-9.81-13.188 c-0.011-0.066-0.031-0.139-0.04-0.204c-0.012-0.087-0.008-0.164-0.016-0.249c-0.02-0.205-0.042-0.413-0.039-0.601 c0-0.001 0-0.001 0-0.002c0.001-0.067 0.017-0.102 0.025-0.152c0.146-0.854 1.329 0.547 2.516 2.208 c1.004 1.406 2.003 2.98 2.358 3.487c0.982 1.393 1.82 2.389 2.686 3.229C190.297 185.367 191.808 186.328 194.177 187.948z"/>
# #                         <path fill="#E3E0DD" d="M397.368 309.241c-0.261-0.421-0.515-0.851-0.789-1.251c-0.119-0.172-0.252-0.329-0.374-0.498 c-0.355-0.493-0.713-0.985-1.097-1.449c-1.061-1.284-2.228-2.461-3.529-3.541c-9.653-8.013-20.562-14.354-29.925-22.777 c-5.18-4.66-11.315-8.287-16.289-13.133c-3.436-3.346-6.821-6.178-11.363-7.746c-12.746-4.402-25.297-9.318-37.806-14.363 c-5.212-2.104-8.992-6.655-14.148-8.286c-5.011-1.585-9.368-3.845-13.188-7.062c-1.195-1.008-2.342-2.103-3.436-3.309 c-0.236-0.263-0.504-0.511-0.797-0.736c-1.041-0.805-2.462-1.286-4.507-0.657c2.625 3 6.2 4.898 6.2 8.75 c0.029 10.375-1.518 20.563-4.211 30.575c-0.283 1.058-0.617 2.509-2.144 2.399c-0.126-0.014-0.231-0.047-0.34-0.078 c-1.058-0.322-1.254-1.564-1.737-2.489c-1.168-2.226 0.229-5.108-1.879-7.075c-4.517-4.214-4.992-10.279-7.05-15.604 c-0.729-1.892 0.104-4.437-2.731-5.277c-0.006-0.003-0.013-0.006-0.021-0.008c-2.953-0.86-3.546 1.873-5.052 3.187 c-8.374 7.295-12.026 18.521-21.318 25.2c-8.297 5.931-16.328 12.183-26.8 13.716c-2.79 0.407-5.649 0.323-8.459 0.627 c-1.733 0.188-3.997-0.093-4.459 2.299c-0.365 1.899 1.1 3.102 2.5 3.949c1.73 1 3.1 2.899 4.7 3.578 c3.386 1.398 2.6 2.698 0.7 4.5c-2.543 2.476-3.724 4.93-0.872 8.198c1.765 2.021-0.304 4.5-1.314 5.711 c-0.307 0.367-0.615 0.511-0.923 0.513c-1.023 0.006-2.039-1.625-2.944-2.394c-0.887-0.75-1.582-1.731-2.484-2.459 c-1.267-1.021-2.576-2.888-4.149-2.603c-0.405 0.072-0.826 0.281-1.27 0.691c-2.076 1.9 0 3.9 1.4 5.602 c4.511 5.563 8.05 11.524 8.194 19.838c0 0.056 0.005 0.106 0.006 0.162c-3.156-2.711-6.338-4.35-8.485-7.479 c-1.777-2.588-3.426-5.543-6.256-7.043c-7.64-4.051-12.329-9.996-14.186-18.574c-1.413-6.529-1.927-13.146-3.01-19.693 c-1.136-6.866-2.037-13.854-5.661-20.014c-2.048-3.479-4.663-4.494-8.15-1.59c-3.831 3.191-7.883 6.066-11.413 9.674 c-8.022 8.195-15.606 17.19-26.436 21.801c-11.449 4.848-17.431 13.926-21.416 24.898c-4.198 11.539-5.315 23.633-6.518 35.768 c-1.136 11.451-1.973 22.699 1.5 34c0.259 0.869 0.56 1.72 0.86 2.569c1.22 3.454 2.781 6.741 4.682 9.873 c0.035 0.03 0.07 0.062 0.105 0.09c0.259 0.216 0.513 0.438 0.773 0.653c38.203 31.621 87.228 50.627 140.694 50.627 c53.438 0 102.44-18.985 140.635-50.577c3.521-2.911 6.94-5.938 10.272-9.06c-2.618-3.158-5.301-6.254-8.485-8.67 c-7.959-6.028-17.794-8.264-27.218-11.09c-0.239-0.071-0.48-0.144-0.719-0.215c-0.01-0.004-0.019-0.006-0.026-0.009 c-0.019-0.006-0.035-0.012-0.054-0.019c-0.25-0.076-0.492-0.154-0.724-0.235c-0.029-0.011-0.058-0.021-0.087-0.032 c-0.207-0.074-0.405-0.148-0.598-0.228c-0.136-0.056-0.261-0.113-0.389-0.171c-0.07-0.031-0.144-0.062-0.21-0.094 c-2.793-1.33-3.677-3.312-2.927-7.151c0.733-3.767 2.284-6.832 4.471-9.828c5.71-7.841 12.521-14.705 19.023-21.845 c7.076-7.768 15.928-13.119 25.398-17.319c7.65-3.396 10.099-2.508 15.7 3.799c0.678 0.8 1.1 2.196 3.093 1.354 c0.002-0.002 0.004-0.002 0.007-0.002C397.742 309.809 397.549 309.533 397.368 309.241z"/>
# #                     </g>
# #                 </svg></a>	</div>
# # <h1 class="site-title" itemprop="headline"><a href="https://coreyms.com/">CoreyMS</a></h1><p class="site-description" itemprop="description">Development, Design, DIY, and more</p>	<div class="social-links-div">
# # 		<ul>
# # 			<li class="social-links-li">
# # 				<a class="social-link social-youtube" href="https://www.youtube.com/user/schafer5">
# # 					<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
# # 					     viewBox="0 0 100 100" style="height: 40px; width: 40px;">
# # 						<circle class="outer-shape" cx="50" cy="50" r="48"></circle>
# # 						<path class="inner-shape" style="opacity: 1; fill: rgb(255, 255, 255);"
# # 						      transform="translate(25,25) scale(0.5)"
# # 						      d="M97.284,26.359c-1-5.352-5.456-9.346-10.574-9.839c-12.221-0.784-24.488-1.42-36.731-1.428 c-12.244-0.007-24.464,0.616-36.687,1.388c-5.137,0.497-9.592,4.47-10.589,9.842C1.567,34.058,1,41.869,1,49.678 s0.568,15.619,1.703,23.355c0.996,5.372,5.451,9.822,10.589,10.314c12.226,0.773,24.439,1.561,36.687,1.561 c12.239,0,24.515-0.688,36.731-1.479c5.118-0.497,9.574-5.079,10.574-10.428C98.43,65.278,99,57.477,99,49.676 C99,41.88,98.428,34.083,97.284,26.359z M38.89,63.747V35.272l26.52,14.238L38.89,63.747z"></path>
# # 					</svg>
# # 				</a>
# # 			</li>
# # 			<li class="social-links-li">
# # 				<a class="social-link social-github" href="https://github.com/CoreyMSchafer">
# # 					<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
# # 					     viewBox="0 0 100 100" style="height: 40px; width: 40px;">
# # 						<circle class="outer-shape" cx="50" cy="50" r="48"></circle>
# # 						<path class="inner-shape" style="opacity: 1; fill: rgb(255, 255, 255);"
# # 						      transform="translate(25,25) scale(0.5)"
# # 						      d="M50,1C22.938,1,1,22.938,1,50s21.938,49,49,49s49-21.938,49-49S77.062,1,50,1z M79.099,79.099 c-3.782,3.782-8.184,6.75-13.083,8.823c-1.245,0.526-2.509,0.989-3.79,1.387v-7.344c0-3.86-1.324-6.699-3.972-8.517 c1.659-0.16,3.182-0.383,4.57-0.67c1.388-0.287,2.855-0.702,4.402-1.245c1.547-0.543,2.935-1.189,4.163-1.938 c1.228-0.75,2.409-1.723,3.541-2.919s2.082-2.552,2.847-4.067s1.372-3.334,1.818-5.455c0.446-2.121,0.67-4.458,0.67-7.01 c0-4.945-1.611-9.155-4.833-12.633c1.467-3.828,1.308-7.991-0.478-12.489l-1.197-0.143c-0.829-0.096-2.321,0.255-4.474,1.053 c-2.153,0.798-4.57,2.105-7.249,3.924c-3.797-1.053-7.736-1.579-11.82-1.579c-4.115,0-8.039,0.526-11.772,1.579 c-1.69-1.149-3.294-2.097-4.809-2.847c-1.515-0.75-2.727-1.26-3.637-1.532c-0.909-0.271-1.754-0.439-2.536-0.503 c-0.782-0.064-1.284-0.079-1.507-0.048c-0.223,0.031-0.383,0.064-0.478,0.096c-1.787,4.53-1.946,8.694-0.478,12.489 c-3.222,3.477-4.833,7.688-4.833,12.633c0,2.552,0.223,4.889,0.67,7.01c0.447,2.121,1.053,3.94,1.818,5.455 c0.765,1.515,1.715,2.871,2.847,4.067s2.313,2.169,3.541,2.919c1.228,0.751,2.616,1.396,4.163,1.938 c1.547,0.543,3.014,0.957,4.402,1.245c1.388,0.287,2.911,0.511,4.57,0.67c-2.616,1.787-3.924,4.626-3.924,8.517v7.487 c-1.445-0.43-2.869-0.938-4.268-1.53c-4.899-2.073-9.301-5.041-13.083-8.823c-3.782-3.782-6.75-8.184-8.823-13.083 C9.934,60.948,8.847,55.56,8.847,50s1.087-10.948,3.231-16.016c2.073-4.899,5.041-9.301,8.823-13.083s8.184-6.75,13.083-8.823 C39.052,9.934,44.44,8.847,50,8.847s10.948,1.087,16.016,3.231c4.9,2.073,9.301,5.041,13.083,8.823 c3.782,3.782,6.75,8.184,8.823,13.083c2.143,5.069,3.23,10.457,3.23,16.016s-1.087,10.948-3.231,16.016 C85.848,70.915,82.88,75.317,79.099,79.099L79.099,79.099z"></path>
# # 					</svg>
# # 				</a>
# # 			</li>
# # 			<li class="social-links-li">
# # 				<a class="social-link social-gplus" title="YouTube"
# # 				   href="https://plus.google.com/+CoreySchafer44/posts">
# # 					<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
# # 					     viewBox="0 0 100 100" style="height: 40px; width: 40px;">
# # 						<circle class="outer-shape" cx="50" cy="50" r="48"></circle>
# # 						<path class="inner-shape" style="opacity: 1; fill: rgb(255, 255, 255);"
# # 						      transform="translate(25,25) scale(0.5)"
# # 						      d="M1.079,84.227c-0.024-0.242-0.043-0.485-0.056-0.73C1.036,83.742,1.055,83.985,1.079,84.227z M23.578,55.086 c8.805,0.262,14.712-8.871,13.193-20.402c-1.521-11.53-9.895-20.783-18.701-21.046C9.264,13.376,3.357,22.2,4.878,33.734 C6.398,45.262,14.769,54.823,23.578,55.086z M98.999,25.501v-8.164c0-8.984-7.348-16.335-16.332-16.335H17.336 c-8.831,0-16.078,7.104-16.323,15.879c5.585-4.917,13.333-9.026,21.329-9.026c8.546,0,34.188,0,34.188,0l-7.651,6.471H38.039 c7.19,2.757,11.021,11.113,11.021,19.687c0,7.201-4.001,13.393-9.655,17.797c-5.516,4.297-6.562,6.096-6.562,9.749 c0,3.117,5.909,8.422,8.999,10.602c9.032,6.368,11.955,12.279,11.955,22.15c0,1.572-0.195,3.142-0.58,4.685h29.451 C91.652,98.996,99,91.651,99,82.661V31.625H80.626v18.374h-6.125V31.625H56.127V25.5h18.374V7.127h6.125V25.5H99L98.999,25.501z M18.791,74.301c2.069,0,3.964-0.057,5.927-0.057c-2.598-2.52-4.654-5.608-4.654-9.414c0-2.259,0.724-4.434,1.736-6.366 c-1.032,0.073-2.085,0.095-3.17,0.095c-7.116,0-13.159-2.304-17.629-6.111v6.435l0.001,19.305 C6.116,75.76,12.188,74.301,18.791,74.301L18.791,74.301z M1.329,85.911c-0.107-0.522-0.188-1.053-0.243-1.591 C1.141,84.858,1.223,85.389,1.329,85.911z M44.589,92.187c-1.442-5.628-6.551-8.418-13.675-13.357 c-2.591-0.836-5.445-1.328-8.507-1.36c-8.577-0.092-16.566,3.344-21.074,8.457c1.524,7.436,8.138,13.068,16.004,13.068h27.413 c0.173-1.065,0.258-2.166,0.258-3.295C45.007,94.502,44.86,93.329,44.589,92.187z"></path>
# # 					</svg>
# # 				</a>
# # 			</li>
# # 			<li class="social-links-li">
# # 				<a class="social-link social-twitter" href="https://twitter.com/CoreyMSchafer">
# # 					<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
# # 					     viewBox="0 0 100 100" style="height: 40px; width: 40px;">
# # 						<circle class="outer-shape" cx="50" cy="50" r="48"></circle>
# # 						<path class="inner-shape" style="opacity: 1; fill: rgb(255, 255, 255);"
# # 						      transform="translate(25,25) scale(0.5)"
# # 						      d="M99.001,19.428c-3.606,1.608-7.48,2.695-11.547,3.184c4.15-2.503,7.338-6.466,8.841-11.189 c-3.885,2.318-8.187,4-12.768,4.908c-3.667-3.931-8.893-6.387-14.676-6.387c-11.104,0-20.107,9.054-20.107,20.223 c0,1.585,0.177,3.128,0.52,4.609c-16.71-0.845-31.525-8.895-41.442-21.131C6.092,16.633,5.1,20.107,5.1,23.813 c0,7.017,3.55,13.208,8.945,16.834c-3.296-0.104-6.397-1.014-9.106-2.529c-0.002,0.085-0.002,0.17-0.002,0.255 c0,9.799,6.931,17.972,16.129,19.831c-1.688,0.463-3.463,0.71-5.297,0.71c-1.296,0-2.555-0.127-3.783-0.363 c2.559,8.034,9.984,13.882,18.782,14.045c-6.881,5.424-15.551,8.657-24.971,8.657c-1.623,0-3.223-0.096-4.796-0.282 c8.898,5.738,19.467,9.087,30.82,9.087c36.982,0,57.206-30.817,57.206-57.543c0-0.877-0.02-1.748-0.059-2.617 C92.896,27.045,96.305,23.482,99.001,19.428z"></path>
# # 					</svg>
# # 				</a>
# # 			</li>
# # 			<li class="social-links-li">
# # 				<a class="social-link social-linkedin" href="https://www.instagram.com/coreymschafer/">
# # 					<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
# # 					     viewBox="0 0 100 100" style="height: 40px; width: 40px;">
# # 						<circle class="outer-shape" cx="50" cy="50" r="48"></circle>
# # 						<path class="inner-shape" style="opacity: 1; fill: rgb(255, 255, 255);"
# # 						      transform="translate(25,25) scale(0.5)"
# # 						      d="M88.2,1H11.8C5.85,1,1.026,5.827,1.026,11.781V88.22C1.026,94.174,5.85,99,11.8,99H88.2c5.95,0,10.774-4.826,10.774-10.78 V11.781C98.973,5.827,94.149,1,88.2,1z M49.946,31.184c10.356,0,18.752,8.4,18.752,18.762c0,10.361-8.396,18.761-18.752,18.761 s-18.752-8.4-18.752-18.761S39.589,31.184,49.946,31.184z M87.513,83.615c0,2.165-1.753,3.919-3.917,3.919H16.341 c-2.164,0-3.917-1.755-3.917-3.919v-41.06h8.508c-0.589,2.35-0.904,4.807-0.904,7.34c0,16.612,13.459,30.079,30.063,30.079 s30.063-13.466,30.063-30.079c0-2.533-0.315-4.99-0.904-7.34h8.263L87.513,83.615L87.513,83.615z M87.764,27.124 c0,2.165-1.754,3.919-3.918,3.919H72.723c-2.164,0-3.917-1.755-3.917-3.919v-11.13c0-2.165,1.754-3.919,3.917-3.919h11.123 c2.165,0,3.918,1.755,3.918,3.919V27.124z"></path>
# # 					</svg>
# # 				</a>
# # 			</li>
# # 			<li class="social-links-li">
# # 				<a class="social-link social-rss" href="http://coreyms.com/feed/">
# # 					<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
# # 					     viewBox="0 0 100 100" style="height: 40px; width: 40px;">
# # 						<circle class="outer-shape" cx="50" cy="50" r="48"></circle>
# # 						<path class="inner-shape" style="opacity: 1; fill: rgb(255, 255, 255);"
# # 						      transform="translate(25,25) scale(0.5)"
# # 						      d="M14.044,72.866C6.848,72.866,1,78.736,1,85.889c0,7.192,5.848,12.997,13.044,12.997c7.223,0,13.062-5.804,13.062-12.997 C27.106,78.736,21.267,72.866,14.044,72.866z M1.015,34.299v18.782c12.229,0,23.73,4.782,32.392,13.447 C42.057,75.172,46.832,86.725,46.832,99h18.865C65.697,63.321,36.672,34.3,1.015,34.299L1.015,34.299z M1.038,1v18.791 C44.657,19.792,80.16,55.329,80.16,99H99C99,44.979,55.048,1,1.038,1z"></path>
# # 					</svg>
# # 				</a>
# # 			</li>
# # 		</ul>
# # 	</div>
# # </div><div class="widget-area header-widget-area"><section id="nav_menu-2" class="widget widget_nav_menu"><div class="widget-wrap"><nav class="nav-header" itemscope itemtype="https://schema.org/SiteNavigationElement"><ul id="menu-contact-menu" class="menu genesis-nav-menu js-superfish"><li id="menu-item-984" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-984"><a href="https://coreyms.com/contact" itemprop="url"><span itemprop="name">Contact</span></a></li>
# # <li id="menu-item-153" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-153"><a title="Portfolio" href="http://coreyms.com/portfolio" itemprop="url"><span itemprop="name">Portfolio</span></a></li>
# # </ul></nav></div></section>
# # </div></div></header><nav class="nav-primary" aria-label="Main" itemscope itemtype="https://schema.org/SiteNavigationElement"><div class="wrap"><ul id="menu-primary-navigation" class="menu genesis-nav-menu menu-primary js-superfish"><li id="menu-item-124" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children menu-item-124"><a title="Development" href="https://coreyms.com/category/development" itemprop="url"><span itemprop="name">Development</span></a>
# # <ul class="sub-menu">
# # 	<li id="menu-item-1070" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-1070"><a href="https://coreyms.com/category/development/python" itemprop="url"><span itemprop="name">Python</span></a></li>
# # 	<li id="menu-item-1105" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-1105"><a href="https://coreyms.com/category/development/git" itemprop="url"><span itemprop="name">Git</span></a></li>
# # 	<li id="menu-item-1106" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-1106"><a href="https://coreyms.com/category/development/terminal" itemprop="url"><span itemprop="name">Terminal</span></a></li>
# # 	<li id="menu-item-803" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-803"><a title="JavaScript" href="https://coreyms.com/category/development/javascript" itemprop="url"><span itemprop="name">JavaScript</span></a></li>
# # 	<li id="menu-item-1072" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-1072"><a href="https://coreyms.com/category/development/wordpress" itemprop="url"><span itemprop="name">WordPress</span></a></li>
# # </ul>
# # </li>
# # <li id="menu-item-125" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children menu-item-125"><a title="Design" href="https://coreyms.com/category/web-design" itemprop="url"><span itemprop="name">Design</span></a>
# # <ul class="sub-menu">
# # 	<li id="menu-item-801" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-801"><a title="CSS" href="https://coreyms.com/category/web-design/css" itemprop="url"><span itemprop="name">CSS</span></a></li>
# # </ul>
# # </li>
# # <li id="menu-item-804" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children menu-item-804"><a title="DIY" href="https://coreyms.com/category/diy" itemprop="url"><span itemprop="name">DIY</span></a>
# # <ul class="sub-menu">
# # 	<li id="menu-item-805" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-805"><a title="Woodworking" href="https://coreyms.com/category/diy/woodworking" itemprop="url"><span itemprop="name">Woodworking</span></a></li>
# # 	<li id="menu-item-806" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-806"><a title="Home Improvement" href="https://coreyms.com/category/diy/home-improvement" itemprop="url"><span itemprop="name">Home Improvement</span></a></li>
# # </ul>
# # </li>
# # <li id="menu-item-1154" class="right menu-item menu-item-type-post_type menu-item-object-page menu-item-1154"><a title="Contributors" href="https://coreyms.com/contributors" itemprop="url"><span itemprop="name">Contributors</span></a></li>
# # <li id="menu-item-898" class="right menu-item menu-item-type-post_type menu-item-object-page menu-item-898"><a title="Support" href="https://coreyms.com/support" itemprop="url"><span itemprop="name">Support</span></a></li>
# # <li id="menu-item-1260" class="right menu-item menu-item-type-post_type menu-item-object-page menu-item-1260"><a href="https://coreyms.com/giveaway" itemprop="url"><span itemprop="name">Giveaway</span></a></li>
# # </ul></div></nav><div class="site-inner"><div class="content-sidebar-wrap"><main class="content"><article class="post-1670 post type-post status-publish format-standard has-post-thumbnail category-development category-python tag-gzip tag-shutil tag-zip tag-zipfile entry" itemscope itemtype="https://schema.org/CreativeWork"><header class="entry-header"><h2 class="entry-title" itemprop="headline"><a class="entry-title-link" rel="bookmark" href="https://coreyms.com/development/python/python-tutorial-zip-files-creating-and-extracting-zip-archives">Python Tutorial: Zip Files &#8211; Creating and Extracting Zip Archives</a></h2>
# # <p class="entry-meta"><time class="entry-time" itemprop="datePublished" datetime="2019-11-19T13:02:37-05:00">November 19, 2019</time> by <span class="entry-author" itemprop="author" itemscope itemtype="https://schema.org/Person"><a href="https://coreyms.com/author/coreymschafer" class="entry-author-link" itemprop="url" rel="author"><span class="entry-author-name" itemprop="name">Corey Schafer</span></a></span> <span class="entry-comments-link"><a href="https://coreyms.com/development/python/python-tutorial-zip-files-creating-and-extracting-zip-archives#respond"><span class="dsq-postid" data-dsqidentifier="1670 http://coreyms.com/?p=1670">Leave a Comment</span></a></span> </p></header><div class="entry-content" itemprop="text">
# # <p>In this video, we will be learning how to create and extract zip archives. We will start by using the zipfile module, and then we will see how to do this using the shutil module. We will learn how to do this with single files and directories, as well as learning how to use gzip as well. Let&#8217;s get started…<br></p>
# #
# # <span class="embed-youtube" style="text-align:center; display: block;"><iframe class='youtube-player' type='text/html' width='640' height='360' src='https://www.youtube.com/embed/z0gguhEmWiY?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' allowfullscreen='true' style='border:0;'></iframe></span>
# # </div><footer class="entry-footer"><p class="entry-meta"><span class="entry-categories">Filed Under: <a href="https://coreyms.com/category/development" rel="category tag">Development</a>, <a href="https://coreyms.com/category/development/python" rel="category tag">Python</a></span> <span class="entry-tags">Tagged With: <a href="https://coreyms.com/tag/gzip" rel="tag">gzip</a>, <a href="https://coreyms.com/tag/shutil" rel="tag">shutil</a>, <a href="https://coreyms.com/tag/zip" rel="tag">zip</a>, <a href="https://coreyms.com/tag/zipfile" rel="tag">zipfile</a></span></p></footer></article><article class="post-1665 post type-post status-publish format-standard has-post-thumbnail category-development category-python tag-data-analysis tag-data-science tag-stack-overflow entry" itemscope itemtype="https://schema.org/CreativeWork"><header class="entry-header"><h2 class="entry-title" itemprop="headline"><a class="entry-title-link" rel="bookmark" href="https://coreyms.com/development/python/python-data-science-tutorial-analyzing-the-2019-stack-overflow-developer-survey">Python Data Science Tutorial: Analyzing the 2019 Stack Overflow Developer Survey</a></h2>
# # <p class="entry-meta"><time class="entry-time" itemprop="datePublished" datetime="2019-10-17T12:35:51-04:00">October 17, 2019</time> by <span class="entry-author" itemprop="author" itemscope itemtype="https://schema.org/Person"><a href="https://coreyms.com/author/coreymschafer" class="entry-author-link" itemprop="url" rel="author"><span class="entry-author-name" itemprop="name">Corey Schafer</span></a></span> <span class="entry-comments-link"><a href="https://coreyms.com/development/python/python-data-science-tutorial-analyzing-the-2019-stack-overflow-developer-survey#respond"><span class="dsq-postid" data-dsqidentifier="1665 http://coreyms.com/?p=1665">Leave a Comment</span></a></span> </p></header><div class="entry-content" itemprop="text">
# # <p>In this Python Programming video, we will be learning how to download and analyze real-world data from the 2019 Stack Overflow Developer Survey. This is terrific practice for anyone getting into the data science field. We will learn different ways to analyze this data and also some best practices. Let&#8217;s get started…</p>
# #
# #
# #
# # <figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
# # <span class="embed-youtube" style="text-align:center; display: block;"><iframe class='youtube-player' type='text/html' width='640' height='360' src='https://www.youtube.com/embed/_P7X8tMplsw?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' allowfullscreen='true' style='border:0;'></iframe></span>
# # </div></figure>
# # </div><footer class="entry-footer"><p class="entry-meta"><span class="entry-categories">Filed Under: <a href="https://coreyms.com/category/development" rel="category tag">Development</a>, <a href="https://coreyms.com/category/development/python" rel="category tag">Python</a></span> <span class="entry-tags">Tagged With: <a href="https://coreyms.com/tag/data-analysis" rel="tag">data analysis</a>, <a href="https://coreyms.com/tag/data-science" rel="tag">Data Science</a>, <a href="https://coreyms.com/tag/stack-overflow" rel="tag">stack overflow</a></span></p></footer></article><article class="post-1661 post type-post status-publish format-standard has-post-thumbnail category-development category-python tag-asynchronous tag-concurrent-futures tag-multiprocessing tag-parallel tag-threading entry" itemscope itemtype="https://schema.org/CreativeWork"><header class="entry-header"><h2 class="entry-title" itemprop="headline"><a class="entry-title-link" rel="bookmark" href="https://coreyms.com/development/python/python-multiprocessing-tutorial-run-code-in-parallel-using-the-multiprocessing-module">Python Multiprocessing Tutorial: Run Code in Parallel Using the Multiprocessing Module</a></h2>
# # <p class="entry-meta"><time class="entry-time" itemprop="datePublished" datetime="2019-09-21T10:59:18-04:00">September 21, 2019</time> by <span class="entry-author" itemprop="author" itemscope itemtype="https://schema.org/Person"><a href="https://coreyms.com/author/coreymschafer" class="entry-author-link" itemprop="url" rel="author"><span class="entry-author-name" itemprop="name">Corey Schafer</span></a></span> <span class="entry-comments-link"><a href="https://coreyms.com/development/python/python-multiprocessing-tutorial-run-code-in-parallel-using-the-multiprocessing-module#respond"><span class="dsq-postid" data-dsqidentifier="1661 http://coreyms.com/?p=1661">Leave a Comment</span></a></span> </p></header><div class="entry-content" itemprop="text">
# # <p>In this Python Programming video, we will be learning how to run code in parallel using the multiprocessing module. We will also look at how to process multiple high-resolution images at the same time using a ProcessPoolExecutor from the concurrent.futures module. Let&#8217;s get started…</p>
# #
# #
# #
# # <figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
# # <span class="embed-youtube" style="text-align:center; display: block;"><iframe class='youtube-player' type='text/html' width='640' height='360' src='https://www.youtube.com/embed/fKl2JW_qrso?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' allowfullscreen='true' style='border:0;'></iframe></span>
# # </div></figure>
# # </div><footer class="entry-footer"><p class="entry-meta"><span class="entry-categories">Filed Under: <a href="https://coreyms.com/category/development" rel="category tag">Development</a>, <a href="https://coreyms.com/category/development/python" rel="category tag">Python</a></span> <span class="entry-tags">Tagged With: <a href="https://coreyms.com/tag/asynchronous" rel="tag">asynchronous</a>, <a href="https://coreyms.com/tag/concurrent-futures" rel="tag">concurrent.futures</a>, <a href="https://coreyms.com/tag/multiprocessing" rel="tag">multiprocessing</a>, <a href="https://coreyms.com/tag/parallel" rel="tag">parallel</a>, <a href="https://coreyms.com/tag/threading" rel="tag">threading</a></span></p></footer></article><article class="post-1658 post type-post status-publish format-standard has-post-thumbnail category-development category-python tag-asynchronous tag-concurrency tag-multiprocessing tag-threading entry" itemscope itemtype="https://schema.org/CreativeWork"><header class="entry-header"><h2 class="entry-title" itemprop="headline"><a class="entry-title-link" rel="bookmark" href="https://coreyms.com/development/python/python-threading-tutorial-run-code-concurrently-using-the-threading-module">Python Threading Tutorial: Run Code Concurrently Using the Threading Module</a></h2>
# # <p class="entry-meta"><time class="entry-time" itemprop="datePublished" datetime="2019-09-12T10:49:54-04:00">September 12, 2019</time> by <span class="entry-author" itemprop="author" itemscope itemtype="https://schema.org/Person"><a href="https://coreyms.com/author/coreymschafer" class="entry-author-link" itemprop="url" rel="author"><span class="entry-author-name" itemprop="name">Corey Schafer</span></a></span> <span class="entry-comments-link"><a href="https://coreyms.com/development/python/python-threading-tutorial-run-code-concurrently-using-the-threading-module#respond"><span class="dsq-postid" data-dsqidentifier="1658 http://coreyms.com/?p=1658">Leave a Comment</span></a></span> </p></header><div class="entry-content" itemprop="text">
# # <p>In this Python Programming video, we will be learning how to run threads concurrently using the threading module. We will also look at how to download multiple high-resolution images online using a ThreadPoolExecutor from the concurrent.futures module. Let&#8217;s get started…</p>
# #
# #
# #
# # <figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
# # <span class="embed-youtube" style="text-align:center; display: block;"><iframe class='youtube-player' type='text/html' width='640' height='360' src='https://www.youtube.com/embed/IEEhzQoKtQU?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' allowfullscreen='true' style='border:0;'></iframe></span>
# # </div></figure>
# # </div><footer class="entry-footer"><p class="entry-meta"><span class="entry-categories">Filed Under: <a href="https://coreyms.com/category/development" rel="category tag">Development</a>, <a href="https://coreyms.com/category/development/python" rel="category tag">Python</a></span> <span class="entry-tags">Tagged With: <a href="https://coreyms.com/tag/asynchronous" rel="tag">asynchronous</a>, <a href="https://coreyms.com/tag/concurrency" rel="tag">concurrency</a>, <a href="https://coreyms.com/tag/multiprocessing" rel="tag">multiprocessing</a>, <a href="https://coreyms.com/tag/threading" rel="tag">threading</a></span></p></footer></article><article class="post-1655 post type-post status-publish format-standard category-general entry" itemscope itemtype="https://schema.org/CreativeWork"><header class="entry-header"><h2 class="entry-title" itemprop="headline"><a class="entry-title-link" rel="bookmark" href="https://coreyms.com/general/update-2019-09-03">Update (2019-09-03)</a></h2>
# # <p class="entry-meta"><time class="entry-time" itemprop="datePublished" datetime="2019-09-03T16:42:01-04:00">September 3, 2019</time> by <span class="entry-author" itemprop="author" itemscope itemtype="https://schema.org/Person"><a href="https://coreyms.com/author/coreymschafer" class="entry-author-link" itemprop="url" rel="author"><span class="entry-author-name" itemprop="name">Corey Schafer</span></a></span> <span class="entry-comments-link"><a href="https://coreyms.com/general/update-2019-09-03#respond"><span class="dsq-postid" data-dsqidentifier="1655 http://coreyms.com/?p=1655">Leave a Comment</span></a></span> </p></header><div class="entry-content" itemprop="text">
# # <p>Hey everyone. I wanted to give you an update on my videos. I will be releasing videos on threading and multiprocessing within the next week. Thanks so much for your patience. I currently have a temporary recording studio setup at my Airbnb that will allow me to record and edit the threading/multiprocessing videos. I am going to be moving into my new house in 10 days and once I have my recording studio setup then you can expect much faster video releases. I really appreciate how patient everyone has been while I go through this move, especially those of you who are contributing monthly through YouTube </p>
# # </div><footer class="entry-footer"><p class="entry-meta"><span class="entry-categories">Filed Under: <a href="https://coreyms.com/category/general" rel="category tag">General</a></span> </p></footer></article><article class="post-1651 post type-post status-publish format-standard has-post-thumbnail category-development category-python tag-vs-is tag-equality tag-identity entry" itemscope itemtype="https://schema.org/CreativeWork"><header class="entry-header"><h2 class="entry-title" itemprop="headline"><a class="entry-title-link" rel="bookmark" href="https://coreyms.com/development/python/python-quick-tip-the-difference-between-and-is-equality-vs-identity">Python Quick Tip: The Difference Between &#8220;==&#8221; and &#8220;is&#8221; (Equality vs Identity)</a></h2>
# # <p class="entry-meta"><time class="entry-time" itemprop="datePublished" datetime="2019-08-06T12:17:28-04:00">August 6, 2019</time> by <span class="entry-author" itemprop="author" itemscope itemtype="https://schema.org/Person"><a href="https://coreyms.com/author/coreymschafer" class="entry-author-link" itemprop="url" rel="author"><span class="entry-author-name" itemprop="name">Corey Schafer</span></a></span> <span class="entry-comments-link"><a href="https://coreyms.com/development/python/python-quick-tip-the-difference-between-and-is-equality-vs-identity#respond"><span class="dsq-postid" data-dsqidentifier="1651 http://coreyms.com/?p=1651">Leave a Comment</span></a></span> </p></header><div class="entry-content" itemprop="text">
# # <p>In this Python Programming Tutorial, we will be learning the difference between using &#8220;==&#8221; and the &#8220;is&#8221; keyword when doing comparisons. The difference between these is that &#8220;==&#8221; checks to see if values are equal, and the &#8220;is&#8221; keyword checks their identity, which means it&#8217;s going to check if the values are identical in terms of being the same object in memory. We&#8217;ll learn more in the video. Let&#8217;s get started&#8230;</p>
# #
# #
# #
# # <figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
# # <span class="embed-youtube" style="text-align:center; display: block;"><iframe class='youtube-player' type='text/html' width='640' height='360' src='https://www.youtube.com/embed/mO_dS3rXDIs?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' allowfullscreen='true' style='border:0;'></iframe></span>
# # </div></figure>
# # </div><footer class="entry-footer"><p class="entry-meta"><span class="entry-categories">Filed Under: <a href="https://coreyms.com/category/development" rel="category tag">Development</a>, <a href="https://coreyms.com/category/development/python" rel="category tag">Python</a></span> <span class="entry-tags">Tagged With: <a href="https://coreyms.com/tag/vs-is" rel="tag">== vs is</a>, <a href="https://coreyms.com/tag/equality" rel="tag">equality</a>, <a href="https://coreyms.com/tag/identity" rel="tag">identity</a></span></p></footer></article><article class="post-1647 post type-post status-publish format-standard has-post-thumbnail category-development category-python tag-standard-library tag-subprocess entry" itemscope itemtype="https://schema.org/CreativeWork"><header class="entry-header"><h2 class="entry-title" itemprop="headline"><a class="entry-title-link" rel="bookmark" href="https://coreyms.com/development/python/python-tutorial-calling-external-commands-using-the-subprocess-module">Python Tutorial: Calling External Commands Using the Subprocess Module</a></h2>
# # <p class="entry-meta"><time class="entry-time" itemprop="datePublished" datetime="2019-07-24T15:26:19-04:00">July 24, 2019</time> by <span class="entry-author" itemprop="author" itemscope itemtype="https://schema.org/Person"><a href="https://coreyms.com/author/coreymschafer" class="entry-author-link" itemprop="url" rel="author"><span class="entry-author-name" itemprop="name">Corey Schafer</span></a></span> <span class="entry-comments-link"><a href="https://coreyms.com/development/python/python-tutorial-calling-external-commands-using-the-subprocess-module#respond"><span class="dsq-postid" data-dsqidentifier="1647 http://coreyms.com/?p=1647">Leave a Comment</span></a></span> </p></header><div class="entry-content" itemprop="text">
# # <p>In this Python Programming Tutorial, we will be learning how to run external commands using the subprocess module from the standard library. We will learn how to run commands, capture the output, handle errors, and also how to pipe output into other commands. Let&#8217;s get started…</p>
# #
# #
# #
# # <figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
# # <span class="embed-youtube" style="text-align:center; display: block;"><iframe class='youtube-player' type='text/html' width='640' height='360' src='https://www.youtube.com/embed/2Fp1N6dof0Y?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' allowfullscreen='true' style='border:0;'></iframe></span>
# # </div></figure>
# # </div><footer class="entry-footer"><p class="entry-meta"><span class="entry-categories">Filed Under: <a href="https://coreyms.com/category/development" rel="category tag">Development</a>, <a href="https://coreyms.com/category/development/python" rel="category tag">Python</a></span> <span class="entry-tags">Tagged With: <a href="https://coreyms.com/tag/standard-library" rel="tag">standard library</a>, <a href="https://coreyms.com/tag/subprocess" rel="tag">subprocess</a></span></p></footer></article><article class="post-1642 post type-post status-publish format-standard has-post-thumbnail category-development category-python tag-development-environment tag-visual-studio-code tag-visual-studios tag-vs-code tag-vscode entry" itemscope itemtype="https://schema.org/CreativeWork"><header class="entry-header"><h2 class="entry-title" itemprop="headline"><a class="entry-title-link" rel="bookmark" href="https://coreyms.com/development/python/visual-studio-code-windows-setting-up-a-python-development-environment-and-complete-overview">Visual Studio Code (Windows) &#8211; Setting up a Python Development Environment and Complete Overview</a></h2>
# # <p class="entry-meta"><time class="entry-time" itemprop="datePublished" datetime="2019-05-01T14:03:24-04:00">May 1, 2019</time> by <span class="entry-author" itemprop="author" itemscope itemtype="https://schema.org/Person"><a href="https://coreyms.com/author/coreymschafer" class="entry-author-link" itemprop="url" rel="author"><span class="entry-author-name" itemprop="name">Corey Schafer</span></a></span> <span class="entry-comments-link"><a href="https://coreyms.com/development/python/visual-studio-code-windows-setting-up-a-python-development-environment-and-complete-overview#respond"><span class="dsq-postid" data-dsqidentifier="1642 http://coreyms.com/?p=1642">Leave a Comment</span></a></span> </p></header><div class="entry-content" itemprop="text">
# # <p>In this Python Programming Tutorial, we will be learning how to set up a Python development environment in VSCode on Windows. VSCode is a very nice free editor for writing Python applications and many developers are now switching over to this editor. In this video, we will learn how to install VSCode, get the Python extension installed, how to change Python interpreters, create virtual environments, format/lint our code, how to use Git within VSCode, how to debug our programs, how unit testing works, and more. We have a lot to cover, so let&#8217;s go ahead and get started…</p>
# #
# #
# #
# # <p>VSCode on MacOS &#8211; https://youtu.be/06I63_p-2A4</p>
# #
# #
# #
# # <p>Timestamps for topics in this tutorial:<br> Installation &#8211; 1:13<br> Python Extension &#8211; 5:48<br> Switching Interpreters &#8211; 10:04<br> Changing Color Themes &#8211; 12:35<br> VSCode Settings &#8211; 16:16<br> Set Default Python &#8211; 21:33<br> Using Virtual Environments &#8211; 25:10<br> IntelliSense &#8211; 29:45<br> Code Formatting &#8211; 32:13<br> Code Linting &#8211; 37:06<br> Code Runner Extension &#8211; 39:42<br> Git Integration &#8211; 47:44<br> Use Different Terminal &#8211; 51:07<br> Debugging &#8211; 58:45<br> Unit Testing &#8211; 1:03:25<br> Zen Mode &#8211; 1:09:55</p>
# #
# #
# #
# # <figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
# # <span class="embed-youtube" style="text-align:center; display: block;"><iframe class='youtube-player' type='text/html' width='640' height='360' src='https://www.youtube.com/embed/-nh9rCzPJ20?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' allowfullscreen='true' style='border:0;'></iframe></span>
# # </div></figure>
# # </div><footer class="entry-footer"><p class="entry-meta"><span class="entry-categories">Filed Under: <a href="https://coreyms.com/category/development" rel="category tag">Development</a>, <a href="https://coreyms.com/category/development/python" rel="category tag">Python</a></span> <span class="entry-tags">Tagged With: <a href="https://coreyms.com/tag/development-environment" rel="tag">Development Environment</a>, <a href="https://coreyms.com/tag/visual-studio-code" rel="tag">visual studio code</a>, <a href="https://coreyms.com/tag/visual-studios" rel="tag">visual studios</a>, <a href="https://coreyms.com/tag/vs-code" rel="tag">vs code</a>, <a href="https://coreyms.com/tag/vscode" rel="tag">vscode</a></span></p></footer></article><article class="post-1639 post type-post status-publish format-standard has-post-thumbnail category-development category-python tag-development-environment tag-visual-studio-code tag-visual-studios tag-vs-code tag-vscode entry" itemscope itemtype="https://schema.org/CreativeWork"><header class="entry-header"><h2 class="entry-title" itemprop="headline"><a class="entry-title-link" rel="bookmark" href="https://coreyms.com/development/python/visual-studio-code-mac-setting-up-a-python-development-environment-and-complete-overview">Visual Studio Code (Mac) &#8211; Setting up a Python Development Environment and Complete Overview</a></h2>
# # <p class="entry-meta"><time class="entry-time" itemprop="datePublished" datetime="2019-05-01T14:01:45-04:00">May 1, 2019</time> by <span class="entry-author" itemprop="author" itemscope itemtype="https://schema.org/Person"><a href="https://coreyms.com/author/coreymschafer" class="entry-author-link" itemprop="url" rel="author"><span class="entry-author-name" itemprop="name">Corey Schafer</span></a></span> <span class="entry-comments-link"><a href="https://coreyms.com/development/python/visual-studio-code-mac-setting-up-a-python-development-environment-and-complete-overview#respond"><span class="dsq-postid" data-dsqidentifier="1639 http://coreyms.com/?p=1639">Leave a Comment</span></a></span> </p></header><div class="entry-content" itemprop="text">
# # <p>In this Python Programming Tutorial, we will be learning how to set up a Python development environment in VSCode on MacOS. VSCode is a very nice free editor for writing Python applications and many developers are now switching over to this editor. In this video, we will learn how to install VSCode, get the Python extension installed, how to change Python interpreters, create virtual environments, format/lint our code, how to use Git within VSCode, how to debug our programs, how unit testing works, and more. We have a lot to cover, so let&#8217;s go ahead and get started…</p>
# #
# #
# #
# # <p>VSCode on Windows &#8211; https://youtu.be/-nh9rCzPJ20</p>
# #
# #
# #
# # <p>Timestamps for topics in this tutorial:<br> Installation &#8211; 1:11<br> Python Extension &#8211; 6:21<br> Switching Interpreters &#8211; 10:16<br> Changing Color Themes &#8211; 13:08<br> VSCode Settings &#8211; 17:12<br> Set Default Python &#8211; 22:24<br> Using Virtual Environments &#8211; 25:52<br> IntelliSense &#8211; 30:28<br> Code Formatting &#8211; 33:08<br> Code Linting &#8211; 38:01<br> Code Runner Extension &#8211; 40:45<br> Git Integration &#8211; 49:05<br> Debugging &#8211; 58:15<br> Unit Testing &#8211; 1:02:38<br> Zen Mode &#8211; 1:10:42 </p>
# #
# #
# #
# # <figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
# # <span class="embed-youtube" style="text-align:center; display: block;"><iframe class='youtube-player' type='text/html' width='640' height='360' src='https://www.youtube.com/embed/06I63_p-2A4?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' allowfullscreen='true' style='border:0;'></iframe></span>
# # </div></figure>
# # </div><footer class="entry-footer"><p class="entry-meta"><span class="entry-categories">Filed Under: <a href="https://coreyms.com/category/development" rel="category tag">Development</a>, <a href="https://coreyms.com/category/development/python" rel="category tag">Python</a></span> <span class="entry-tags">Tagged With: <a href="https://coreyms.com/tag/development-environment" rel="tag">Development Environment</a>, <a href="https://coreyms.com/tag/visual-studio-code" rel="tag">visual studio code</a>, <a href="https://coreyms.com/tag/visual-studios" rel="tag">visual studios</a>, <a href="https://coreyms.com/tag/vs-code" rel="tag">vs code</a>, <a href="https://coreyms.com/tag/vscode" rel="tag">vscode</a></span></p></footer></article><article class="post-1634 post type-post status-publish format-standard has-post-thumbnail category-development category-python tag-common-errors tag-common-mistakes tag-functions tag-mutable-default-arguments entry" itemscope itemtype="https://schema.org/CreativeWork"><header class="entry-header"><h2 class="entry-title" itemprop="headline"><a class="entry-title-link" rel="bookmark" href="https://coreyms.com/development/python/clarifying-the-issues-with-mutable-default-arguments">Clarifying the Issues with Mutable Default Arguments</a></h2>
# # <p class="entry-meta"><time class="entry-time" itemprop="datePublished" datetime="2019-04-24T11:46:42-04:00">April 24, 2019</time> by <span class="entry-author" itemprop="author" itemscope itemtype="https://schema.org/Person"><a href="https://coreyms.com/author/coreymschafer" class="entry-author-link" itemprop="url" rel="author"><span class="entry-author-name" itemprop="name">Corey Schafer</span></a></span> <span class="entry-comments-link"><a href="https://coreyms.com/development/python/clarifying-the-issues-with-mutable-default-arguments#respond"><span class="dsq-postid" data-dsqidentifier="1634 http://coreyms.com/?p=1634">Leave a Comment</span></a></span> </p></header><div class="entry-content" itemprop="text">
# # <p>In this Python Programming Tutorial, we will be clarifying the issues with mutable default arguments. We discussed this in my last video titled &#8220;5 Common Python Mistakes and How to Fix Them&#8221;, but I received many comments from people who were still confused. So we will be doing a deeper dive to explain exactly what is going on here. Let&#8217;s get started…</p>
# #
# #
# #
# # <figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
# # <span class="embed-youtube" style="text-align:center; display: block;"><iframe class='youtube-player' type='text/html' width='640' height='360' src='https://www.youtube.com/embed/_JGmemuINww?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' allowfullscreen='true' style='border:0;'></iframe></span>
# # </div></figure>
# # </div><footer class="entry-footer"><p class="entry-meta"><span class="entry-categories">Filed Under: <a href="https://coreyms.com/category/development" rel="category tag">Development</a>, <a href="https://coreyms.com/category/development/python" rel="category tag">Python</a></span> <span class="entry-tags">Tagged With: <a href="https://coreyms.com/tag/common-errors" rel="tag">common errors</a>, <a href="https://coreyms.com/tag/common-mistakes" rel="tag">common mistakes</a>, <a href="https://coreyms.com/tag/functions" rel="tag">functions</a>, <a href="https://coreyms.com/tag/mutable-default-arguments" rel="tag">mutable default arguments</a></span></p></footer></article><div class="archive-pagination pagination"><ul><li class="active" ><a href="https://coreyms.com/" aria-label="Current page" aria-current="page">1</a></li>
# # <li><a href="https://coreyms.com/page/2">2</a></li>
# # <li><a href="https://coreyms.com/page/3">3</a></li>
# # <li class="pagination-omission">&#x02026;</li>
# # <li><a href="https://coreyms.com/page/17">17</a></li>
# # <li class="pagination-next"><a href="https://coreyms.com/page/2" >Next Page &#x000BB;</a></li>
# # </ul></div>
# # </main><aside class="sidebar sidebar-primary widget-area" role="complementary" aria-label="Primary Sidebar" itemscope itemtype="https://schema.org/WPSideBar"><section id="text-5" class="widget widget_text"><div class="widget-wrap"><h4 class="widget-title widgettitle">Main Contributor</h4>
# # 			<div class="textwidget"><ul>
# # <li><b>Andre Nevares</b></li>
# # </ul>
# # <h4 style="margin-top: 25px; font-size: 17px;">Top Contributors (17)</h4>
# # <ul>
# # <li>Andre Nevares</li>
# # <li>Cyril Hediger</li>
# # <li>Abhilash Rajan</li>
# # <li>Hien Nguyen</li>
# # <li>Alan Hawse &#8211; iotexpert.com</li>
# # <li>Just a Guy</li>
# # <li>Alex Canady</li>
# # <li>Sergey Trubin</li>
# # <li>Justin Presley</li>
# # <li>Sirake </li>
# # <li>chris </li>
# # <li>Jerome Massey</li>
# # <li>Robert Butler</li>
# # <li>Jonathan Llovet</li>
# # <li>David Myers</li>
# # <li>Karthik </li>
# # <li>Michael Zoitas</li>
# # </ul>
# # <hr style="border: 0; border-bottom: 1px dotted #ddd;" />
# # <p><b>Thank You!</b> If you would like to have your name listed as a contributor and support the website, you can do so through <a href="https://www.patreon.com/coreyms" target="_blank" rel="noopener noreferrer">my Patreon Page</a>. I am extremely grateful for any support.</p>
# # </div>
# # 		</div></section>
# # <section id="search-3" class="widget widget_search"><div class="widget-wrap"><h4 class="widget-title widgettitle">Search CoreyMS.com</h4>
# # <form class="search-form" itemprop="potentialAction" itemscope itemtype="https://schema.org/SearchAction" method="get" action="https://coreyms.com/" role="search"><input class="search-form-input" type="search" itemprop="query-input" name="s" id="searchform-5e4a2be1502e86.57845115" placeholder="Search this website"><input class="search-form-submit" type="submit" value="Search"><meta itemprop="target" content="https://coreyms.com/?s={s}"></form></div></section>
# # <section id="enews-ext-4" class="widget enews-widget"><div class="widget-wrap"><div class="enews"><h4 class="widget-title widgettitle">Subscribe to Future Posts</h4>
# # 			<form id="subscribeenews-ext-4" action="//coreyms.us9.list-manage.com/subscribe/post?u=f4df8a0f0be5d3754ed52b1ef&amp;id=5b06358625" method="post"
# # 																			target="_blank" onsubmit="if ( subbox1.value == 'First Name') { subbox1.value = ''; } if ( subbox2.value == 'Last Name') { subbox2.value = ''; }" name="enews-ext-4">
# # 				<label for="subbox1" class="screenread">First Name</label><input type="text" id="subbox1" class="enews-subbox" value="" placeholder="First Name" name="FNAME" />								<label for="subbox" class="screenread">E-Mail Address</label><input type="email" value="" id="subbox" placeholder="E-Mail Address" name="EMAIL"
# # 																														required="required" />
# # 								<input type="submit" value="Subscribe" id="subbutton" />
# # 			</form>
# # 		</div></div></section>
# # <section id="text-2" class="widget widget_text"><div class="widget-wrap"><h4 class="widget-title widgettitle">Recommended Books</h4>
# # 			<div class="textwidget"><a target="_blank" href="https://www.amazon.com/gp/product/1449355730/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1449355730&linkCode=as2&tag=coreyms-20&linkId=2f9ceaf471d7d35f2c2657051780fc6f" rel="noopener noreferrer"><img class="widget_book" border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=1449355730&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=coreyms-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=coreyms-20&l=am2&o=1&a=1449355730" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
# #
# # <a target="_blank" href="https://www.amazon.com/gp/product/1491946008/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1491946008&linkCode=as2&tag=coreyms-20&linkId=39335cdc340fb7ce5bd51d59c57e7e54" rel="noopener noreferrer"><img class="widget_book" border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=1491946008&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=coreyms-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=coreyms-20&l=am2&o=1&a=1491946008" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
# #
# # <a target="_blank" href="https://www.amazon.com/gp/product/1593276036/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1593276036&linkCode=as2&tag=coreyms-20&linkId=75ff844a147bc8cb5fb325608b286158" rel="noopener noreferrer"><img class="widget_book" border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=1593276036&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=coreyms-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=coreyms-20&l=am2&o=1&a=1593276036" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
# #
# # <a target="_blank" href="https://www.amazon.com/gp/product/0984782850/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0984782850&linkCode=as2&tag=coreyms-20&linkId=e2f7c21906426f17958a1d04718e7d02" rel="noopener noreferrer"><img class="widget_book" border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=0984782850&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=coreyms-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=coreyms-20&l=am2&o=1&a=0984782850" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
# #
# # <a target="_blank" href="https://www.amazon.com/gp/product/020161622X/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=020161622X&linkCode=as2&tag=coreyms-20&linkId=a2699f6b6cb5814da54f71140c52f2ca" rel="noopener noreferrer"><img class="widget_book" border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=020161622X&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=coreyms-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=coreyms-20&l=am2&o=1&a=020161622X" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
# #
# # <a target="_blank" href="https://www.amazon.com/gp/product/0201835959/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0201835959&linkCode=as2&tag=coreyms-20&linkId=c3de80ab4a4761f7634751cf323af13f" rel="noopener noreferrer"><img class="widget_book" border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=0201835959&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=coreyms-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=coreyms-20&l=am2&o=1&a=0201835959" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
# # </div>
# # 		</div></section>
# # <section id="text-3" class="widget widget_text"><div class="widget-wrap"><h4 class="widget-title widgettitle">Podcasts I Listen To</h4>
# # 			<div class="textwidget"><u>Tech Related</u>:<br>
# #
# # <a href="http://talkpython.fm/">Talk Python To Me</a>
# # <br>
# #
# # <a href="http://shoptalkshow.com/">Shoptalk Show</a>
# # <br>
# #
# # <a href="http://www.se-radio.net/">Software Engineering Radio</a>
# # <br>
# #
# # <a href="http://hanselminutes.com/">HanselMinutes</a>
# # <br>
# #
# # <a href="https://blog.codepen.io/radio/">CodePen Radio</a>
# # <br><br>
# #
# # <u>Non-Tech Related</u>:
# # <br>
# #
# # <a href="http://www.dancarlin.com/hardcore-history-series/">Dan Carlin's Hardcore History</a>
# # <br>
# #
# # <a href="http://www.billburr.com/podcast">Bill Burr's Monday Morning Podcast</a>
# # <br>
# #
# # <a href="http://www.samharris.org/podcast">Waking Up with Sam Harris</a>
# # <br>
# #
# # <a href="http://www.startalkradio.net/shows-archive/">StarTalk Radio</a>
# # <br>
# #
# # <a href="http://carasantamaria.com/podcast/">Talk Nerdy with Cara Santa Maria</a>
# # </div>
# # 		</div></section>
# # </aside></div></div><footer class="site-footer" itemscope itemtype="https://schema.org/WPFooter"><div class="wrap"><p>&#x000A9;&nbsp;2020 &middot; <a href="http://coreyms.com">CoreyMS</a> &middot; Corey Schafer</p></div></footer></div><link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/8.4/styles/zenburn.min.css">
# # <script src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/8.4/highlight.min.js"></script>
# # <script>hljs.initHighlightingOnLoad();</script><script type='text/javascript'>
# # /* <![CDATA[ */
# # var wpcf7 = {"apiSettings":{"root":"https:\/\/coreyms.com\/wp-json\/contact-form-7\/v1","namespace":"contact-form-7\/v1"},"cached":"1"};
# # /* ]]> */
# # </script>
# # <script src="https://coreyms.com/wp-content/cache/minify/0fef6.js"></script>
# #
# # <script type='text/javascript'>
# # /* <![CDATA[ */
# # var countVars = {"disqusShortname":"coreyms"};
# # /* ]]> */
# # </script>
# #
# #
# #
# #
# #
# #
# # <script src="https://coreyms.com/wp-content/cache/minify/9b739.js"></script>
# #
# # <script type='text/javascript' src='https://stats.wp.com/e-202008.js' async='async' defer='defer'></script>
# # <script type='text/javascript'>
# # 	_stq = window._stq || [];
# # 	_stq.push([ 'view', {v:'ext',j:'1:8.2',blog:'70676981',post:'0',tz:'-5',srv:'coreyms.com'} ]);
# # 	_stq.push([ 'clickTrackerInit', '70676981', '0' ]);
# # </script>
# # </body></html>
# #
# # <!--
# # Performance optimized by W3 Total Cache. Learn more: https://www.w3-edge.com/products/
# #
# # Page Caching using disk: enhanced (SSL caching disabled)
# # Minified using disk
# #
# # Served from: coreyms.com @ 2020-02-17 01:00:01 by W3 Total Cache
# # -->
#
# source = requests.get('http://coreyms.com').text
#
# soup = BeautifulSoup(source,'lxml')
# print (soup.prettify())
#
# o/p is -->
#
# /anaconda3/bin/python3.7m /Users/headshot/PycharmProjects/untitled10/beautiful.py
# <!DOCTYPE html>
# <html lang="en-US">
#  <head>
#   <meta charset="utf-8"/>
#   <meta content="width=device-width, initial-scale=1" name="viewport"/>
#   <title>
#    CoreyMS - Development, Design, DIY, and more
#   </title>
#   <!-- This site is optimized with the Yoast SEO plugin v13.0 - https://yoast.com/wordpress/plugins/seo/ -->
#   <meta content="Development, Design, DIY, and more" name="description"/>
#   <meta content="max-snippet:-1, max-image-preview:large, max-video-preview:-1" name="robots"/>
#   <link href="https://coreyms.com/" rel="canonical"/>
#   <link href="http://coreyms.com/page/2" rel="next"/>
#   <meta content="en_US" property="og:locale"/>
#   <meta content="website" property="og:type"/>
#   <meta content="CoreyMS - Development, Design, DIY, and more" property="og:title"/>
#   <meta content="Development, Design, DIY, and more" property="og:description"/>
#   <meta content="https://coreyms.com/" property="og:url"/>
#   <meta content="CoreyMS" property="og:site_name"/>
#   <meta content="https://coreyms.com/wp-content/uploads/2014/11/SocialIcon.png" property="og:image"/>
#   <meta content="https://coreyms.com/wp-content/uploads/2014/11/SocialIcon.png" property="og:image:secure_url"/>
#   <meta content="800" property="og:image:width"/>
#   <meta content="800" property="og:image:height"/>
#   <meta content="summary_large_image" name="twitter:card"/>
#   <meta content="Development, Design, DIY, and more" name="twitter:description"/>
#   <meta content="CoreyMS - Development, Design, DIY, and more" name="twitter:title"/>
#   <meta content="@CoreyMSchafer" name="twitter:site"/>
#   <meta content="http://coreyms.com/wp-content/uploads/2014/11/SocialIcon.png" name="twitter:image"/>
#   <meta content="69D01EB6520B2918B78685B21805C977" name="msvalidate.01"/>
#   <meta content="cWGcd5qKYyguo-9DC8wgwnOjN0_P9bBazUyRTtHohMU" name="google-site-verification"/>
#   <script class="yoast-schema-graph yoast-schema-graph--main" type="application/ld+json">
#    {"@context":"https://schema.org","@graph":[{"@type":"WebSite","@id":"https://coreyms.com/#website","url":"https://coreyms.com/","name":"CoreyMS","description":"Development, Design, DIY, and more","potentialAction":{"@type":"SearchAction","target":"https://coreyms.com/?s={search_term_string}","query-input":"required name=search_term_string"}},{"@type":"CollectionPage","@id":"https://coreyms.com/#webpage","url":"https://coreyms.com/","inLanguage":"en-US","name":"CoreyMS - Development, Design, DIY, and more","isPartOf":{"@id":"https://coreyms.com/#website"},"description":"Development, Design, DIY, and more"}]}
#   </script>
#   <!-- / Yoast SEO plugin. -->
#   <link href="//fonts.googleapis.com" rel="dns-prefetch"/>
#   <link href="//s.w.org" rel="dns-prefetch"/>
#   <link href="https://coreyms.com/feed" rel="alternate" title="CoreyMS » Feed" type="application/rss+xml"/>
#   <link href="https://coreyms.com/comments/feed" rel="alternate" title="CoreyMS » Comments Feed" type="application/rss+xml"/>
#   <script type="text/javascript">
#    window._wpemojiSettings = {"baseUrl":"https:\/\/s.w.org\/images\/core\/emoji\/12.0.0-1\/72x72\/","ext":".png","svgUrl":"https:\/\/s.w.org\/images\/core\/emoji\/12.0.0-1\/svg\/","svgExt":".svg","source":{"concatemoji":"https:\/\/coreyms.com\/wp-includes\/js\/wp-emoji-release.min.js?ver=5.3.2"}};
# 			!function(e,a,t){var r,n,o,i,p=a.createElement("canvas"),s=p.getContext&&p.getContext("2d");function c(e,t){var a=String.fromCharCode;s.clearRect(0,0,p.width,p.height),s.fillText(a.apply(this,e),0,0);var r=p.toDataURL();return s.clearRect(0,0,p.width,p.height),s.fillText(a.apply(this,t),0,0),r===p.toDataURL()}function l(e){if(!s||!s.fillText)return!1;switch(s.textBaseline="top",s.font="600 32px Arial",e){case"flag":return!c([127987,65039,8205,9895,65039],[127987,65039,8203,9895,65039])&&(!c([55356,56826,55356,56819],[55356,56826,8203,55356,56819])&&!c([55356,57332,56128,56423,56128,56418,56128,56421,56128,56430,56128,56423,56128,56447],[55356,57332,8203,56128,56423,8203,56128,56418,8203,56128,56421,8203,56128,56430,8203,56128,56423,8203,56128,56447]));case"emoji":return!c([55357,56424,55356,57342,8205,55358,56605,8205,55357,56424,55356,57340],[55357,56424,55356,57342,8203,55358,56605,8203,55357,56424,55356,57340])}return!1}function d(e){var t=a.createElement("script");t.src=e,t.defer=t.type="text/javascript",a.getElementsByTagName("head")[0].appendChild(t)}for(i=Array("flag","emoji"),t.supports={everything:!0,everythingExceptFlag:!0},o=0;o<i.length;o++)t.supports[i[o]]=l(i[o]),t.supports.everything=t.supports.everything&&t.supports[i[o]],"flag"!==i[o]&&(t.supports.everythingExceptFlag=t.supports.everythingExceptFlag&&t.supports[i[o]]);t.supports.everythingExceptFlag=t.supports.everythingExceptFlag&&!t.supports.flag,t.DOMReady=!1,t.readyCallback=function(){t.DOMReady=!0},t.supports.everything||(n=function(){t.readyCallback()},a.addEventListener?(a.addEventListener("DOMContentLoaded",n,!1),e.addEventListener("load",n,!1)):(e.attachEvent("onload",n),a.attachEvent("onreadystatechange",function(){"complete"===a.readyState&&t.readyCallback()})),(r=t.source||{}).concatemoji?d(r.concatemoji):r.wpemoji&&r.twemoji&&(d(r.twemoji),d(r.wpemoji)))}(window,document,window._wpemojiSettings);
#   </script>
#   <style type="text/css">
#    img.wp-smiley,
# img.emoji {
# 	display: inline !important;
# 	border: none !important;
# 	box-shadow: none !important;
# 	height: 1em !important;
# 	width: 1em !important;
# 	margin: 0 .07em !important;
# 	vertical-align: -0.1em !important;
# 	background: none !important;
# 	padding: 0 !important;
# }
#   </style>
#   <link href="https://coreyms.com/wp-content/cache/minify/119a3.css" media="all" rel="stylesheet"/>
#   <style id="wp-block-library-inline-css" type="text/css">
#    .has-text-align-justify{text-align:justify;}
#   </style>
#   <link href="https://coreyms.com/wp-content/cache/minify/4c431.css" media="all" rel="stylesheet"/>
#   <link href="//fonts.googleapis.com/css?family=Lato%3A300%2C400%2C700%7CVarela+Round&amp;ver=2.1.2" id="google-fonts-css" media="all" rel="stylesheet" type="text/css"/>
#   <link href="https://coreyms.com/wp-content/cache/minify/95173.css" media="all" rel="stylesheet"/>
#   <script src="https://coreyms.com/wp-content/cache/minify/df983.js">
#   </script>
#   <!--[if lt IE 9]>
# <script type='text/javascript' src='https://coreyms.com/wp-content/themes/genesis/lib/js/html5shiv.min.js?ver=3.7.3'></script>
# <![endif]-->
#   <link href="https://coreyms.com/wp-json/" rel="https://api.w.org/"/>
#   <link href="https://coreyms.com/xmlrpc.php?rsd" rel="EditURI" title="RSD" type="application/rsd+xml"/>
#   <link href="https://coreyms.com/wp-includes/wlwmanifest.xml" rel="wlwmanifest" type="application/wlwmanifest+xml"/>
#   <meta content="WordPress 5.3.2" name="generator"/>
#   <style type="text/css">
#    .enews .screenread {
# 	height: 1px;
#     left: -1000em;
#     overflow: hidden;
#     position: absolute;
#     top: -1000em;
#     width: 1px; }
#   </style>
#   <link href="//v0.wordpress.com" rel="dns-prefetch"/>
#   <link href="https://coreyms.com/xmlrpc.php" rel="pingback"/>
#   <link href="https://plus.google.com/+CoreySchafer44/posts" rel="author"/>
#   <link href="/apple-touch-icon-57x57.png" rel="apple-touch-icon" sizes="57x57"/>
#   <link href="/apple-touch-icon-114x114.png" rel="apple-touch-icon" sizes="114x114"/>
#   <link href="/apple-touch-icon-72x72.png" rel="apple-touch-icon" sizes="72x72"/>
#   <link href="/apple-touch-icon-144x144.png" rel="apple-touch-icon" sizes="144x144"/>
#   <link href="/apple-touch-icon-60x60.png" rel="apple-touch-icon" sizes="60x60"/>
#   <link href="/apple-touch-icon-120x120.png" rel="apple-touch-icon" sizes="120x120"/>
#   <link href="/apple-touch-icon-76x76.png" rel="apple-touch-icon" sizes="76x76"/>
#   <link href="/apple-touch-icon-152x152.png" rel="apple-touch-icon" sizes="152x152"/>
#   <link href="/apple-touch-icon-180x180.png" rel="apple-touch-icon" sizes="180x180"/>
#   <link href="/favicon-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
#   <link href="/favicon-160x160.png" rel="icon" sizes="160x160" type="image/png"/>
#   <link href="/favicon-96x96.png" rel="icon" sizes="96x96" type="image/png"/>
#   <link href="/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
#   <link href="/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
#   <meta content="#56616b" name="msapplication-TileColor"/>
#   <meta content="/mstile-144x144.png" name="msapplication-TileImage"/>
#   <script>
#    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
#   (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
#   m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
#   })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
#   ga('create', 'UA-53634311-1', 'auto');
#   ga('send', 'pageview');
#   </script>
#  </head>
#  <body class="home blog content-sidebar" itemscope="" itemtype="https://schema.org/WebPage">
#   <div class="site-container">
#    <header class="site-header" itemscope="" itemtype="https://schema.org/WPHeader">
#     <div class="wrap">
#      <div class="title-area">
#       <div class="site-avatar">
#        <a href="https://coreyms.com/">
#         <svg class="site-avatar-svg" enable-background="new 0 0 441.5 441.5" height="150px" id="Layer_1" version="1.1" viewbox="0 0 441.5 441.5" width="150px" x="0px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" y="0px">
#          <g class="site-avatar-background">
#           <path d="M79.178 390.133C30.781 349.639 0 288.789 0 220.75C0 98.833 98.833 0 220.75 0S441.5 98.833 441.5 220.75 c0 63.558-26.86 120.842-69.848 161.12" fill="#56616B">
#           </path>
#          </g>
#          <g class="site-avatar-foreground">
#           <path d="M254.602 182.291c0 1.992-0.097 4 0 6c0.057 0.88-0.093 1.952 0.194 2.78c0.22 0.631 0.69 1.12 1.704 1.273 c2.009 0.3 3.436-1.062 4.384-2.719c0.712-1.244 0.863-3.376 1.843-3.807c1.612-0.712 2.646-1.537 3.276-2.44 c1.903-2.732 0.09-6.185-0.723-9.42c-0.29-1.157-1.995-2.036-0.556-3.456c0.801-0.789 1.711-0.981 2.717-0.718 c0.164 0.043 0.33 0.095 0.5 0.162c0.262 0.104 0.505 0.185 0.732 0.249c3.521 0.99 3.182-2.499 3.459-4.337 c0.262-1.728 0.411-3.561-0.128-5.161c-0.413-1.229-1.231-2.321-2.721-3.124c-0.345-0.187-1.271 0.296-1.683 0.7 C260.971 165 252.55 170.8 254.65 182.291H254.602z" fill="#E3E0DD">
#           </path>
#           <path d="M121.076 185.062c-0.633 2.075-1.555 4.107-1.326 6.3c1.215 11.7 4.9 22.7 10.4 32.958 c1.692 3.201 3.6 6.4 6.3 8.931c6.878 6.299 15.1 11.5 18.3 21.101c0.697 2.1 2.7 3.799 4.1 5.616c0.797 1.101 7.7 7.5 9.9 9.06 c5.75 4 12.2 2.399 18.3 2.701c3.969 0.19 7.635-0.422 10.23-2.799c1.496-1.371 2.638-3.322 3.271-6.056 c0.378-1.636 1.506-3.308 2.812-4.621c0.372-0.374 0.756-0.724 1.144-1.028c0.236-0.187 0.452-0.393 0.683-0.584 c2.745-2.268 5.197-4.824 7.772-7.193c0.196-0.182 0.395-0.361 0.593-0.541c0.263-0.235 0.516-0.484 0.783-0.715 c2.067-1.778 3.228-4.668 5.456-6.357c0.991-0.751 2.192-1.268 3.781-1.339c4.19-0.188 7.815-1.231 10.56-3.522 c2.112-1.764 3.703-4.267 4.627-7.693c0.437-1.615 2.252-2.815 3.221-4.342c1.367-2.154 1.631-5.814-0.541-5.996 c-5.594-0.462-3.601-4.181-3.784-6.851c-0.224-3.178 0.817-6.237 1.688-9.293c2.23-7.859 2.068-15.447-2.718-22.497 c-1.593-2.346-2.862-4.882-3.588-7.658c-0.304-1.159-0.571-2.27 0.562-2.565c0.258-0.067 0.584-0.093 1.002-0.067 c0.979 0.081 2.138 1.205 2.97 0.79c0.196-0.099 0.377-0.282 0.53-0.589c0.812-1.632-0.619-3.176-1.769-4.355 c-1.974-2.029-2.121-3.545 0.03-5.829c4.014-4.26 2.55-9.908-3.036-11.764c-3.315-1.103-5.812-2.844-8.128-5.404 c-3.221-3.559-7.302-6.113-12.188-4.117c-0.077 0.031-0.152 0.054-0.229 0.087c-4.316 1.881-8.25 4.641-12.839 7.3 c5.969 2.5 11.4 4 17.4 3.326c4.219-0.484 7.9 0.8 10.7 4.1c1.021 1.2 1.1 2.8 0.1 4.197c-0.256 0.386-0.549 0.657-0.873 0.774 c-0.367 0.132-0.774 0.069-1.225-0.274c-4.875-3.503-10.354-1.259-15.552-1.665c-1.768-0.138-4.002 0.686-5.052-1.229 c-0.998-1.819-2.014-2.475-3.065-2.466c-1.199 0.009-2.443 0.886-3.757 1.931c-0.647 0.515-1.219 1.372-2.061 1.577 c-0.304 0.074-0.642 0.067-1.033-0.077c-0.107-2.153 2.641-2.457 2.183-4.465c-2.788-0.657-5.483-0.628-8.281 0.466 c-0.928 0.363-1.869 0.849-2.827 1.464c-0.095 0.061-0.188 0.107-0.283 0.17c0.945-3.138 5.419-5.098 0.606-7.558 c-0.949-0.485 0.189-1.66 1.02-2.292c1.043-0.794 2.321-1.519 2.936-2.594c1.521-2.665 3.594-4.347 5.997-5.363 c1.868-0.791 3.936-1.18 6.098-1.316c4.041-0.255 7.759-1.711 11.647-2.479c0.852-0.168 1.606-0.458 2.265-0.854 c1.858-1.119 2.911-3.136 2.915-6.033c0.009-6.685-2.918-12.743-3.582-19.266c-0.12-1.184-1.234-3.36-3.023-2.574 c-3.523 1.548-5.289-0.921-6.55-2.962c-1.631-2.64-3.149-2.745-4.879-1.815c-0.514 0.276-1.045 0.64-1.605 1.06 c-1.044 0.784-1.544 2.183-2.749 2.872c-0.285 0.163-0.596 0.298-0.977 0.362c-0.388-1.862 1.36-2.985 1.44-4.602 c0.051-1.008-0.054-2.516-1.327-1.745c-0.018 0.011-0.031 0.012-0.05 0.024c-0.144 0.092-0.273 0.166-0.403 0.24 c-2.564 1.457-2.537-0.535-2.866-2.284c-0.325-1.727-1.001-3.345-2.837-3.741c-0.406-0.087-0.729-0.082-0.991-0.007 c-1.147 0.325-1.128 1.968-1.773 2.907c-1.611 2.263-3.115 4.664-6.599 7.237c-0.113 0.083-0.21 0.166-0.328 0.25 c2.371-4.847 3.656-8.487 0.458-12.642c-0.07-0.09-0.129-0.18-0.203-0.271c-0.833 4.386-1.515 8.2-4.973 10.605 c-0.093 0.064-0.18 0.133-0.277 0.195c-1.097-1.5 0.22-3.408-1.72-4.438c-0.012-0.006-0.021-0.014-0.032-0.02 c-0.35 0.452-0.84 0.881-1.076 1.4c-1.153 2.642-1.673 3.754-2.146 4.263c-0.381 0.41-0.731 0.431-1.355 0.537 c-3.99 0.632-4.702-1.837-5.834-4.938c-2.642-7.239-9.918-10.402-14.395-6.815c-0.378 0.303-0.743 0.637-1.077 1.039 c-2.435 2.929-4.771 6.612-5.835 10c-1.345 4.336-3.751 6.76-7.148 8.956c-5.305 3.428-8.463 7.855-7.026 14.6 c0.539 2.542-0.675 4.875-1.846 7.1c-1.875 3.597-0.992 5.7 3.3 5.997c1.991 0.1 4 0.5 6 0.553c4.777 0.2 8.7 1.7 12.6 5 c3.784 3.3 6.8 7.3 10.6 10.378c3.999 3.3 5.2 6.9 4.6 11.811c-0.675 6.117-1.21 12.273-1.305 18.4 c-0.06 3.896-0.854 6.795-4.75 8.389c-1.934 0.791-3.424 2.349-2.862 4.699c0.609 2.5 2.7 3.2 5 3.1 c0.5-0.016 1.015-0.126 1.496-0.042c2.554 0.4 5.5 0.6 2.8 4.468c-0.756 1.058-0.791 2.3 0.8 2.8c1.242 0.4 3 0.2 2.5 2.2 c-0.369 1.521-2.162 1.237-3.3 1.809c-0.792 0.397-1.632 0.577-2.505 0.667c-1.329 0.138-2.731 0.069-4.149 0.233 c-1.444 0.167-2.903 0.575-4.315 1.699c0.827 0.264 1.74 0.504 2.708 0.726c8.333 1.914 20.87 2.433 20.086 3.987 c-0.007 0.015-0.021 0.03-0.031 0.045c-0.02 0.031-0.033 0.061-0.063 0.092h0.009v0.051c-4.351 0.46-8.029 1.064-12.392 1.2 c-1.847 0.066-3.692-0.031-4.682 1.264c-0.246 0.323-0.441 0.728-0.568 1.247c-0.572 2.399 1.2 4.101 2.9 5.399 c1.688 1.302 3.7 2.302 5.3 3.7c2.363 1.9 1.9 4.699 0.9 6.913c-0.278 0.625-0.608 0.995-0.969 1.202 c-1.229 0.705-2.845-0.562-4.213-0.901c-3.906-1.047-5.531-4.397-7.769-7.324c-4.868-6.364-7.044-12.982-16.966-15.704 c-0.459-0.125-0.913-0.253-1.406-0.362c-1.632-0.36-1.601-0.026-1.583-2c0.017-1.846 4.917-0.833 6.5-1.333 c5.514-1.741 5.65-2.834 10.5-4.167c3.46-0.951 2.169-6.663 1.322-10.273c-0.003-0.014-0.007-0.029-0.01-0.043 c-0.104-0.441-0.179-0.878-0.232-1.312c-0.361-2.919 0.352-5.695 1.408-8.45c6.845-10.339 3.558-20.753 4.884-23.425 c0.777-1.565 1.148-2.989 1.094-4.267c-0.092-2.177-1.423-3.929-4.123-5.227c-7.634-3.67-15.45-6.876-23.707-8.9 c-1.792-0.439-3.357-0.107-4.359 1.482c-0.006 0.009-0.013 0.016-0.019 0.025c-1.01 1.628-1.361 3.475-0.355 5.2 c0.944 1.6 2.6 1 4 1c5.133-0.093 10.274-0.174 15.4 0.045c3.086 0.1 3.9 1.8 2.4 4.722c-0.343 0.664-0.82 1.233-1.384 1.709 c-2.594 2.19-7.13 2.328-10.065-0.209c-0.722-0.629-1.141-1.751-2.391-1.317c-0.15 0.052-0.262 0.125-0.365 0.204 c-0.378 0.292-0.477 0.754-0.492 1.357c-0.035 1.376-0.479 2.212-1.139 2.757c-1.51 1.246-4.167 0.963-5.775 2.043 c-1.373 0.908-3.125-1.413-3.536-3.282c-0.312-1.417-0.514-2.734-2.291-2.62c-0.586 0.038-1.049 0.236-1.412 0.534 c-0.625 0.514-0.948 1.329-1.06 2.166c-0.39 2.976-0.977 6.3 0.9 8.741C123.411 174.752 122.676 179.853 121.076 185.062z M211.68 211.557c0.16-0.005 0.319-0.011 0.479-0.017c0.196-0.006 0.401-0.005 0.61 0c1.39 0.026 2.971 0.134 3.738-1.328 c0.028-0.053 0.064-0.089 0.09-0.146c0.049-0.119 0.086-0.232 0.113-0.341c0.398-1.586-1.396-2.169-2.316-3.113 c-0.159-0.163-0.322-0.34-0.462-0.523c-0.389-0.508-0.595-1.069 0.001-1.558c0.515-0.422 1.704-0.564 2.294-0.258 c3.199 1.7 4.7 0.5 5.533-2.735c0.286-1.132 1.02-1.809 1.979-1.574c0.325 0.079 0.677 0.262 1.047 0.568 c2.446 2 4.8 4.2 5.601 7.437c0.483 2 0.5 4.07-1.045 5.7c-1.617 1.698-3.396 0.774-5.011-0.143 c-2.403-1.37-4.178-0.281-5.707 1.436c-3.979 4.466-8.223 8.75-11.737 13.601c-3.714 5.086-8.537 5.843-14.104 5.198 c-0.648-0.075-1.368-0.171-1.786-0.653c-0.114-0.131-0.209-0.285-0.27-0.482c-0.37-1.215 0.587-1.834 1.458-2.285 c2.948-1.527 5.975-2.908 8.896-4.486c1.887-1.021 3.851-2.061 5.402-3.496c1.875-1.738 5.248-3.51 4.134-6.221 c-0.141-0.343-0.323-0.6-0.535-0.794c-1.383-1.272-4.106 0.29-6.09 0.26c-4.13-0.028-8.242-0.928-12.342-0.218h-0.023v-0.073 c0.004-0.002 0.008-0.003 0.012-0.005c0.007-0.003 0.014-0.006 0.021-0.009c0.814-0.378 1.633-0.717 2.458-1.021 c2.471-0.91 4.987-1.504 7.531-1.902c0.032-0.005 0.064-0.011 0.096-0.016c0.033-0.005 0.065-0.009 0.098-0.014 C205.084 211.85 208.374 211.669 211.68 211.557z M194.177 187.948c3.15 2.3 4 6 2.9 6.258h-0.062 c-2.208-0.583-2.876-3.92-5.816-4.751c-0.006-0.001-0.012-0.005-0.018-0.007c-3.767-1.083-9.077-8.666-9.81-13.188 c-0.011-0.066-0.031-0.139-0.04-0.204c-0.012-0.087-0.008-0.164-0.016-0.249c-0.02-0.205-0.042-0.413-0.039-0.601 c0-0.001 0-0.001 0-0.002c0.001-0.067 0.017-0.102 0.025-0.152c0.146-0.854 1.329 0.547 2.516 2.208 c1.004 1.406 2.003 2.98 2.358 3.487c0.982 1.393 1.82 2.389 2.686 3.229C190.297 185.367 191.808 186.328 194.177 187.948z" fill="#E3E0DD">
#           </path>
#           <path d="M397.368 309.241c-0.261-0.421-0.515-0.851-0.789-1.251c-0.119-0.172-0.252-0.329-0.374-0.498 c-0.355-0.493-0.713-0.985-1.097-1.449c-1.061-1.284-2.228-2.461-3.529-3.541c-9.653-8.013-20.562-14.354-29.925-22.777 c-5.18-4.66-11.315-8.287-16.289-13.133c-3.436-3.346-6.821-6.178-11.363-7.746c-12.746-4.402-25.297-9.318-37.806-14.363 c-5.212-2.104-8.992-6.655-14.148-8.286c-5.011-1.585-9.368-3.845-13.188-7.062c-1.195-1.008-2.342-2.103-3.436-3.309 c-0.236-0.263-0.504-0.511-0.797-0.736c-1.041-0.805-2.462-1.286-4.507-0.657c2.625 3 6.2 4.898 6.2 8.75 c0.029 10.375-1.518 20.563-4.211 30.575c-0.283 1.058-0.617 2.509-2.144 2.399c-0.126-0.014-0.231-0.047-0.34-0.078 c-1.058-0.322-1.254-1.564-1.737-2.489c-1.168-2.226 0.229-5.108-1.879-7.075c-4.517-4.214-4.992-10.279-7.05-15.604 c-0.729-1.892 0.104-4.437-2.731-5.277c-0.006-0.003-0.013-0.006-0.021-0.008c-2.953-0.86-3.546 1.873-5.052 3.187 c-8.374 7.295-12.026 18.521-21.318 25.2c-8.297 5.931-16.328 12.183-26.8 13.716c-2.79 0.407-5.649 0.323-8.459 0.627 c-1.733 0.188-3.997-0.093-4.459 2.299c-0.365 1.899 1.1 3.102 2.5 3.949c1.73 1 3.1 2.899 4.7 3.578 c3.386 1.398 2.6 2.698 0.7 4.5c-2.543 2.476-3.724 4.93-0.872 8.198c1.765 2.021-0.304 4.5-1.314 5.711 c-0.307 0.367-0.615 0.511-0.923 0.513c-1.023 0.006-2.039-1.625-2.944-2.394c-0.887-0.75-1.582-1.731-2.484-2.459 c-1.267-1.021-2.576-2.888-4.149-2.603c-0.405 0.072-0.826 0.281-1.27 0.691c-2.076 1.9 0 3.9 1.4 5.602 c4.511 5.563 8.05 11.524 8.194 19.838c0 0.056 0.005 0.106 0.006 0.162c-3.156-2.711-6.338-4.35-8.485-7.479 c-1.777-2.588-3.426-5.543-6.256-7.043c-7.64-4.051-12.329-9.996-14.186-18.574c-1.413-6.529-1.927-13.146-3.01-19.693 c-1.136-6.866-2.037-13.854-5.661-20.014c-2.048-3.479-4.663-4.494-8.15-1.59c-3.831 3.191-7.883 6.066-11.413 9.674 c-8.022 8.195-15.606 17.19-26.436 21.801c-11.449 4.848-17.431 13.926-21.416 24.898c-4.198 11.539-5.315 23.633-6.518 35.768 c-1.136 11.451-1.973 22.699 1.5 34c0.259 0.869 0.56 1.72 0.86 2.569c1.22 3.454 2.781 6.741 4.682 9.873 c0.035 0.03 0.07 0.062 0.105 0.09c0.259 0.216 0.513 0.438 0.773 0.653c38.203 31.621 87.228 50.627 140.694 50.627 c53.438 0 102.44-18.985 140.635-50.577c3.521-2.911 6.94-5.938 10.272-9.06c-2.618-3.158-5.301-6.254-8.485-8.67 c-7.959-6.028-17.794-8.264-27.218-11.09c-0.239-0.071-0.48-0.144-0.719-0.215c-0.01-0.004-0.019-0.006-0.026-0.009 c-0.019-0.006-0.035-0.012-0.054-0.019c-0.25-0.076-0.492-0.154-0.724-0.235c-0.029-0.011-0.058-0.021-0.087-0.032 c-0.207-0.074-0.405-0.148-0.598-0.228c-0.136-0.056-0.261-0.113-0.389-0.171c-0.07-0.031-0.144-0.062-0.21-0.094 c-2.793-1.33-3.677-3.312-2.927-7.151c0.733-3.767 2.284-6.832 4.471-9.828c5.71-7.841 12.521-14.705 19.023-21.845 c7.076-7.768 15.928-13.119 25.398-17.319c7.65-3.396 10.099-2.508 15.7 3.799c0.678 0.8 1.1 2.196 3.093 1.354 c0.002-0.002 0.004-0.002 0.007-0.002C397.742 309.809 397.549 309.533 397.368 309.241z" fill="#E3E0DD">
#           </path>
#          </g>
#         </svg>
#        </a>
#       </div>
#       <h1 class="site-title" itemprop="headline">
#        <a href="https://coreyms.com/">
#         CoreyMS
#        </a>
#       </h1>
#       <p class="site-description" itemprop="description">
#        Development, Design, DIY, and more
#       </p>
#       <div class="social-links-div">
#        <ul>
#         <li class="social-links-li">
#          <a class="social-link social-youtube" href="https://www.youtube.com/user/schafer5">
#           <svg style="height: 40px; width: 40px;" version="1.1" viewbox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
#            <circle class="outer-shape" cx="50" cy="50" r="48">
#            </circle>
#            <path class="inner-shape" d="M97.284,26.359c-1-5.352-5.456-9.346-10.574-9.839c-12.221-0.784-24.488-1.42-36.731-1.428 c-12.244-0.007-24.464,0.616-36.687,1.388c-5.137,0.497-9.592,4.47-10.589,9.842C1.567,34.058,1,41.869,1,49.678 s0.568,15.619,1.703,23.355c0.996,5.372,5.451,9.822,10.589,10.314c12.226,0.773,24.439,1.561,36.687,1.561 c12.239,0,24.515-0.688,36.731-1.479c5.118-0.497,9.574-5.079,10.574-10.428C98.43,65.278,99,57.477,99,49.676 C99,41.88,98.428,34.083,97.284,26.359z M38.89,63.747V35.272l26.52,14.238L38.89,63.747z" style="opacity: 1; fill: rgb(255, 255, 255);" transform="translate(25,25) scale(0.5)">
#            </path>
#           </svg>
#          </a>
#         </li>
#         <li class="social-links-li">
#          <a class="social-link social-github" href="https://github.com/CoreyMSchafer">
#           <svg style="height: 40px; width: 40px;" version="1.1" viewbox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
#            <circle class="outer-shape" cx="50" cy="50" r="48">
#            </circle>
#            <path class="inner-shape" d="M50,1C22.938,1,1,22.938,1,50s21.938,49,49,49s49-21.938,49-49S77.062,1,50,1z M79.099,79.099 c-3.782,3.782-8.184,6.75-13.083,8.823c-1.245,0.526-2.509,0.989-3.79,1.387v-7.344c0-3.86-1.324-6.699-3.972-8.517 c1.659-0.16,3.182-0.383,4.57-0.67c1.388-0.287,2.855-0.702,4.402-1.245c1.547-0.543,2.935-1.189,4.163-1.938 c1.228-0.75,2.409-1.723,3.541-2.919s2.082-2.552,2.847-4.067s1.372-3.334,1.818-5.455c0.446-2.121,0.67-4.458,0.67-7.01 c0-4.945-1.611-9.155-4.833-12.633c1.467-3.828,1.308-7.991-0.478-12.489l-1.197-0.143c-0.829-0.096-2.321,0.255-4.474,1.053 c-2.153,0.798-4.57,2.105-7.249,3.924c-3.797-1.053-7.736-1.579-11.82-1.579c-4.115,0-8.039,0.526-11.772,1.579 c-1.69-1.149-3.294-2.097-4.809-2.847c-1.515-0.75-2.727-1.26-3.637-1.532c-0.909-0.271-1.754-0.439-2.536-0.503 c-0.782-0.064-1.284-0.079-1.507-0.048c-0.223,0.031-0.383,0.064-0.478,0.096c-1.787,4.53-1.946,8.694-0.478,12.489 c-3.222,3.477-4.833,7.688-4.833,12.633c0,2.552,0.223,4.889,0.67,7.01c0.447,2.121,1.053,3.94,1.818,5.455 c0.765,1.515,1.715,2.871,2.847,4.067s2.313,2.169,3.541,2.919c1.228,0.751,2.616,1.396,4.163,1.938 c1.547,0.543,3.014,0.957,4.402,1.245c1.388,0.287,2.911,0.511,4.57,0.67c-2.616,1.787-3.924,4.626-3.924,8.517v7.487 c-1.445-0.43-2.869-0.938-4.268-1.53c-4.899-2.073-9.301-5.041-13.083-8.823c-3.782-3.782-6.75-8.184-8.823-13.083 C9.934,60.948,8.847,55.56,8.847,50s1.087-10.948,3.231-16.016c2.073-4.899,5.041-9.301,8.823-13.083s8.184-6.75,13.083-8.823 C39.052,9.934,44.44,8.847,50,8.847s10.948,1.087,16.016,3.231c4.9,2.073,9.301,5.041,13.083,8.823 c3.782,3.782,6.75,8.184,8.823,13.083c2.143,5.069,3.23,10.457,3.23,16.016s-1.087,10.948-3.231,16.016 C85.848,70.915,82.88,75.317,79.099,79.099L79.099,79.099z" style="opacity: 1; fill: rgb(255, 255, 255);" transform="translate(25,25) scale(0.5)">
#            </path>
#           </svg>
#          </a>
#         </li>
#         <li class="social-links-li">
#          <a class="social-link social-gplus" href="https://plus.google.com/+CoreySchafer44/posts" title="YouTube">
#           <svg style="height: 40px; width: 40px;" version="1.1" viewbox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
#            <circle class="outer-shape" cx="50" cy="50" r="48">
#            </circle>
#            <path class="inner-shape" d="M1.079,84.227c-0.024-0.242-0.043-0.485-0.056-0.73C1.036,83.742,1.055,83.985,1.079,84.227z M23.578,55.086 c8.805,0.262,14.712-8.871,13.193-20.402c-1.521-11.53-9.895-20.783-18.701-21.046C9.264,13.376,3.357,22.2,4.878,33.734 C6.398,45.262,14.769,54.823,23.578,55.086z M98.999,25.501v-8.164c0-8.984-7.348-16.335-16.332-16.335H17.336 c-8.831,0-16.078,7.104-16.323,15.879c5.585-4.917,13.333-9.026,21.329-9.026c8.546,0,34.188,0,34.188,0l-7.651,6.471H38.039 c7.19,2.757,11.021,11.113,11.021,19.687c0,7.201-4.001,13.393-9.655,17.797c-5.516,4.297-6.562,6.096-6.562,9.749 c0,3.117,5.909,8.422,8.999,10.602c9.032,6.368,11.955,12.279,11.955,22.15c0,1.572-0.195,3.142-0.58,4.685h29.451 C91.652,98.996,99,91.651,99,82.661V31.625H80.626v18.374h-6.125V31.625H56.127V25.5h18.374V7.127h6.125V25.5H99L98.999,25.501z M18.791,74.301c2.069,0,3.964-0.057,5.927-0.057c-2.598-2.52-4.654-5.608-4.654-9.414c0-2.259,0.724-4.434,1.736-6.366 c-1.032,0.073-2.085,0.095-3.17,0.095c-7.116,0-13.159-2.304-17.629-6.111v6.435l0.001,19.305 C6.116,75.76,12.188,74.301,18.791,74.301L18.791,74.301z M1.329,85.911c-0.107-0.522-0.188-1.053-0.243-1.591 C1.141,84.858,1.223,85.389,1.329,85.911z M44.589,92.187c-1.442-5.628-6.551-8.418-13.675-13.357 c-2.591-0.836-5.445-1.328-8.507-1.36c-8.577-0.092-16.566,3.344-21.074,8.457c1.524,7.436,8.138,13.068,16.004,13.068h27.413 c0.173-1.065,0.258-2.166,0.258-3.295C45.007,94.502,44.86,93.329,44.589,92.187z" style="opacity: 1; fill: rgb(255, 255, 255);" transform="translate(25,25) scale(0.5)">
#            </path>
#           </svg>
#          </a>
#         </li>
#         <li class="social-links-li">
#          <a class="social-link social-twitter" href="https://twitter.com/CoreyMSchafer">
#           <svg style="height: 40px; width: 40px;" version="1.1" viewbox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
#            <circle class="outer-shape" cx="50" cy="50" r="48">
#            </circle>
#            <path class="inner-shape" d="M99.001,19.428c-3.606,1.608-7.48,2.695-11.547,3.184c4.15-2.503,7.338-6.466,8.841-11.189 c-3.885,2.318-8.187,4-12.768,4.908c-3.667-3.931-8.893-6.387-14.676-6.387c-11.104,0-20.107,9.054-20.107,20.223 c0,1.585,0.177,3.128,0.52,4.609c-16.71-0.845-31.525-8.895-41.442-21.131C6.092,16.633,5.1,20.107,5.1,23.813 c0,7.017,3.55,13.208,8.945,16.834c-3.296-0.104-6.397-1.014-9.106-2.529c-0.002,0.085-0.002,0.17-0.002,0.255 c0,9.799,6.931,17.972,16.129,19.831c-1.688,0.463-3.463,0.71-5.297,0.71c-1.296,0-2.555-0.127-3.783-0.363 c2.559,8.034,9.984,13.882,18.782,14.045c-6.881,5.424-15.551,8.657-24.971,8.657c-1.623,0-3.223-0.096-4.796-0.282 c8.898,5.738,19.467,9.087,30.82,9.087c36.982,0,57.206-30.817,57.206-57.543c0-0.877-0.02-1.748-0.059-2.617 C92.896,27.045,96.305,23.482,99.001,19.428z" style="opacity: 1; fill: rgb(255, 255, 255);" transform="translate(25,25) scale(0.5)">
#            </path>
#           </svg>
#          </a>
#         </li>
#         <li class="social-links-li">
#          <a class="social-link social-linkedin" href="https://www.instagram.com/coreymschafer/">
#           <svg style="height: 40px; width: 40px;" version="1.1" viewbox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
#            <circle class="outer-shape" cx="50" cy="50" r="48">
#            </circle>
#            <path class="inner-shape" d="M88.2,1H11.8C5.85,1,1.026,5.827,1.026,11.781V88.22C1.026,94.174,5.85,99,11.8,99H88.2c5.95,0,10.774-4.826,10.774-10.78 V11.781C98.973,5.827,94.149,1,88.2,1z M49.946,31.184c10.356,0,18.752,8.4,18.752,18.762c0,10.361-8.396,18.761-18.752,18.761 s-18.752-8.4-18.752-18.761S39.589,31.184,49.946,31.184z M87.513,83.615c0,2.165-1.753,3.919-3.917,3.919H16.341 c-2.164,0-3.917-1.755-3.917-3.919v-41.06h8.508c-0.589,2.35-0.904,4.807-0.904,7.34c0,16.612,13.459,30.079,30.063,30.079 s30.063-13.466,30.063-30.079c0-2.533-0.315-4.99-0.904-7.34h8.263L87.513,83.615L87.513,83.615z M87.764,27.124 c0,2.165-1.754,3.919-3.918,3.919H72.723c-2.164,0-3.917-1.755-3.917-3.919v-11.13c0-2.165,1.754-3.919,3.917-3.919h11.123 c2.165,0,3.918,1.755,3.918,3.919V27.124z" style="opacity: 1; fill: rgb(255, 255, 255);" transform="translate(25,25) scale(0.5)">
#            </path>
#           </svg>
#          </a>
#         </li>
#         <li class="social-links-li">
#          <a class="social-link social-rss" href="http://coreyms.com/feed/">
#           <svg style="height: 40px; width: 40px;" version="1.1" viewbox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
#            <circle class="outer-shape" cx="50" cy="50" r="48">
#            </circle>
#            <path class="inner-shape" d="M14.044,72.866C6.848,72.866,1,78.736,1,85.889c0,7.192,5.848,12.997,13.044,12.997c7.223,0,13.062-5.804,13.062-12.997 C27.106,78.736,21.267,72.866,14.044,72.866z M1.015,34.299v18.782c12.229,0,23.73,4.782,32.392,13.447 C42.057,75.172,46.832,86.725,46.832,99h18.865C65.697,63.321,36.672,34.3,1.015,34.299L1.015,34.299z M1.038,1v18.791 C44.657,19.792,80.16,55.329,80.16,99H99C99,44.979,55.048,1,1.038,1z" style="opacity: 1; fill: rgb(255, 255, 255);" transform="translate(25,25) scale(0.5)">
#            </path>
#           </svg>
#          </a>
#         </li>
#        </ul>
#       </div>
#      </div>
#      <div class="widget-area header-widget-area">
#       <section class="widget widget_nav_menu" id="nav_menu-2">
#        <div class="widget-wrap">
#         <nav class="nav-header" itemscope="" itemtype="https://schema.org/SiteNavigationElement">
#          <ul class="menu genesis-nav-menu js-superfish" id="menu-contact-menu">
#           <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-984" id="menu-item-984">
#            <a href="https://coreyms.com/contact" itemprop="url">
#             <span itemprop="name">
#              Contact
#             </span>
#            </a>
#           </li>
#           <li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-153" id="menu-item-153">
#            <a href="http://coreyms.com/portfolio" itemprop="url" title="Portfolio">
#             <span itemprop="name">
#              Portfolio
#             </span>
#            </a>
#           </li>
#          </ul>
#         </nav>
#        </div>
#       </section>
#      </div>
#     </div>
#    </header>
#    <nav aria-label="Main" class="nav-primary" itemscope="" itemtype="https://schema.org/SiteNavigationElement">
#     <div class="wrap">
#      <ul class="menu genesis-nav-menu menu-primary js-superfish" id="menu-primary-navigation">
#       <li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children menu-item-124" id="menu-item-124">
#        <a href="https://coreyms.com/category/development" itemprop="url" title="Development">
#         <span itemprop="name">
#          Development
#         </span>
#        </a>
#        <ul class="sub-menu">
#         <li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-1070" id="menu-item-1070">
#          <a href="https://coreyms.com/category/development/python" itemprop="url">
#           <span itemprop="name">
#            Python
#           </span>
#          </a>
#         </li>
#         <li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-1105" id="menu-item-1105">
#          <a href="https://coreyms.com/category/development/git" itemprop="url">
#           <span itemprop="name">
#            Git
#           </span>
#          </a>
#         </li>
#         <li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-1106" id="menu-item-1106">
#          <a href="https://coreyms.com/category/development/terminal" itemprop="url">
#           <span itemprop="name">
#            Terminal
#           </span>
#          </a>
#         </li>
#         <li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-803" id="menu-item-803">
#          <a href="https://coreyms.com/category/development/javascript" itemprop="url" title="JavaScript">
#           <span itemprop="name">
#            JavaScript
#           </span>
#          </a>
#         </li>
#         <li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-1072" id="menu-item-1072">
#          <a href="https://coreyms.com/category/development/wordpress" itemprop="url">
#           <span itemprop="name">
#            WordPress
#           </span>
#          </a>
#         </li>
#        </ul>
#       </li>
#       <li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children menu-item-125" id="menu-item-125">
#        <a href="https://coreyms.com/category/web-design" itemprop="url" title="Design">
#         <span itemprop="name">
#          Design
#         </span>
#        </a>
#        <ul class="sub-menu">
#         <li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-801" id="menu-item-801">
#          <a href="https://coreyms.com/category/web-design/css" itemprop="url" title="CSS">
#           <span itemprop="name">
#            CSS
#           </span>
#          </a>
#         </li>
#        </ul>
#       </li>
#       <li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children menu-item-804" id="menu-item-804">
#        <a href="https://coreyms.com/category/diy" itemprop="url" title="DIY">
#         <span itemprop="name">
#          DIY
#         </span>
#        </a>
#        <ul class="sub-menu">
#         <li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-805" id="menu-item-805">
#          <a href="https://coreyms.com/category/diy/woodworking" itemprop="url" title="Woodworking">
#           <span itemprop="name">
#            Woodworking
#           </span>
#          </a>
#         </li>
#         <li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-806" id="menu-item-806">
#          <a href="https://coreyms.com/category/diy/home-improvement" itemprop="url" title="Home Improvement">
#           <span itemprop="name">
#            Home Improvement
#           </span>
#          </a>
#         </li>
#        </ul>
#       </li>
#       <li class="right menu-item menu-item-type-post_type menu-item-object-page menu-item-1154" id="menu-item-1154">
#        <a href="https://coreyms.com/contributors" itemprop="url" title="Contributors">
#         <span itemprop="name">
#          Contributors
#         </span>
#        </a>
#       </li>
#       <li class="right menu-item menu-item-type-post_type menu-item-object-page menu-item-898" id="menu-item-898">
#        <a href="https://coreyms.com/support" itemprop="url" title="Support">
#         <span itemprop="name">
#          Support
#         </span>
#        </a>
#       </li>
#       <li class="right menu-item menu-item-type-post_type menu-item-object-page menu-item-1260" id="menu-item-1260">
#        <a href="https://coreyms.com/giveaway" itemprop="url">
#         <span itemprop="name">
#          Giveaway
#         </span>
#        </a>
#       </li>
#      </ul>
#     </div>
#    </nav>
#    <div class="site-inner">
#     <div class="content-sidebar-wrap">
#      <main class="content">
#       <article class="post-1670 post type-post status-publish format-standard has-post-thumbnail category-development category-python tag-gzip tag-shutil tag-zip tag-zipfile entry" itemscope="" itemtype="https://schema.org/CreativeWork">
#        <header class="entry-header">
#         <h2 class="entry-title" itemprop="headline">
#          <a class="entry-title-link" href="https://coreyms.com/development/python/python-tutorial-zip-files-creating-and-extracting-zip-archives" rel="bookmark">
#           Python Tutorial: Zip Files – Creating and Extracting Zip Archives
#          </a>
#         </h2>
#         <p class="entry-meta">
#          <time class="entry-time" datetime="2019-11-19T13:02:37-05:00" itemprop="datePublished">
#           November 19, 2019
#          </time>
#          by
#          <span class="entry-author" itemprop="author" itemscope="" itemtype="https://schema.org/Person">
#           <a class="entry-author-link" href="https://coreyms.com/author/coreymschafer" itemprop="url" rel="author">
#            <span class="entry-author-name" itemprop="name">
#             Corey Schafer
#            </span>
#           </a>
#          </span>
#          <span class="entry-comments-link">
#           <a href="https://coreyms.com/development/python/python-tutorial-zip-files-creating-and-extracting-zip-archives#respond">
#            <span class="dsq-postid" data-dsqidentifier="1670 http://coreyms.com/?p=1670">
#             Leave a Comment
#            </span>
#           </a>
#          </span>
#         </p>
#        </header>
#        <div class="entry-content" itemprop="text">
#         <p>
#          In this video, we will be learning how to create and extract zip archives. We will start by using the zipfile module, and then we will see how to do this using the shutil module. We will learn how to do this with single files and directories, as well as learning how to use gzip as well. Let’s get started…
#          <br/>
#         </p>
#         <span class="embed-youtube" style="text-align:center; display: block;">
#          <iframe allowfullscreen="true" class="youtube-player" height="360" src="https://www.youtube.com/embed/z0gguhEmWiY?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="640">
#          </iframe>
#         </span>
#        </div>
#        <footer class="entry-footer">
#         <p class="entry-meta">
#          <span class="entry-categories">
#           Filed Under:
#           <a href="https://coreyms.com/category/development" rel="category tag">
#            Development
#           </a>
#           ,
#           <a href="https://coreyms.com/category/development/python" rel="category tag">
#            Python
#           </a>
#          </span>
#          <span class="entry-tags">
#           Tagged With:
#           <a href="https://coreyms.com/tag/gzip" rel="tag">
#            gzip
#           </a>
#           ,
#           <a href="https://coreyms.com/tag/shutil" rel="tag">
#            shutil
#           </a>
#           ,
#           <a href="https://coreyms.com/tag/zip" rel="tag">
#            zip
#           </a>
#           ,
#           <a href="https://coreyms.com/tag/zipfile" rel="tag">
#            zipfile
#           </a>
#          </span>
#         </p>
#        </footer>
#       </article>
#       <article class="post-1665 post type-post status-publish format-standard has-post-thumbnail category-development category-python tag-data-analysis tag-data-science tag-stack-overflow entry" itemscope="" itemtype="https://schema.org/CreativeWork">
#        <header class="entry-header">
#         <h2 class="entry-title" itemprop="headline">
#          <a class="entry-title-link" href="https://coreyms.com/development/python/python-data-science-tutorial-analyzing-the-2019-stack-overflow-developer-survey" rel="bookmark">
#           Python Data Science Tutorial: Analyzing the 2019 Stack Overflow Developer Survey
#          </a>
#         </h2>
#         <p class="entry-meta">
#          <time class="entry-time" datetime="2019-10-17T12:35:51-04:00" itemprop="datePublished">
#           October 17, 2019
#          </time>
#          by
#          <span class="entry-author" itemprop="author" itemscope="" itemtype="https://schema.org/Person">
#           <a class="entry-author-link" href="https://coreyms.com/author/coreymschafer" itemprop="url" rel="author">
#            <span class="entry-author-name" itemprop="name">
#             Corey Schafer
#            </span>
#           </a>
#          </span>
#          <span class="entry-comments-link">
#           <a href="https://coreyms.com/development/python/python-data-science-tutorial-analyzing-the-2019-stack-overflow-developer-survey#respond">
#            <span class="dsq-postid" data-dsqidentifier="1665 http://coreyms.com/?p=1665">
#             Leave a Comment
#            </span>
#           </a>
#          </span>
#         </p>
#        </header>
#        <div class="entry-content" itemprop="text">
#         <p>
#          In this Python Programming video, we will be learning how to download and analyze real-world data from the 2019 Stack Overflow Developer Survey. This is terrific practice for anyone getting into the data science field. We will learn different ways to analyze this data and also some best practices. Let’s get started…
#         </p>
#         <figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio">
#          <div class="wp-block-embed__wrapper">
#           <span class="embed-youtube" style="text-align:center; display: block;">
#            <iframe allowfullscreen="true" class="youtube-player" height="360" src="https://www.youtube.com/embed/_P7X8tMplsw?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="640">
#            </iframe>
#           </span>
#          </div>
#         </figure>
#        </div>
#        <footer class="entry-footer">
#         <p class="entry-meta">
#          <span class="entry-categories">
#           Filed Under:
#           <a href="https://coreyms.com/category/development" rel="category tag">
#            Development
#           </a>
#           ,
#           <a href="https://coreyms.com/category/development/python" rel="category tag">
#            Python
#           </a>
#          </span>
#          <span class="entry-tags">
#           Tagged With:
#           <a href="https://coreyms.com/tag/data-analysis" rel="tag">
#            data analysis
#           </a>
#           ,
#           <a href="https://coreyms.com/tag/data-science" rel="tag">
#            Data Science
#           </a>
#           ,
#           <a href="https://coreyms.com/tag/stack-overflow" rel="tag">
#            stack overflow
#           </a>
#          </span>
#         </p>
#        </footer>
#       </article>
#       <article class="post-1661 post type-post status-publish format-standard has-post-thumbnail category-development category-python tag-asynchronous tag-concurrent-futures tag-multiprocessing tag-parallel tag-threading entry" itemscope="" itemtype="https://schema.org/CreativeWork">
#        <header class="entry-header">
#         <h2 class="entry-title" itemprop="headline">
#          <a class="entry-title-link" href="https://coreyms.com/development/python/python-multiprocessing-tutorial-run-code-in-parallel-using-the-multiprocessing-module" rel="bookmark">
#           Python Multiprocessing Tutorial: Run Code in Parallel Using the Multiprocessing Module
#          </a>
#         </h2>
#         <p class="entry-meta">
#          <time class="entry-time" datetime="2019-09-21T10:59:18-04:00" itemprop="datePublished">
#           September 21, 2019
#          </time>
#          by
#          <span class="entry-author" itemprop="author" itemscope="" itemtype="https://schema.org/Person">
#           <a class="entry-author-link" href="https://coreyms.com/author/coreymschafer" itemprop="url" rel="author">
#            <span class="entry-author-name" itemprop="name">
#             Corey Schafer
#            </span>
#           </a>
#          </span>
#          <span class="entry-comments-link">
#           <a href="https://coreyms.com/development/python/python-multiprocessing-tutorial-run-code-in-parallel-using-the-multiprocessing-module#respond">
#            <span class="dsq-postid" data-dsqidentifier="1661 http://coreyms.com/?p=1661">
#             Leave a Comment
#            </span>
#           </a>
#          </span>
#         </p>
#        </header>
#        <div class="entry-content" itemprop="text">
#         <p>
#          In this Python Programming video, we will be learning how to run code in parallel using the multiprocessing module. We will also look at how to process multiple high-resolution images at the same time using a ProcessPoolExecutor from the concurrent.futures module. Let’s get started…
#         </p>
#         <figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio">
#          <div class="wp-block-embed__wrapper">
#           <span class="embed-youtube" style="text-align:center; display: block;">
#            <iframe allowfullscreen="true" class="youtube-player" height="360" src="https://www.youtube.com/embed/fKl2JW_qrso?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="640">
#            </iframe>
#           </span>
#          </div>
#         </figure>
#        </div>
#        <footer class="entry-footer">
#         <p class="entry-meta">
#          <span class="entry-categories">
#           Filed Under:
#           <a href="https://coreyms.com/category/development" rel="category tag">
#            Development
#           </a>
#           ,
#           <a href="https://coreyms.com/category/development/python" rel="category tag">
#            Python
#           </a>
#          </span>
#          <span class="entry-tags">
#           Tagged With:
#           <a href="https://coreyms.com/tag/asynchronous" rel="tag">
#            asynchronous
#           </a>
#           ,
#           <a href="https://coreyms.com/tag/concurrent-futures" rel="tag">
#            concurrent.futures
#           </a>
#           ,
#           <a href="https://coreyms.com/tag/multiprocessing" rel="tag">
#            multiprocessing
#           </a>
#           ,
#           <a href="https://coreyms.com/tag/parallel" rel="tag">
#            parallel
#           </a>
#           ,
#           <a href="https://coreyms.com/tag/threading" rel="tag">
#            threading
#           </a>
#          </span>
#         </p>
#        </footer>
#       </article>
#       <article class="post-1658 post type-post status-publish format-standard has-post-thumbnail category-development category-python tag-asynchronous tag-concurrency tag-multiprocessing tag-threading entry" itemscope="" itemtype="https://schema.org/CreativeWork">
#        <header class="entry-header">
#         <h2 class="entry-title" itemprop="headline">
#          <a class="entry-title-link" href="https://coreyms.com/development/python/python-threading-tutorial-run-code-concurrently-using-the-threading-module" rel="bookmark">
#           Python Threading Tutorial: Run Code Concurrently Using the Threading Module
#          </a>
#         </h2>
#         <p class="entry-meta">
#          <time class="entry-time" datetime="2019-09-12T10:49:54-04:00" itemprop="datePublished">
#           September 12, 2019
#          </time>
#          by
#          <span class="entry-author" itemprop="author" itemscope="" itemtype="https://schema.org/Person">
#           <a class="entry-author-link" href="https://coreyms.com/author/coreymschafer" itemprop="url" rel="author">
#            <span class="entry-author-name" itemprop="name">
#             Corey Schafer
#            </span>
#           </a>
#          </span>
#          <span class="entry-comments-link">
#           <a href="https://coreyms.com/development/python/python-threading-tutorial-run-code-concurrently-using-the-threading-module#respond">
#            <span class="dsq-postid" data-dsqidentifier="1658 http://coreyms.com/?p=1658">
#             Leave a Comment
#            </span>
#           </a>
#          </span>
#         </p>
#        </header>
#        <div class="entry-content" itemprop="text">
#         <p>
#          In this Python Programming video, we will be learning how to run threads concurrently using the threading module. We will also look at how to download multiple high-resolution images online using a ThreadPoolExecutor from the concurrent.futures module. Let’s get started…
#         </p>
#         <figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio">
#          <div class="wp-block-embed__wrapper">
#           <span class="embed-youtube" style="text-align:center; display: block;">
#            <iframe allowfullscreen="true" class="youtube-player" height="360" src="https://www.youtube.com/embed/IEEhzQoKtQU?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="640">
#            </iframe>
#           </span>
#          </div>
#         </figure>
#        </div>
#        <footer class="entry-footer">
#         <p class="entry-meta">
#          <span class="entry-categories">
#           Filed Under:
#           <a href="https://coreyms.com/category/development" rel="category tag">
#            Development
#           </a>
#           ,
#           <a href="https://coreyms.com/category/development/python" rel="category tag">
#            Python
#           </a>
#          </span>
#          <span class="entry-tags">
#           Tagged With:
#           <a href="https://coreyms.com/tag/asynchronous" rel="tag">
#            asynchronous
#           </a>
#           ,
#           <a href="https://coreyms.com/tag/concurrency" rel="tag">
#            concurrency
#           </a>
#           ,
#           <a href="https://coreyms.com/tag/multiprocessing" rel="tag">
#            multiprocessing
#           </a>
#           ,
#           <a href="https://coreyms.com/tag/threading" rel="tag">
#            threading
#           </a>
#          </span>
#         </p>
#        </footer>
#       </article>
#       <article class="post-1655 post type-post status-publish format-standard category-general entry" itemscope="" itemtype="https://schema.org/CreativeWork">
#        <header class="entry-header">
#         <h2 class="entry-title" itemprop="headline">
#          <a class="entry-title-link" href="https://coreyms.com/general/update-2019-09-03" rel="bookmark">
#           Update (2019-09-03)
#          </a>
#         </h2>
#         <p class="entry-meta">
#          <time class="entry-time" datetime="2019-09-03T16:42:01-04:00" itemprop="datePublished">
#           September 3, 2019
#          </time>
#          by
#          <span class="entry-author" itemprop="author" itemscope="" itemtype="https://schema.org/Person">
#           <a class="entry-author-link" href="https://coreyms.com/author/coreymschafer" itemprop="url" rel="author">
#            <span class="entry-author-name" itemprop="name">
#             Corey Schafer
#            </span>
#           </a>
#          </span>
#          <span class="entry-comments-link">
#           <a href="https://coreyms.com/general/update-2019-09-03#respond">
#            <span class="dsq-postid" data-dsqidentifier="1655 http://coreyms.com/?p=1655">
#             Leave a Comment
#            </span>
#           </a>
#          </span>
#         </p>
#        </header>
#        <div class="entry-content" itemprop="text">
#         <p>
#          Hey everyone. I wanted to give you an update on my videos. I will be releasing videos on threading and multiprocessing within the next week. Thanks so much for your patience. I currently have a temporary recording studio setup at my Airbnb that will allow me to record and edit the threading/multiprocessing videos. I am going to be moving into my new house in 10 days and once I have my recording studio setup then you can expect much faster video releases. I really appreciate how patient everyone has been while I go through this move, especially those of you who are contributing monthly through YouTube
#         </p>
#        </div>
#        <footer class="entry-footer">
#         <p class="entry-meta">
#          <span class="entry-categories">
#           Filed Under:
#           <a href="https://coreyms.com/category/general" rel="category tag">
#            General
#           </a>
#          </span>
#         </p>
#        </footer>
#       </article>
#       <article class="post-1651 post type-post status-publish format-standard has-post-thumbnail category-development category-python tag-vs-is tag-equality tag-identity entry" itemscope="" itemtype="https://schema.org/CreativeWork">
#        <header class="entry-header">
#         <h2 class="entry-title" itemprop="headline">
#          <a class="entry-title-link" href="https://coreyms.com/development/python/python-quick-tip-the-difference-between-and-is-equality-vs-identity" rel="bookmark">
#           Python Quick Tip: The Difference Between “==” and “is” (Equality vs Identity)
#          </a>
#         </h2>
#         <p class="entry-meta">
#          <time class="entry-time" datetime="2019-08-06T12:17:28-04:00" itemprop="datePublished">
#           August 6, 2019
#          </time>
#          by
#          <span class="entry-author" itemprop="author" itemscope="" itemtype="https://schema.org/Person">
#           <a class="entry-author-link" href="https://coreyms.com/author/coreymschafer" itemprop="url" rel="author">
#            <span class="entry-author-name" itemprop="name">
#             Corey Schafer
#            </span>
#           </a>
#          </span>
#          <span class="entry-comments-link">
#           <a href="https://coreyms.com/development/python/python-quick-tip-the-difference-between-and-is-equality-vs-identity#respond">
#            <span class="dsq-postid" data-dsqidentifier="1651 http://coreyms.com/?p=1651">
#             Leave a Comment
#            </span>
#           </a>
#          </span>
#         </p>
#        </header>
#        <div class="entry-content" itemprop="text">
#         <p>
#          In this Python Programming Tutorial, we will be learning the difference between using “==” and the “is” keyword when doing comparisons. The difference between these is that “==” checks to see if values are equal, and the “is” keyword checks their identity, which means it’s going to check if the values are identical in terms of being the same object in memory. We’ll learn more in the video. Let’s get started…
#         </p>
#         <figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio">
#          <div class="wp-block-embed__wrapper">
#           <span class="embed-youtube" style="text-align:center; display: block;">
#            <iframe allowfullscreen="true" class="youtube-player" height="360" src="https://www.youtube.com/embed/mO_dS3rXDIs?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="640">
#            </iframe>
#           </span>
#          </div>
#         </figure>
#        </div>
#        <footer class="entry-footer">
#         <p class="entry-meta">
#          <span class="entry-categories">
#           Filed Under:
#           <a href="https://coreyms.com/category/development" rel="category tag">
#            Development
#           </a>
#           ,
#           <a href="https://coreyms.com/category/development/python" rel="category tag">
#            Python
#           </a>
#          </span>
#          <span class="entry-tags">
#           Tagged With:
#           <a href="https://coreyms.com/tag/vs-is" rel="tag">
#            == vs is
#           </a>
#           ,
#           <a href="https://coreyms.com/tag/equality" rel="tag">
#            equality
#           </a>
#           ,
#           <a href="https://coreyms.com/tag/identity" rel="tag">
#            identity
#           </a>
#          </span>
#         </p>
#        </footer>
#       </article>
#       <article class="post-1647 post type-post status-publish format-standard has-post-thumbnail category-development category-python tag-standard-library tag-subprocess entry" itemscope="" itemtype="https://schema.org/CreativeWork">
#        <header class="entry-header">
#         <h2 class="entry-title" itemprop="headline">
#          <a class="entry-title-link" href="https://coreyms.com/development/python/python-tutorial-calling-external-commands-using-the-subprocess-module" rel="bookmark">
#           Python Tutorial: Calling External Commands Using the Subprocess Module
#          </a>
#         </h2>
#         <p class="entry-meta">
#          <time class="entry-time" datetime="2019-07-24T15:26:19-04:00" itemprop="datePublished">
#           July 24, 2019
#          </time>
#          by
#          <span class="entry-author" itemprop="author" itemscope="" itemtype="https://schema.org/Person">
#           <a class="entry-author-link" href="https://coreyms.com/author/coreymschafer" itemprop="url" rel="author">
#            <span class="entry-author-name" itemprop="name">
#             Corey Schafer
#            </span>
#           </a>
#          </span>
#          <span class="entry-comments-link">
#           <a href="https://coreyms.com/development/python/python-tutorial-calling-external-commands-using-the-subprocess-module#respond">
#            <span class="dsq-postid" data-dsqidentifier="1647 http://coreyms.com/?p=1647">
#             Leave a Comment
#            </span>
#           </a>
#          </span>
#         </p>
#        </header>
#        <div class="entry-content" itemprop="text">
#         <p>
#          In this Python Programming Tutorial, we will be learning how to run external commands using the subprocess module from the standard library. We will learn how to run commands, capture the output, handle errors, and also how to pipe output into other commands. Let’s get started…
#         </p>
#         <figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio">
#          <div class="wp-block-embed__wrapper">
#           <span class="embed-youtube" style="text-align:center; display: block;">
#            <iframe allowfullscreen="true" class="youtube-player" height="360" src="https://www.youtube.com/embed/2Fp1N6dof0Y?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="640">
#            </iframe>
#           </span>
#          </div>
#         </figure>
#        </div>
#        <footer class="entry-footer">
#         <p class="entry-meta">
#          <span class="entry-categories">
#           Filed Under:
#           <a href="https://coreyms.com/category/development" rel="category tag">
#            Development
#           </a>
#           ,
#           <a href="https://coreyms.com/category/development/python" rel="category tag">
#            Python
#           </a>
#          </span>
#          <span class="entry-tags">
#           Tagged With:
#           <a href="https://coreyms.com/tag/standard-library" rel="tag">
#            standard library
#           </a>
#           ,
#           <a href="https://coreyms.com/tag/subprocess" rel="tag">
#            subprocess
#           </a>
#          </span>
#         </p>
#        </footer>
#       </article>
#       <article class="post-1642 post type-post status-publish format-standard has-post-thumbnail category-development category-python tag-development-environment tag-visual-studio-code tag-visual-studios tag-vs-code tag-vscode entry" itemscope="" itemtype="https://schema.org/CreativeWork">
#        <header class="entry-header">
#         <h2 class="entry-title" itemprop="headline">
#          <a class="entry-title-link" href="https://coreyms.com/development/python/visual-studio-code-windows-setting-up-a-python-development-environment-and-complete-overview" rel="bookmark">
#           Visual Studio Code (Windows) – Setting up a Python Development Environment and Complete Overview
#          </a>
#         </h2>
#         <p class="entry-meta">
#          <time class="entry-time" datetime="2019-05-01T14:03:24-04:00" itemprop="datePublished">
#           May 1, 2019
#          </time>
#          by
#          <span class="entry-author" itemprop="author" itemscope="" itemtype="https://schema.org/Person">
#           <a class="entry-author-link" href="https://coreyms.com/author/coreymschafer" itemprop="url" rel="author">
#            <span class="entry-author-name" itemprop="name">
#             Corey Schafer
#            </span>
#           </a>
#          </span>
#          <span class="entry-comments-link">
#           <a href="https://coreyms.com/development/python/visual-studio-code-windows-setting-up-a-python-development-environment-and-complete-overview#respond">
#            <span class="dsq-postid" data-dsqidentifier="1642 http://coreyms.com/?p=1642">
#             Leave a Comment
#            </span>
#           </a>
#          </span>
#         </p>
#        </header>
#        <div class="entry-content" itemprop="text">
#         <p>
#          In this Python Programming Tutorial, we will be learning how to set up a Python development environment in VSCode on Windows. VSCode is a very nice free editor for writing Python applications and many developers are now switching over to this editor. In this video, we will learn how to install VSCode, get the Python extension installed, how to change Python interpreters, create virtual environments, format/lint our code, how to use Git within VSCode, how to debug our programs, how unit testing works, and more. We have a lot to cover, so let’s go ahead and get started…
#         </p>
#         <p>
#          VSCode on MacOS – https://youtu.be/06I63_p-2A4
#         </p>
#         <p>
#          Timestamps for topics in this tutorial:
#          <br/>
#          Installation – 1:13
#          <br/>
#          Python Extension – 5:48
#          <br/>
#          Switching Interpreters – 10:04
#          <br/>
#          Changing Color Themes – 12:35
#          <br/>
#          VSCode Settings – 16:16
#          <br/>
#          Set Default Python – 21:33
#          <br/>
#          Using Virtual Environments – 25:10
#          <br/>
#          IntelliSense – 29:45
#          <br/>
#          Code Formatting – 32:13
#          <br/>
#          Code Linting – 37:06
#          <br/>
#          Code Runner Extension – 39:42
#          <br/>
#          Git Integration – 47:44
#          <br/>
#          Use Different Terminal – 51:07
#          <br/>
#          Debugging – 58:45
#          <br/>
#          Unit Testing – 1:03:25
#          <br/>
#          Zen Mode – 1:09:55
#         </p>
#         <figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio">
#          <div class="wp-block-embed__wrapper">
#           <span class="embed-youtube" style="text-align:center; display: block;">
#            <iframe allowfullscreen="true" class="youtube-player" height="360" src="https://www.youtube.com/embed/-nh9rCzPJ20?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="640">
#            </iframe>
#           </span>
#          </div>
#         </figure>
#        </div>
#        <footer class="entry-footer">
#         <p class="entry-meta">
#          <span class="entry-categories">
#           Filed Under:
#           <a href="https://coreyms.com/category/development" rel="category tag">
#            Development
#           </a>
#           ,
#           <a href="https://coreyms.com/category/development/python" rel="category tag">
#            Python
#           </a>
#          </span>
#          <span class="entry-tags">
#           Tagged With:
#           <a href="https://coreyms.com/tag/development-environment" rel="tag">
#            Development Environment
#           </a>
#           ,
#           <a href="https://coreyms.com/tag/visual-studio-code" rel="tag">
#            visual studio code
#           </a>
#           ,
#           <a href="https://coreyms.com/tag/visual-studios" rel="tag">
#            visual studios
#           </a>
#           ,
#           <a href="https://coreyms.com/tag/vs-code" rel="tag">
#            vs code
#           </a>
#           ,
#           <a href="https://coreyms.com/tag/vscode" rel="tag">
#            vscode
#           </a>
#          </span>
#         </p>
#        </footer>
#       </article>
#       <article class="post-1639 post type-post status-publish format-standard has-post-thumbnail category-development category-python tag-development-environment tag-visual-studio-code tag-visual-studios tag-vs-code tag-vscode entry" itemscope="" itemtype="https://schema.org/CreativeWork">
#        <header class="entry-header">
#         <h2 class="entry-title" itemprop="headline">
#          <a class="entry-title-link" href="https://coreyms.com/development/python/visual-studio-code-mac-setting-up-a-python-development-environment-and-complete-overview" rel="bookmark">
#           Visual Studio Code (Mac) – Setting up a Python Development Environment and Complete Overview
#          </a>
#         </h2>
#         <p class="entry-meta">
#          <time class="entry-time" datetime="2019-05-01T14:01:45-04:00" itemprop="datePublished">
#           May 1, 2019
#          </time>
#          by
#          <span class="entry-author" itemprop="author" itemscope="" itemtype="https://schema.org/Person">
#           <a class="entry-author-link" href="https://coreyms.com/author/coreymschafer" itemprop="url" rel="author">
#            <span class="entry-author-name" itemprop="name">
#             Corey Schafer
#            </span>
#           </a>
#          </span>
#          <span class="entry-comments-link">
#           <a href="https://coreyms.com/development/python/visual-studio-code-mac-setting-up-a-python-development-environment-and-complete-overview#respond">
#            <span class="dsq-postid" data-dsqidentifier="1639 http://coreyms.com/?p=1639">
#             Leave a Comment
#            </span>
#           </a>
#          </span>
#         </p>
#        </header>
#        <div class="entry-content" itemprop="text">
#         <p>
#          In this Python Programming Tutorial, we will be learning how to set up a Python development environment in VSCode on MacOS. VSCode is a very nice free editor for writing Python applications and many developers are now switching over to this editor. In this video, we will learn how to install VSCode, get the Python extension installed, how to change Python interpreters, create virtual environments, format/lint our code, how to use Git within VSCode, how to debug our programs, how unit testing works, and more. We have a lot to cover, so let’s go ahead and get started…
#         </p>
#         <p>
#          VSCode on Windows – https://youtu.be/-nh9rCzPJ20
#         </p>
#         <p>
#          Timestamps for topics in this tutorial:
#          <br/>
#          Installation – 1:11
#          <br/>
#          Python Extension – 6:21
#          <br/>
#          Switching Interpreters – 10:16
#          <br/>
#          Changing Color Themes – 13:08
#          <br/>
#          VSCode Settings – 17:12
#          <br/>
#          Set Default Python – 22:24
#          <br/>
#          Using Virtual Environments – 25:52
#          <br/>
#          IntelliSense – 30:28
#          <br/>
#          Code Formatting – 33:08
#          <br/>
#          Code Linting – 38:01
#          <br/>
#          Code Runner Extension – 40:45
#          <br/>
#          Git Integration – 49:05
#          <br/>
#          Debugging – 58:15
#          <br/>
#          Unit Testing – 1:02:38
#          <br/>
#          Zen Mode – 1:10:42
#         </p>
#         <figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio">
#          <div class="wp-block-embed__wrapper">
#           <span class="embed-youtube" style="text-align:center; display: block;">
#            <iframe allowfullscreen="true" class="youtube-player" height="360" src="https://www.youtube.com/embed/06I63_p-2A4?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="640">
#            </iframe>
#           </span>
#          </div>
#         </figure>
#        </div>
#        <footer class="entry-footer">
#         <p class="entry-meta">
#          <span class="entry-categories">
#           Filed Under:
#           <a href="https://coreyms.com/category/development" rel="category tag">
#            Development
#           </a>
#           ,
#           <a href="https://coreyms.com/category/development/python" rel="category tag">
#            Python
#           </a>
#          </span>
#          <span class="entry-tags">
#           Tagged With:
#           <a href="https://coreyms.com/tag/development-environment" rel="tag">
#            Development Environment
#           </a>
#           ,
#           <a href="https://coreyms.com/tag/visual-studio-code" rel="tag">
#            visual studio code
#           </a>
#           ,
#           <a href="https://coreyms.com/tag/visual-studios" rel="tag">
#            visual studios
#           </a>
#           ,
#           <a href="https://coreyms.com/tag/vs-code" rel="tag">
#            vs code
#           </a>
#           ,
#           <a href="https://coreyms.com/tag/vscode" rel="tag">
#            vscode
#           </a>
#          </span>
#         </p>
#        </footer>
#       </article>
#       <article class="post-1634 post type-post status-publish format-standard has-post-thumbnail category-development category-python tag-common-errors tag-common-mistakes tag-functions tag-mutable-default-arguments entry" itemscope="" itemtype="https://schema.org/CreativeWork">
#        <header class="entry-header">
#         <h2 class="entry-title" itemprop="headline">
#          <a class="entry-title-link" href="https://coreyms.com/development/python/clarifying-the-issues-with-mutable-default-arguments" rel="bookmark">
#           Clarifying the Issues with Mutable Default Arguments
#          </a>
#         </h2>
#         <p class="entry-meta">
#          <time class="entry-time" datetime="2019-04-24T11:46:42-04:00" itemprop="datePublished">
#           April 24, 2019
#          </time>
#          by
#          <span class="entry-author" itemprop="author" itemscope="" itemtype="https://schema.org/Person">
#           <a class="entry-author-link" href="https://coreyms.com/author/coreymschafer" itemprop="url" rel="author">
#            <span class="entry-author-name" itemprop="name">
#             Corey Schafer
#            </span>
#           </a>
#          </span>
#          <span class="entry-comments-link">
#           <a href="https://coreyms.com/development/python/clarifying-the-issues-with-mutable-default-arguments#respond">
#            <span class="dsq-postid" data-dsqidentifier="1634 http://coreyms.com/?p=1634">
#             Leave a Comment
#            </span>
#           </a>
#          </span>
#         </p>
#        </header>
#        <div class="entry-content" itemprop="text">
#         <p>
#          In this Python Programming Tutorial, we will be clarifying the issues with mutable default arguments. We discussed this in my last video titled “5 Common Python Mistakes and How to Fix Them”, but I received many comments from people who were still confused. So we will be doing a deeper dive to explain exactly what is going on here. Let’s get started…
#         </p>
#         <figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio">
#          <div class="wp-block-embed__wrapper">
#           <span class="embed-youtube" style="text-align:center; display: block;">
#            <iframe allowfullscreen="true" class="youtube-player" height="360" src="https://www.youtube.com/embed/_JGmemuINww?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="640">
#            </iframe>
#           </span>
#          </div>
#         </figure>
#        </div>
#        <footer class="entry-footer">
#         <p class="entry-meta">
#          <span class="entry-categories">
#           Filed Under:
#           <a href="https://coreyms.com/category/development" rel="category tag">
#            Development
#           </a>
#           ,
#           <a href="https://coreyms.com/category/development/python" rel="category tag">
#            Python
#           </a>
#          </span>
#          <span class="entry-tags">
#           Tagged With:
#           <a href="https://coreyms.com/tag/common-errors" rel="tag">
#            common errors
#           </a>
#           ,
#           <a href="https://coreyms.com/tag/common-mistakes" rel="tag">
#            common mistakes
#           </a>
#           ,
#           <a href="https://coreyms.com/tag/functions" rel="tag">
#            functions
#           </a>
#           ,
#           <a href="https://coreyms.com/tag/mutable-default-arguments" rel="tag">
#            mutable default arguments
#           </a>
#          </span>
#         </p>
#        </footer>
#       </article>
#       <div class="archive-pagination pagination">
#        <ul>
#         <li class="active">
#          <a aria-current="page" aria-label="Current page" href="https://coreyms.com/">
#           1
#          </a>
#         </li>
#         <li>
#          <a href="https://coreyms.com/page/2">
#           2
#          </a>
#         </li>
#         <li>
#          <a href="https://coreyms.com/page/3">
#           3
#          </a>
#         </li>
#         <li class="pagination-omission">
#          …
#         </li>
#         <li>
#          <a href="https://coreyms.com/page/17">
#           17
#          </a>
#         </li>
#         <li class="pagination-next">
#          <a href="https://coreyms.com/page/2">
#           Next Page »
#          </a>
#         </li>
#        </ul>
#       </div>
#      </main>
#      <aside aria-label="Primary Sidebar" class="sidebar sidebar-primary widget-area" itemscope="" itemtype="https://schema.org/WPSideBar" role="complementary">
#       <section class="widget widget_text" id="text-5">
#        <div class="widget-wrap">
#         <h4 class="widget-title widgettitle">
#          Main Contributor
#         </h4>
#         <div class="textwidget">
#          <ul>
#           <li>
#            <b>
#             Andre Nevares
#            </b>
#           </li>
#          </ul>
#          <h4 style="margin-top: 25px; font-size: 17px;">
#           Top Contributors (17)
#          </h4>
#          <ul>
#           <li>
#            Andre Nevares
#           </li>
#           <li>
#            Cyril Hediger
#           </li>
#           <li>
#            Abhilash Rajan
#           </li>
#           <li>
#            Hien Nguyen
#           </li>
#           <li>
#            Alan Hawse – iotexpert.com
#           </li>
#           <li>
#            Just a Guy
#           </li>
#           <li>
#            Alex Canady
#           </li>
#           <li>
#            Sergey Trubin
#           </li>
#           <li>
#            Justin Presley
#           </li>
#           <li>
#            Sirake
#           </li>
#           <li>
#            chris
#           </li>
#           <li>
#            Jerome Massey
#           </li>
#           <li>
#            Robert Butler
#           </li>
#           <li>
#            Jonathan Llovet
#           </li>
#           <li>
#            David Myers
#           </li>
#           <li>
#            Karthik
#           </li>
#           <li>
#            Michael Zoitas
#           </li>
#          </ul>
#          <hr style="border: 0; border-bottom: 1px dotted #ddd;"/>
#          <p>
#           <b>
#            Thank You!
#           </b>
#           If you would like to have your name listed as a contributor and support the website, you can do so through
#           <a href="https://www.patreon.com/coreyms" rel="noopener noreferrer" target="_blank">
#            my Patreon Page
#           </a>
#           . I am extremely grateful for any support.
#          </p>
#         </div>
#        </div>
#       </section>
#       <section class="widget widget_search" id="search-3">
#        <div class="widget-wrap">
#         <h4 class="widget-title widgettitle">
#          Search CoreyMS.com
#         </h4>
#         <form action="https://coreyms.com/" class="search-form" itemprop="potentialAction" itemscope="" itemtype="https://schema.org/SearchAction" method="get" role="search">
#          <input class="search-form-input" id="searchform-5e4a2d56a6e692.56263372" itemprop="query-input" name="s" placeholder="Search this website" type="search"/>
#          <input class="search-form-submit" type="submit" value="Search"/>
#          <meta content="https://coreyms.com/?s={s}" itemprop="target"/>
#         </form>
#        </div>
#       </section>
#       <section class="widget enews-widget" id="enews-ext-4">
#        <div class="widget-wrap">
#         <div class="enews">
#          <h4 class="widget-title widgettitle">
#           Subscribe to Future Posts
#          </h4>
#          <form action="//coreyms.us9.list-manage.com/subscribe/post?u=f4df8a0f0be5d3754ed52b1ef&amp;id=5b06358625" id="subscribeenews-ext-4" method="post" name="enews-ext-4" onsubmit="if ( subbox1.value == 'First Name') { subbox1.value = ''; } if ( subbox2.value == 'Last Name') { subbox2.value = ''; }" target="_blank">
#           <label class="screenread" for="subbox1">
#            First Name
#           </label>
#           <input class="enews-subbox" id="subbox1" name="FNAME" placeholder="First Name" type="text" value=""/>
#           <label class="screenread" for="subbox">
#            E-Mail Address
#           </label>
#           <input id="subbox" name="EMAIL" placeholder="E-Mail Address" required="required" type="email" value=""/>
#           <input id="subbutton" type="submit" value="Subscribe"/>
#          </form>
#         </div>
#        </div>
#       </section>
#       <section class="widget widget_text" id="text-2">
#        <div class="widget-wrap">
#         <h4 class="widget-title widgettitle">
#          Recommended Books
#         </h4>
#         <div class="textwidget">
#          <a href="https://www.amazon.com/gp/product/1449355730/ref=as_li_tl?ie=UTF8&amp;camp=1789&amp;creative=9325&amp;creativeASIN=1449355730&amp;linkCode=as2&amp;tag=coreyms-20&amp;linkId=2f9ceaf471d7d35f2c2657051780fc6f" rel="noopener noreferrer" target="_blank">
#           <img border="0" class="widget_book" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&amp;MarketPlace=US&amp;ASIN=1449355730&amp;ServiceVersion=20070822&amp;ID=AsinImage&amp;WS=1&amp;Format=_SL250_&amp;tag=coreyms-20"/>
#          </a>
#          <img alt="" border="0" height="1" src="//ir-na.amazon-adsystem.com/e/ir?t=coreyms-20&amp;l=am2&amp;o=1&amp;a=1449355730" style="border:none !important; margin:0px !important;" width="1"/>
#          <a href="https://www.amazon.com/gp/product/1491946008/ref=as_li_tl?ie=UTF8&amp;camp=1789&amp;creative=9325&amp;creativeASIN=1491946008&amp;linkCode=as2&amp;tag=coreyms-20&amp;linkId=39335cdc340fb7ce5bd51d59c57e7e54" rel="noopener noreferrer" target="_blank">
#           <img border="0" class="widget_book" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&amp;MarketPlace=US&amp;ASIN=1491946008&amp;ServiceVersion=20070822&amp;ID=AsinImage&amp;WS=1&amp;Format=_SL250_&amp;tag=coreyms-20"/>
#          </a>
#          <img alt="" border="0" height="1" src="//ir-na.amazon-adsystem.com/e/ir?t=coreyms-20&amp;l=am2&amp;o=1&amp;a=1491946008" style="border:none !important; margin:0px !important;" width="1"/>
#          <a href="https://www.amazon.com/gp/product/1593276036/ref=as_li_tl?ie=UTF8&amp;camp=1789&amp;creative=9325&amp;creativeASIN=1593276036&amp;linkCode=as2&amp;tag=coreyms-20&amp;linkId=75ff844a147bc8cb5fb325608b286158" rel="noopener noreferrer" target="_blank">
#           <img border="0" class="widget_book" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&amp;MarketPlace=US&amp;ASIN=1593276036&amp;ServiceVersion=20070822&amp;ID=AsinImage&amp;WS=1&amp;Format=_SL250_&amp;tag=coreyms-20"/>
#          </a>
#          <img alt="" border="0" height="1" src="//ir-na.amazon-adsystem.com/e/ir?t=coreyms-20&amp;l=am2&amp;o=1&amp;a=1593276036" style="border:none !important; margin:0px !important;" width="1"/>
#          <a href="https://www.amazon.com/gp/product/0984782850/ref=as_li_tl?ie=UTF8&amp;camp=1789&amp;creative=9325&amp;creativeASIN=0984782850&amp;linkCode=as2&amp;tag=coreyms-20&amp;linkId=e2f7c21906426f17958a1d04718e7d02" rel="noopener noreferrer" target="_blank">
#           <img border="0" class="widget_book" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&amp;MarketPlace=US&amp;ASIN=0984782850&amp;ServiceVersion=20070822&amp;ID=AsinImage&amp;WS=1&amp;Format=_SL250_&amp;tag=coreyms-20"/>
#          </a>
#          <img alt="" border="0" height="1" src="//ir-na.amazon-adsystem.com/e/ir?t=coreyms-20&amp;l=am2&amp;o=1&amp;a=0984782850" style="border:none !important; margin:0px !important;" width="1"/>
#          <a href="https://www.amazon.com/gp/product/020161622X/ref=as_li_tl?ie=UTF8&amp;camp=1789&amp;creative=9325&amp;creativeASIN=020161622X&amp;linkCode=as2&amp;tag=coreyms-20&amp;linkId=a2699f6b6cb5814da54f71140c52f2ca" rel="noopener noreferrer" target="_blank">
#           <img border="0" class="widget_book" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&amp;MarketPlace=US&amp;ASIN=020161622X&amp;ServiceVersion=20070822&amp;ID=AsinImage&amp;WS=1&amp;Format=_SL250_&amp;tag=coreyms-20"/>
#          </a>
#          <img alt="" border="0" height="1" src="//ir-na.amazon-adsystem.com/e/ir?t=coreyms-20&amp;l=am2&amp;o=1&amp;a=020161622X" style="border:none !important; margin:0px !important;" width="1"/>
#          <a href="https://www.amazon.com/gp/product/0201835959/ref=as_li_tl?ie=UTF8&amp;camp=1789&amp;creative=9325&amp;creativeASIN=0201835959&amp;linkCode=as2&amp;tag=coreyms-20&amp;linkId=c3de80ab4a4761f7634751cf323af13f" rel="noopener noreferrer" target="_blank">
#           <img border="0" class="widget_book" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&amp;MarketPlace=US&amp;ASIN=0201835959&amp;ServiceVersion=20070822&amp;ID=AsinImage&amp;WS=1&amp;Format=_SL250_&amp;tag=coreyms-20"/>
#          </a>
#          <img alt="" border="0" height="1" src="//ir-na.amazon-adsystem.com/e/ir?t=coreyms-20&amp;l=am2&amp;o=1&amp;a=0201835959" style="border:none !important; margin:0px !important;" width="1"/>
#         </div>
#        </div>
#       </section>
#       <section class="widget widget_text" id="text-3">
#        <div class="widget-wrap">
#         <h4 class="widget-title widgettitle">
#          Podcasts I Listen To
#         </h4>
#         <div class="textwidget">
#          <u>
#           Tech Related
#          </u>
#          :
#          <br/>
#          <a href="http://talkpython.fm/">
#           Talk Python To Me
#          </a>
#          <br/>
#          <a href="http://shoptalkshow.com/">
#           Shoptalk Show
#          </a>
#          <br/>
#          <a href="http://www.se-radio.net/">
#           Software Engineering Radio
#          </a>
#          <br/>
#          <a href="http://hanselminutes.com/">
#           HanselMinutes
#          </a>
#          <br/>
#          <a href="https://blog.codepen.io/radio/">
#           CodePen Radio
#          </a>
#          <br/>
#          <br/>
#          <u>
#           Non-Tech Related
#          </u>
#          :
#          <br/>
#          <a href="http://www.dancarlin.com/hardcore-history-series/">
#           Dan Carlin's Hardcore History
#          </a>
#          <br/>
#          <a href="http://www.billburr.com/podcast">
#           Bill Burr's Monday Morning Podcast
#          </a>
#          <br/>
#          <a href="http://www.samharris.org/podcast">
#           Waking Up with Sam Harris
#          </a>
#          <br/>
#          <a href="http://www.startalkradio.net/shows-archive/">
#           StarTalk Radio
#          </a>
#          <br/>
#          <a href="http://carasantamaria.com/podcast/">
#           Talk Nerdy with Cara Santa Maria
#          </a>
#         </div>
#        </div>
#       </section>
#      </aside>
#     </div>
#    </div>
#    <footer class="site-footer" itemscope="" itemtype="https://schema.org/WPFooter">
#     <div class="wrap">
#      <p>
#       © 2020 ·
#       <a href="http://coreyms.com">
#        CoreyMS
#       </a>
#       · Corey Schafer
#      </p>
#     </div>
#    </footer>
#   </div>
#   <link href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/8.4/styles/zenburn.min.css" rel="stylesheet"/>
#   <script src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/8.4/highlight.min.js">
#   </script>
#   <script>
#    hljs.initHighlightingOnLoad();
#   </script>
#   <script type="text/javascript">
#    /* <![CDATA[ */
# var wpcf7 = {"apiSettings":{"root":"https:\/\/coreyms.com\/wp-json\/contact-form-7\/v1","namespace":"contact-form-7\/v1"},"cached":"1"};
# /* ]]> */
#   </script>
#   <script src="https://coreyms.com/wp-content/cache/minify/0fef6.js">
#   </script>
#   <script type="text/javascript">
#    /* <![CDATA[ */
# var countVars = {"disqusShortname":"coreyms"};
# /* ]]> */
#   </script>
#   <script src="https://coreyms.com/wp-content/cache/minify/9b739.js">
#   </script>
#   <script async="async" defer="defer" src="https://stats.wp.com/e-202008.js" type="text/javascript">
#   </script>
#   <script type="text/javascript">
#    _stq = window._stq || [];
# 	_stq.push([ 'view', {v:'ext',j:'1:8.2',blog:'70676981',post:'0',tz:'-5',srv:'coreyms.com'} ]);
# 	_stq.push([ 'clickTrackerInit', '70676981', '0' ]);
#   </script>
#  </body>
# </html>
# <!--
# Performance optimized by W3 Total Cache. Learn more: https://www.w3-edge.com/products/
#
# Page Caching using disk: enhanced (SSL caching disabled)
# Minified using disk
#
# Served from: coreyms.com @ 2020-02-17 01:06:14 by W3 Total Cache
# -->
#
#
# Process finished with exit code 0
#
# source = requests.get('http://coreyms.com').text
#
# soup = BeautifulSoup(source,'lxml')
#
# article = soup.find('article')

# o/p is -->

# /anaconda3/bin/python3.7m /Users/headshot/PycharmProjects/untitled10/beautiful.py
# <article class="post-1670 post type-post status-publish format-standard has-post-thumbnail category-development category-python tag-gzip tag-shutil tag-zip tag-zipfile entry" itemscope="" itemtype="https://schema.org/CreativeWork">
#  <header class="entry-header">
#   <h2 class="entry-title" itemprop="headline">
#    <a class="entry-title-link" href="https://coreyms.com/development/python/python-tutorial-zip-files-creating-and-extracting-zip-archives" rel="bookmark">
#     Python Tutorial: Zip Files – Creating and Extracting Zip Archives
#    </a>
#   </h2>
#   <p class="entry-meta">
#    <time class="entry-time" datetime="2019-11-19T13:02:37-05:00" itemprop="datePublished">
#     November 19, 2019
#    </time>
#    by
#    <span class="entry-author" itemprop="author" itemscope="" itemtype="https://schema.org/Person">
#     <a class="entry-author-link" href="https://coreyms.com/author/coreymschafer" itemprop="url" rel="author">
#      <span class="entry-author-name" itemprop="name">
#       Corey Schafer
#      </span>
#     </a>
#    </span>
#    <span class="entry-comments-link">
#     <a href="https://coreyms.com/development/python/python-tutorial-zip-files-creating-and-extracting-zip-archives#respond">
#      <span class="dsq-postid" data-dsqidentifier="1670 http://coreyms.com/?p=1670">
#       Leave a Comment
#      </span>
#     </a>
#    </span>
#   </p>
#  </header>
#  <div class="entry-content" itemprop="text">
#   <p>
#    In this video, we will be learning how to create and extract zip archives. We will start by using the zipfile module, and then we will see how to do this using the shutil module. We will learn how to do this with single files and directories, as well as learning how to use gzip as well. Let’s get started…
#    <br/>
#   </p>
#   <span class="embed-youtube" style="text-align:center; display: block;">
#    <iframe allowfullscreen="true" class="youtube-player" height="360" src="https://www.youtube.com/embed/z0gguhEmWiY?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="640">
#    </iframe>
#   </span>
#  </div>
#  <footer class="entry-footer">
#   <p class="entry-meta">
#    <span class="entry-categories">
#     Filed Under:
#     <a href="https://coreyms.com/category/development" rel="category tag">
#      Development
#     </a>
#     ,
#     <a href="https://coreyms.com/category/development/python" rel="category tag">
#      Python
#     </a>
#    </span>
#    <span class="entry-tags">
#     Tagged With:
#     <a href="https://coreyms.com/tag/gzip" rel="tag">
#      gzip
#     </a>
#     ,
#     <a href="https://coreyms.com/tag/shutil" rel="tag">
#      shutil
#     </a>
#     ,
#     <a href="https://coreyms.com/tag/zip" rel="tag">
#      zip
#     </a>
#     ,
#     <a href="https://coreyms.com/tag/zipfile" rel="tag">
#      zipfile
#     </a>
#    </span>
#   </p>
#  </footer>
# </article>
#
#
# Process finished with exit code 0

# source = requests.get('http://coreyms.com').text
#
# soup = BeautifulSoup(source,'lxml')
#
# article = soup.find('article')
# headline  = article.h2.a.text
# print (headline)

# o/p is -->        Python Tutorial: Zip Files – Creating and Extracting Zip Archives

# source = requests.get('http://coreyms.com').text

# soup = BeautifulSoup(source,'lxml')
# source = requests.get('http://coreyms.com').text

# soup = BeautifulSoup(source,'lxml')
# article = soup.find('article')
# headline  = article.h2.a.text
# print (headline)

# article = soup.find('article')
# summary = article.find('div',class_='entry-content').p.text
# print(summary)
# o/p is -->      In this video, we will be learning how to create and extract zip archives. We will start by using the zipfile module, and then we will see how to do this using the shutil module. We will learn how to do this with single files and directories, as well as learning how to use gzip as well. Let’s get started…

# vid_src  = article.find('iframe',class_='youtube-player')
# print(vid_src)
# o/p is --->  <iframe allowfullscreen="true" class="youtube-player" height="360" src="https://www.youtube.com/embed/z0gguhEmWiY?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="640"></iframe>

# vid_src  = article.find('iframe',class_='youtube-player')['src']
# print(vid_src)
# o/p is -->        https://www.youtube.com/embed/z0gguhEmWiY?version=3&rel=1&fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent

# vid_src  = article.find('iframe',class_='youtube-player')['src']
# vid_src = vid_src.split('/')
# print(vid_src)
# o/p is -->        ['https:', '', 'www.youtube.com', 'embed', 'z0gguhEmWiY?version=3&rel=1&fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent']

# vid_src  = article.find('iframe',class_='youtube-player')['src']
# vid_src = vid_src.split('/')[4]
# print(vid_src)
# o/p is --->   z0gguhEmWiY?version=3&rel=1&fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent

# vid_src  = article.find('iframe',class_='youtube-player')['src']
# vid_src = vid_src.split('/')[4].split('?')
# print(vid_src)
# o/p is -->  ['z0gguhEmWiY', 'version=3&rel=1&fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent']

# vid_src  = article.find('iframe',class_='youtube-player')['src']
# vid_src = vid_src.split('/')[4].split('?')[0]
# print(vid_src)
# o/p is --->     z0gguhEmWiY

# vid_src  = article.find('iframe',class_='youtube-player')['src']
# vid_src = vid_src.split('/')[4].split('?')[0]
# yt_link = f"www.youtube.com/watch?v={vid_src}"
# print (yt_link)
# o/p is --->  www.youtube.com/watch?v=z0gguhEmWiY

from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source,'lxml')

for article in soup.find_all('article'):
    headline  = article.h2.a.text
    print(headline)

    summary = article.find('div',class_='entry-content').p.text
    print (summary)

    try:
        yt_link = article.find('iframe',class_='youtube-player')['src']
        yt_link = yt_link.split('/')
        yt_link = yt_link[4]
        yt_link = yt_link.split('?')
        yt_link = yt_link[0]
        print (f'www.youtube.com/watch?v={yt_link}')

    except:
        print ("link not found")
    print ("\n")

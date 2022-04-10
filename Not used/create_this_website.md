Title: How to create this website
Date: 2020-06-11 08:00
Modified: 2020-06-25 10:50
Category: Computer

####



####

I removed the following from the line 248

```
{% if MAIN_MENU %}
<nav>
  <a href="{{ SITEURL }}">{{ _('Home') }}</a>

  {% for title, link in MENUITEMS %}
  <a href="{{ link }}">{{ _(title) }}</a>
  {% endfor %}

  {% if FEED_ALL_ATOM %}
  <a href="{{ FEED_DOMAIN }}/{{ FEED_ALL_ATOM }}">{{ _('Atom') }}</a>
  {% endif %}

  {% if FEED_ALL_RSS %}
  <a href="{{ FEED_DOMAIN }}/{{ FEED_ALL_RSS }}">{{ _('RSS') }}</a>
  {% endif %}
</nav>
{% endif %}
```	
	
	
#####

modify style.less text-transform to captalized


####
pasted 
```
<li>
	{% for title, link in MENUITEMS %}
<a href="{{ link }}">{{ _(title) }}</a>
</li>
```

in base.html line 212


####

copy the following into ga.html
```
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-165330920-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-165330920-1');
</script>
```



####
I actually redownload the render math function using pip. 


####
Removed copyright in `flex.html`

####

Change fonts in `variables.less`


#### 
I comment out the summary of the blog in category. 
`<!-- {% set summarise = True %}-->`
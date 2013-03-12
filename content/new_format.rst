New Blog Format
===============

:date:      3-12-2012
:author:    Marshall Ward
:category:  Meta
:tags:      blog, pelican, nginx

I may not update my blog very often, but at least I update the underlying
software. The main changes are that I've replaced `Apache`_ with `nginx`_, and
deleted the old Wordpress site. Instead, I am using `Pelican`_ as a static web
generator. I tried out several, but Pelican has been the closest to what I had
in mind. If I don't like it, then I will just modify it!

The internal directory structure on the VPS is also much tidier, but only I
would know about that (unless you are a dirty hacker).

The reason I switched to Pelican is because I wanted to move away from the
bulky database-driven format of Wordpress and get something simpler. Pelican
lets me take a manageable collection of textfiles, treating each as a
mini-essay, and then process them into some sort of blog-like website.

I'll also mirror the contents on a github site, which will act as a history for
the site.  So even if I choose to update or modify the existing articles, there
will be a track record of the modifications. Because accountability matters in
video game posts.

The biggest detriment to static web generators is the loss of user feedback
tools (comments, forums), but I didn't actually have any feedback anyway. So
there's no problem to solve! On the plus side, I've indirectly plugged up any
security holes that Wordpress could have introduced.

I am slowly working on porting over the old articles. I doubt anyone has ever
read them, so it is mostly just as an exercise to get used to Pelican.

More updates soon. Maybe I'll write up an "article" explaining the transition.

.. _`Apache`:
    http://www.apache.org

.. _`nginx`:
    http://nginx.com

.. _`Pelican`:
    https://github.com/getpelican/pelican

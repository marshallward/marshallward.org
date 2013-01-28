Useful Drupal Module
====================

:date:   2011-09-18 12:38:48
:author: Marshall Ward

Lately I have been struggling to learn how to use a Drupal site effectively.
The fact that I can get it running at all shows that it is a mostly painless
process; typical LAMP stuff. But it has been hard to find the right modules for
the job.

The main challenges at the moment have been emulating a wiki, providing
equation support, and setting up a calendar. I will leave out my experiences
with wiki emulation for now, but I will talk about what I learned about
displaying equations and calendars.

My academic background almost requires me to express equations in LaTeX under
penalty of death, so I initially tried to use DruTeX, which generates graphics
for display on the website. It worked in principle, but the permissions turned
out to be a nightmare. But through my frustration, I discovered a whole new
solution: `MathJax`_ (`with associated Drupal module`_).

Apparently there has been a lot of work in web-based equation formatting since
MathML. MathJax is an AJAX-based method for displaying equations using either
MathML or LaTeX format. The equations are formatted on the client-side
(reducing server load) and, unlike graphic files, can be rescaled on the fly.
And on top of all that, you can right-click the equation to get the source
(either LaTeX or MathML).

The calendar setup is also painless, since you just `download the required
modules`_, but configuring it can be a major hassle. Luckily, there is a
`wonderful video`_ explaining how to do it. It even explains what all of the
configuration settings do to your site. Anyone trying to configure a Drupal
calendar should definitely start here!

.. _MathJax:
    http://www.mathjax.org/

.. _with associated Drupal module:
    http://drupal.org/project/mathjax

.. _download the required modules:
    http://drupal.org/node/133341

.. _wonderful video:
    http://vimeo.com/6544779
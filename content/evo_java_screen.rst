Evo (Java) white screen problem
===============================

:date:   2011-10-13 03:34:33
:author: Marshall Ward

Since everyone in my work team is located at different cities, we use
videoconferencing for occasional meetings. The software we use is Evo, which is
a java-based application that has pretty good quality and supports multiuser
conferencing. Today, I had a problem where the application would simply not
open. All I would see is an empty white window. The problem was apparently
solved by clearing the cache. I applied `the suggestion from this post`_:

.. code-block:: bash

    javaws -Xclearcache

and it seemed to fix my problem. I don't know what caused the cache problem, or
why it was hanging, but the post says it's an issue with Ubuntu 11.04 (which is
what I'm running).

.. _the suggestion from this post:
    http://ubuntuforums.org/showthread.php?t=1827546

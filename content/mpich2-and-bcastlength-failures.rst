MPICH2 and bcastlength failures
===============================

:date:   2012-02-28 09:05:44
:author: Marshall Ward

After installing MPICH2 on my workstation, it kept consistently failing the
bcastlength test (something about detection of broadcasting a too-long array,
see `here`_. After scouring Google to see what was wrong, I found nothing.
Eventually, I broke down and subscribed to the mailing list, intending to ask
the community. But as a last ditch, I searched the archives and found `this
post`_, stating that the bcastlength is expected to fail at this time. Part of
me wonders why they didn't deactivate the test, but I am more confused why
there's no mention of this on any general Google search.

Anyway, I can ignore the problem and move on to other unproductive things.

.. _here:
    http://trac.mcs.anl.gov/projects/mpich2/browser/mpich2/trunk/test/mpi/errors/coll/bcastlength.c?rev=100

.. _this post:
    https://lists.mcs.anl.gov/mailman/htdig/mpich-discuss/2011-November/011185.html

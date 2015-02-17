Random File Permissions
=======================

:date:      2013-07-27
:author:    Marshall Ward
:category:  Linux
:tags:      linux, system calls, permissions

If we create a new file in Linux, why are the default permissions random?

At the risk of repeating myself, suppose I run the following C program three
times, where I deliberately omit the permissions (or ``mode``) argument in the
``open`` function:

.. code:: c

   #include <fcntl.h>

   int main()
   {
       int fd, ec;
       fd = open("dummy_file", O_WRONLY | O_CREAT);
       ec = close(fd);

       return 0;
    }

Each time I run the problem, the new file will have an apparently random set of
file permissions::

    -r--rwx--T   1 marshall marshall    0 Jul 26 11:15 dummy_file
    ---xrws--T   1 marshall marshall    0 Jul 26 11:16 dummy_file
    --wx--x---   1 marshall marshall    0 Jul 26 11:16 dummy_file

The usual bugbear for random behaviour is uninitialised variables. But these
days, such variables are usually specified in the BSS section, where the kernel
dutifully initializes them to zero. So what could then be causing the random
permissions?

To answer this, I had to start looking into ``libc``, the GNU C Library, where
``open`` is implemented. The answer, I believe, is due to the variable number
of arguments, and GCC implementation of the ``va_list`` struct and its support
functions.

----

When no new file is created, ``open`` only expects two arguments: the filename
and the IO flags. But whenever a new file is created, it also expects a
``mode`` argument. ``libc`` implements this using the variable argument macros
defined in ``stdargs.h``, which are ultimately implemented internally within
the ``gcc`` compiler.

By providing two pieces of information, the final input argument and the data
type of the unknown fields, the macros are capable of identify and reading the
optional arguments. I can't say how it works without looking at the ``gcc``
source, but I can only assume that it uses the ``typeof`` macro along with
various pointer arithmetic tricks to get the memory address (similar to ones
used in the Linux kernel).

But a dangerous shortcoming of the ``stdargs.h`` implementation is that there
is no intrinsic way to determine if the arguments have been provided! This must
be inferred some other way, such as from the other input arguments. For
example, ``open`` only checks for a third argument if its flags imply the
creation of a new file (e.g. ``O_CREAT``).

And this leads to the problem of random permissions. If we create a new file,
but do not provide a third argument, then ``gcc`` will *still* look at the
following memory contents and *assume* that they contain the mode permissions,
even if they were never provided!

The actual contents will depend on the assembly representation of the function,
which I don't know much about, but it probably includes some sort of reference
to another variable, or a jump statement to a particular address. These sort of
variables would depend on where the process stack was located in memory, which
could be almost anywhere, and could easily lead to a random file permission if
the contents were misinterpreted as valid data.

I think this also explains why ``icc`` always provides default permissions of
``000``. The ``open`` implementation does explicitly initialise ``mode`` to
zero before reading the third argument. This is almost pointless in ``gcc``,
since it will always overwrite the value with the presumed ``va_list``
contents. But my guess is that ``icc`` has a completely different
implementation of the ``va_list`` framework, possibly even some sort of safety
checks. I can only assume that it's better prepared to deal with the scenario
of a missing input argument.

There are still a few lingering questions here, such as the actual ``gcc``
implementation of ``va_list`` or the assembly representation of the functions,
but I am mostly sure that this explains why default permissions are random on
Linux.

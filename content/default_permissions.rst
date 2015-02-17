Default File Permissions
========================

:date:      2013-07-26
:author:    Marshall Ward
:category:  Linux
:tags:      linux, python, system calls, permissions

What are the default file permissions when creating a new Linux file?

Most documentation describes the permissions as "unpredictable", which usually
means quasi-random. If I create a new file in C and compile it using ``gcc``,
then permissions do appear to be random:

.. code:: c

   #include <fcntl.h>

   int main()
   {
       int fd, ec;
       fd = open("dummy_file", O_WRONLY | O_CREAT);
       ec = close(fd);

       return 0;
    }

Three successive runs of this program show three different permissions
(even the "exotic" ones like sticky bits and set[ug]id)::

    -r--rwx--T   1 marshall marshall    0 Jul 26 11:15 dummy_file
    ---xrws--T   1 marshall marshall    0 Jul 26 11:16 dummy_file
    --wx--x---   1 marshall marshall    0 Jul 26 11:16 dummy_file

(Note: Since ``O_CREAT`` doesn't replace an existing file, I have to delete it
each time.)

The result is different if I use Intel's compiler::

    ----------   1 marshall marshall     0 Jul 26 11:17 dummy_file

Any new file defaults to no permissions.

The story is a little different if I create a file using Python. If I use
Python's ``open`` function:

.. code:: python

   f = open('dummy_file', 'w')
   f.close()

then default is all-read/write but no execution (``0666``)::

   -rw-rw-rw-   1 marshall marshall    0 Jul 26 11:53 dummy_file

But if I use the more primitive ``os`` (actually ``posix``) module function:

.. code:: python

   import os
   fd = os.open('dummy_file', O_WRONLY | O_CREAT)
   os.close(fd)

then I create a completely open file without "exotic" permissions (``0777``)::

   -rwxrwxrwx   1 marshall marshall    0 Jul 26 11:54 dummy_file

The differences in the Python behaviour can be explained by looking at the
CPython implementation. The ``open`` and ``os.open`` functions use completely
independent functions (``fileio_init`` and ``posix_open``, respectively) with
each containing its own call to the POSIX C ``open``. And each just happens to
enforce a different default permission for new files.

(Note that a nonzero ``umask`` will change these results by disabling any
specified permissions.)

I don't know why CPython's ``fileio_init`` and ``posix_open`` don't share more
code. Maybe it's just simpler to keep them separate for other reasons, such as
OS interoperability.

More importantly, I also don't know why ``gcc`` produces random permissions, or
how ``icc`` manages to produce a different result, since it seems to be using
the same ``libc`` as ``gcc``.

``gcc``::

    linux-vdso.so.1 =>  (0x00007fffa239e000)
    libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fec40e20000)
    /lib64/ld-linux-x86-64.so.2 (0x00007fec41207000)

``icc``::

    linux-vdso.so.1 =>  (0x00007fff77bd4000)
    libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007ff31ebb4000)
    libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007ff31e99d000)
    libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007ff31e5de000)
    libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007ff31e3da000)
    /lib64/ld-linux-x86-64.so.2 (0x00007ff31eed8000)

Most of this is not too important for programmers, since any Linux system
programming manual will impress the importance of setting the permissions
explicitly. But at least I know what to expect if I ever forget and get
confused about unexpected file permissions.

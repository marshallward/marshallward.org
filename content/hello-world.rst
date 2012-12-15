Are we having fun yet?
======================

:date:   2011-05-16 06:28:48
:author: Marshall Ward

Hello, this is my new blog where I will write about my life, including my
transition from academics to the IT world. I expect that this will mostly be a
documentation of the various tips and surprises that I learn every day as I
focus on computing. It might be an interesting resource for others, but the
main purpose will be to help me reinforce what I have learned.

Elizabeth and I are also leaving for a trip to Japan and Korea in a few days,
so I thought that it would be a good time to start a blog. I've decided to run
this blog on a virtual server, to give myself a bit of practice at system
administration. I found a very nice VPS from `Jumba`_, which offer a simple
10GB server for $10/month, an incredible rate for an Aussie ISP. Yes, the
server does appear to be physically located in Sydney, based on a traceroute,
and the performance has been great.

I've already learned one small lesson about system administration: creating a
user is a two-step process, not one step as I had always assumed. First, you
create the user (e.g. bobdobbs):

.. code::

   useradd bobdobbs

But then you have to create their home directory:

.. code::

   mkdir /home/bobdobbs
   chown bobdobbs:users /home/bobdobbs

I was surprised that this wasn't automatic, but I think that there are reasons
for creating users without home directories. I think I saw users associated
with daemons such as sshd in the config files.

My next challenge is to get the server to recognise FTPS (FTP using TLS/SSL) so
that I can update Wordpress (the software behind this blog) through the web
interface. Until then, I am stuck with the boring default layouts.

Anyway, I am just glad that I was able to get this up and running. Hopefully I
will find the time to write about my trip while I am overseas. Please don't rob
my house while I am away.

Update: Apparently debian supports a higher level command, ``adduser``, which
does everything in a single step. I have a lot to learn!

.. _Jumba:
    http://www.jumba.com.au/

Heap or stack?
==============

:date:   2011-07-26 13:06:23
:author: Marshall Ward

After a visit to UNSW last Friday, the subject of using stack or heap memory
for a climate model came up, with my host promoting use of the stack for all
variables, including basic field variables like velocity or temperature. The
issue surprised me a bit because I had never considered using stack memory for
large numerical simulations. I had never  used anything but heap memory through
static or dynamic allocation, and generally associated the stack with smaller
call-by-value functions that are more typical in C programs.

In order to create a variable for use in the stack, one would essentially run
the ``main()`` program loop through a larger wrapper program, such as shown
here:

.. code:: fortran

   program model
     call read_parameters(M,N)
     call main(M,N)
   end program model

   subroutine main(N)
     integer, intent(in) :: M, N
     real :: u(M, N), v(M, N), T(M, N)

     ! Run your model time loop
   end subroutine main

In principle, all of the variables are automatically created during runtime and
would normally be created in the stack after the ``main()`` function call. On
the other hand, a typical use of heap memory would rely on direct allocation
calls and would look more like this:

.. code:: fortran

   program model
     integer :: M, N
     real, allocatable :: u, v, T

     call read_parameters(M, N)
     allocate(u(M, N)); allocate(v(M, N)); allocate(T(M, N))

     ! Run your model time loop
   end program model

In this case, the variables should be manually allocated in the heap and would
rest in the top-level of the code.

After reading around a bit, it looks like the Fortran standard doesn't insist
on where compilers place variables in memory, and that some compilers may in
fact place a variable in the heap if they are large enough, regardless of
whether it was allocated manually or created automatically by the function. But
even if we ignore this issue, I think it's still interesting to consider if
there is an advantage to storing variables in the stack or the heap.

My guess is that it won't matter in a climate model. Most of the arguments for
or against stack memory have to do with either

* *allocation*: stack memory can be allocated more quickly than a
  heap, since it just requires shift of a stack pointer, or

* *memory management*: variables pushed onto a stack always remain in
  a continuous stack with no gaps inbetween, while a heap must try to determine
  how to fit any new variables in the available space; in other words, memory
  fragmentation.

(Coincidentally, there was a popular `reddit post today arguing against overuse
of malloc`_, the C equivalent of heap memory).

These issues make strong arguments for using the stack in smaller applications
on a typical PC, where applications risk crashing into each other and memory
leaks can lead to a mysterious drain of available RAM. But I'm not sure that
either issue is relevant to most climate models. Usually, the models require so
much memory and CPU time that they tend to be the only applications running on
the computer, and can even fill the entire memory map on their own.
Additionally, most of the variables are created during initialization, and are
accessed and updated continuously throughout the simulation. So allocation
occurs only once, at the very beginning of the model run, so it also tends to
remain highly organised within the heap. So neither argument seems to be
relevant to climate codes.

The general advice I was taught is that small, short-term variables are best
placed in the stack, while large, long-term variables are best placed in the
heap. The unique circumstances of a climate model, along with the perpetual
call-by-reference nature of Fortran variables, suggest to me that it doesn't
matter which framework you use. But I still think that it's in the modeller's
best interest to place the largest data vectors into the heap and to keep
temporary variables or configuration data in the stack, if only because it's
closer to the original intent of most OS memory models. There are also direct
advantages. Heap-style variables are more easily accessible across the code
abstraction levels (which can be a good or bad thing, depending on how
defensive a programmer you are). Additionally, it means that the user doesn't
have to set an enormously large stacksize limit in the operating system.

But I would be interested to know if there are other arguments in favour of the
stack approach, and will keep an eye out for other discussions on the issue.

.. _reddit post today arguing against overuse of malloc:
    http://altdevblogaday.com/2011/02/12/alternatives-to-malloc-and-new/

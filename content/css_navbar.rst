====================================
Horizontal Mouseover Submenus in CSS
====================================

:date:      12-03-2013
:author:    Marshall Ward
:category:  Web
:tags:      css, html, web

In this document, I provide instructions on how to make a horizontal
navigational bar with mouseover submenus using CSS. This is also an attempt to
documents things as I learn, so expect frequent updates.


HTML example template
=====================
In the example below, we isolate the components within a top-level ``nav``
element and construct the navigational bar as a ``ul`` element (unordered
list), such as in the HTML block shown below:

.. code:: html

   <header>
     <nav>
       <ul>
         <li>
           Programming
           <ul>
             <li>Python</li>
             <li>Fortran</li>
             <li>Java</li>
           </ul>
         </li>
         <li>About</li>
         <li>
           Authors
           <ul>
             <li>Marshall</li>
             <li>Evil Marshall</li>
           </ul>
         </li>
       </ul>
     </header>


CSS Elements
============
Here I introduce each CSS element definition and how to iterate towards a
horizontal navigation bar with vertical submenus on mouseover.

1. First set the top ``li`` element display as ``inline`` rather than
   ``list-item``:

   .. code:: css

      nav ul li {
          display: inline;
      }

   This places each list element as ``inline``, while still preserving default
   list spacing. It also removes most standard list features, such as markers.

   However, any new sublist ``ul`` elements will start new display blocks,
   causing any subsequent top-level ``li`` to appear below each sublist.

2. Set menu ``li`` element positions as ``relative``, so that the containing
   sublists are positioned relative to the ``li``. This will not change
   anything yet, but ensures that the sublists keep their original position.

   .. code:: css

      nav ul li {
          display: inline;
          position: relative;
      }

3. Now fix the sublist ``ul`` positions as ``absolute`` (relative to the parent
   ``li``), so that they are fixed below each element.

   .. code:: css

      nav ul li ul {
          position: absolute;
      }

   At this point, the submenus should now be arranged properly, with submenus
   arranged vertically below the parent horizontal menu.
   
   The submenu ``li`` elements are still ``inline``, which would normally
   arrange them in a horizontal row. But since the parent ``ul`` submenu
   position is relative, the submenu ``li`` retains its original (vertical)
   positions.  *(At least, I think that's what's going on.)*

   If you want to be more explicit, then you can display the submenu ``li`` as
   ``block``:

   .. code:: css

      nav ul li ul li {
          display: block;
      }

    But as far as I know, this isn't necessary.

4. Finally, it's time to enable the mouseover menus. First disable the submenus
   on default:

   .. code:: css

      nav ul li ul {
          display: none;
          position: absolute;
      }

   Then re-enable display on mouseover:

   .. code:: css

      nav ul li: hover > ul {
          display: block;
      }

   After that, the minimal mouseover menus are complete!

Once it's working, you can start stylizing the menus. One simple addition is to
remove padding from the submenus:

.. code:: css

   nav ul li ul {
       display: none;
       padding: 0;
       position: absolute;
   }

so that the ``ul`` submenus remain aligned with the parent ``li``.


Alternative approaches
======================
Like most CSS layouts, there are an almost uncountable number of ways to get a
similar (if not identical) layout. Below I mention some of the other solutions,
and why I chose not to use them.


Floating list elements
----------------------
This seems to be the most popular method of creating a horizontal list. Instead
of relying on ``inline`` or ``block`` layouts, you could use something like
this:

.. code:: css 

   nav ul li {
       float: left;
   }

There are several disadvantages here though:

* The ``li`` elements are floated below the ``nav`` element, rather than within
  it, and cannot inherit its parent properties, such as background colour.
  
* Any padding is removed from the floated ``li`` elements, and must padded
  explicitly.

* The next element after the list (usually a ``div`` or ``section``) is floated
  directly to the right of the final ``li`` element, unless one applies a
  ``clear: left`` (or ``both``).

We avoid all of these issues by not using ``float``, and retain better style
control over individual elements.

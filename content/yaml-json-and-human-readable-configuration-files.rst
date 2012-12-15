YAML, JSON and human-readable configuration files
=================================================

:date:   2011-07-01 10:10:37
:author: Marshall Ward

There are many headaches involved in using climate models. One is usually
required to compile and build the programs themselves, and there is usually a
dependence on at least a few external libraries, such as NetCDF or MPI support.
Data formats can be peculiar and poorly documented, and modifying the behaviour
of the model usually means manipulating the source code, which is more often
than not written in Fortran 77. My own pet peeve, however, is the configuration
files used to drive climate models. Nearly every model is controlled through
some text files fed through a Fortran parser, which can't usually manage much
more than &lt;variable&gt; &lt;value&gt; separated by carriage returns.
Occasionally one will encounter the namelist files, which are simply a
serialised list of Fortran variables written in a Fortran-readable format.
These files are only as readable as your typical bit of Fortran source code,
which essentially restricts you to Fortran formatting and layout.

Because configuration files can be difficult to read, navigate, and modify, I'd
like to see a more human-readable format for the model user. At first I
considered something like XML, which has the advantage of popularity and
standardisation, but XML is not always very readable or modifiable due to the
immense amount of markup.

It seems that I'm not the only one to feel this way. There appear to be two
popular standards for human-readable markup in text files. `JSON`_, which grew
out of Javascript, appears to be like a stripped-down version of XML and allows
some basic structured variables. It looks a lot like C, with everything blocked
in {curly brackets}. `YAML`_ is essentially a superset of JSON, supporting
more elaborate data structure, and is more like Python in appearance (including
its dictionary support), formatted by whitespace.

After using Python actively for a year, my preference is for something like
YAML, at least in appearance. If you don't format your whitespace, then your
document isn't human-readable anyway, so the whitespace essentially becomes a
self-correcting feature in the file. YAML can also do everything that JSON does
(`by definition`_). The only drawback is that there appears to be better
support for JSON, including embedded support in HTML5. But from the perspective
of climate modelling there is probably very little Fortran support for either
standard.

I don't know how realistic it would be to use either of these schemes. I have
never heard about a JSON or YAML parser for Fortran, and it may not end up
being much more readable than your typical model configuration file. But it
would be a move to a standardised format, and if a parser were developed then
all models could use the same libraries for configuration, and could possibly
even start sharing variable sets and names. It would allow us to focus less on
the individual quirks of the models and more on the underlying mathematical and
physical assumptions.

.. _JSON:
    http://en.wikipedia.org/wiki/JSON

.. _YAML:
    http://en.wikipedia.org/wiki/YAML

.. _by definition:
    http://en.wikipedia.org/wiki/YAML#JSON

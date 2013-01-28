Rambo NES doesn't use Zelda 2 code
==================================

:category: Gaming
:author: Marshall Ward
:date: 2013-01-28 17:23
:tags: nes rambo zelda bsdiff

I occasionally read rumours that Rambo for the NES used code from
Zelda 2, making it not much more than a ROM hack of the original cartridge.
The clearest statement of this rumour is the `about.com review of the game`__,
but I have also read this on various forums.

A cursory glance of the two games suggests that they may have a lot in common.
Both feature a 16x32 sprite protagonist who makes high vertical leaps and
attacks with a dagger-like weapon (even if Link is supposed to be wielding a
sword). But the gameplay of the two definitely feels different. Rambo's jumps
are higher and less parabolic, the knockback is more uncontrollable, and the
collision detection of his attacks is far worse than the strong dueling sense
we get from Link. Rambo combat is the typical bash and leap combat from early
NES games.

But just to be sure, I decided to put this theory to the test by using Colin
Percival's `bsdiff`_ tool on the two ROMs. Each ROM was from the GoodSet
collection, so the bitwise accuracy of each ROM is nearly perfect. I compared
the US version of Zelda 2 to both the US and Japanese release of each game, and
found exactly what I expected: There is no difference between the code between
the two. The only contigous match in the ROMS are various streams of zeros and
ones ("FF") throughout the ROM, neither of which is significant of anything
other than unused space in the ROM.

For posterity, this is the command that I ran::

    bsdiff -cb rambo.nes zelda.nes


So as far as I'm concerned, the two games have nothing more in common than a
shared gaming style. Maybe the programmers of Pack-In-Video were trying their
best to reproduce the Zelda 2 experience, but it looks like it was never more
than a stylistic emulation. There is no common code here, much less a shared
"engine" between the two.

__ http://classicgames.about.com/od/consoleandhandheldgames/fr/RamboNESReview.htm
.. _bsdiff: http://www.daemonology.net/bsdiff/

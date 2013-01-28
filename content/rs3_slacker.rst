Slacker Pin's "Tool Around" Ability (partially) Explained
=========================================================

:date:   2012-07-13 13:35:07
:author: Marshall Ward

After playing Penny Arcade Adventures: `On the Rain-Slick Precipice of Darkness
3`_, I got very interested in the "Slacker" pin's "Tool Around" ability. After
a few minutes with a disassembler, and a few hours sorting through the mess, I
managed to work out most of it to the best of my ability. This is what I came
up with.

"Tool Around" applies a randomly selected attack from a hidden list in the
game. The effect is based primarily on your level, which is outlined below in
more detail.

1. First, a maximum random number value is determined based on your Slacker
   level. Specifically, 
  
.. code:: c

   rand_max = max(1, MyJob["Slacker"].LV / 4)

2. Once the maximum random number has been determined, a random number is
   generated between ``0`` and ``(rand_max - 1)``.

However, if this number matches the previous number, then it attempts to
determine another number. In other words, you will not get the same attack
twice. (An exception is made for ``rand_max = 1``, which always produces a
random number equal to zero).

Once the number is determined, the ability is then selected from the table
listed below.

The range is determined by level. If you are level 6, then you can only get
effect 0 ("Do Nothing"). If you are level 20, then you can get any of the first
five effects (except the one from your previous attack). It does not matter how
often the ability was used, as suggested in the forums.

Most of the abilities apply some sort of damage. The base damage is roughly
proportional to your level:

.. code:: c

   Power = PowerBase * (5 + JobLevel) / 25

although various other effects will modify the eventual damage.

The abilities are as follows:

0. "Do Nothing"
   Apty named, this attack does nothing.

1. "Whatever"
   This attacks a random target of base damange 0.6*Power.

2. "Zen"
   This cures the caster of any status ailments.

3. "Harsh"
   This is a slightly stronger attack, causing 1.8*Power damage (or 3x stronger
   than "Whatever").

4. "Herb"
   This appears to heal the caster to full HP, and to cure any status ailments.
   It also may amplify magic by 35%, although it's difficult to tell from the
   code.

5. "My New Band"
   Another random attack, applying 2.4*Power damage (or 4x "Whatever")

6. "Daydream"
   This appears to add a buff which increases magic power by 75%, but it's hard to
   tell.

7. "Bohomoth"
   Another more powerful attack, it does 4.8*Power base damage (or 8x "Whatever")

8. "Hookah"
   This seems to heal all party members to maximum HP.

   It also appears to apply the same 35% magic bonus from "Herb".

9. "Whatever"
   This has the same name as "Whatever", but it does a massive 9.6*Power damage
   (or 16x the base "Whatever" attack)

.. _On the Rain-Slick Precipice of Darkness 3:
    http://rainslick.com/

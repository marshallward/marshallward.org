Avoiding Utility Classes
========================

:date:   2012-05-21 07:12:23
:author: Marshall Ward

My journey from science to computer science consists mostly of very small
victories, so I don't always recognise everything that I've learned as it
happens. But in C#, my first serious attempt at object-oriented programming,
the lessons are occasionally more acute. In the space of about a week, I
discovered the power of Utility classes, followed by several discussions about
how they should never be used, finally learning how to get the same utility
without Utility classes.

This is my interpretation of the Utility class dilemma. I'm sure it is not a
new story, but by rehashing it in my mind, I hope to better learn the lesson.

If you have two classes A and B, and have a method ``f()`` that both must use,
then the most naive approach is to repeat the function as a method in both
classes.  However, this violates the "Don't repeat yourself" (DRY) approach to
programming. It's not just about reducing work: if both classes truly need the
same function, then it should be the same function. If you change ``f()``, then
A and B ought to behave identically. And it's not just based on principle: if
you change ``f`` in A but forget to change ``f`` in B, then you potentially
break your program. Relationships between classes should be explicit.

The most natural solution is inheritance, but it's not always beneficial for A
and B to be subclasses of some parent class. In my case, A was already a
subclass of another class, while B was not. There was no way to make A and B
subclasses of a parent class without breaking that other relationship.

The alternative is to define the "Utility" class: a public static class that
sits in the global namespace, awaiting anyone to "borrow" them. They are not
bad in themselves, but they do imply relationships between your data that are
not explicitly defined. Also, if your static class has any static variables,
then A and B never really know what they're getting into when they use it.

In my case, the solution was to use interfaces. My only requirement was that
methods in A and B needed to have a field called Name. This is weak grounds to
create a class relationship. So I created a ``IName`` interface, so that any
class choosing to implement this interface had a Name. A and B could retain
their independence, but still operate under the assumption of a ``Name`` field.

That wasn't the end of the story. It got a little more complicated because I
eventually wanted an internal method to change Name in exceptional cases, even
though I wanted it to remain private. I gradually learned that this was not
possible under my current design, and I almost gave up and made the method a
utility class. But eventually, I recognised that this wasn't the solution. If I
really did want a private field and a common method to change them, then A and
B needed a relationship to permit this action. I eventually recognised this and
found an alternative design that did not require changes to "Name". In other
words, I settled on a design - the one that best represented the relationship
that I wanted - and worked within this design choice.

I still find object-oriented programming a little bewildering. For every
"right" decision, there are a thousand "wrong" decisions, and little feedback
to indicate the quality of your design. C# limits your behaviour in ways that
C++ does not, and so it's a much better platform for learning the concepts. As
I continue to practice, I become more comfortable with my design choices, and I
see less flaws in my work than I used to, so I guess that is progress.

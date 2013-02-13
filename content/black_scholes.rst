========================
Black-Scholes Derivation
========================

:Author:    Marshall Ward
:Contact:   mail@marshallward.org
:Date:      2013-01-30

Introduction
============
I found it difficult to follow many of the derivations of the Black-Scholes
option pricing formula. Most get the stochastic details correct, but they all
seem to be a bit loose in their definitions of the portfolio. So this is my
attempt to document a derivation that I could reference comfortably.


Defining the Portfolio
======================
Define a portfolio :math:`\Pi` which is defined as:

.. math::

    \Pi = V + S \Delta + C

so that the total value of the portfolio consists of the following assets:

* :math:`V`, the value of a single option
* :math:`S`, the value of a single share of same asset, and the only stochastic
  variable in the model.
* :math:`\Delta`, the number of shares held of this asset
* :math:`C`, the amount of cash on hand

Both :math:`\Delta` and :math:`C` can be negative (via buying short or
borrowing).

The Black-Scholes formula seeks to define a value of the option :math:`V` which
eliminates any dependence on volatility (or randomness) in the asset price
:math:`S` under a particular set of constraints. This requires tracking the
time series of :math:`S` as well as buying and selling shares :math:`\Delta` to
offset the volatility of :math:`S`.

First consider a differential change in the portfolio value, :math:`d\Pi`,

.. math::

    d\Pi = dV + \Delta dS + S d\Delta + dC.

The change in cash over time consists of any interest gained at a some
idealised market-competitive interest rate :math:`r`, minus the number of
shares purchased:

.. math::

    dC = r C dt - S d\Delta

so that the change in portfolio value over time is

.. math::

    d\Pi = dV + \Delta dS + r C dt.


Modelling the Asset Price
=========================
We presume that :math:`V` depends only on the current asset price :math:`S` and
the time :math:`t`, so that :math:`V = V(S, t)`. Since :math:`S` is a
stochastic variable, :math:`V` is also stochastic and the differential change
in :math:`V` is

.. math::

    dV = \frac{\partial V}{\partial t} dt + \frac{\partial V}{\partial S} dS
        + \frac{1}{2} \frac{\partial^2 V}{\partial S^2} (dS)^2.

We also introduce an assumption about the stochastic form of the asset price,
namely that it follows a geometric random walk:

.. math::

    dS = \mu S dt + \sigma S dW

where

* :math:`\mu` is the deterministic growth rate
* :math:`\sigma` is a stochastic variance relative to :math:`S`
* :math:`dW` is the Wiener random walk displacement.

Using this result, the :math:`V` differential becomes

.. math::

    dV = \left( \frac{\partial V}{\partial t}
            + \mu S \frac{\partial V}{\partial S}
            + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}
         \right) dt
          + \sigma S \frac{\partial V}{\partial S} dW

When these are combined and applied to the portfolio differential, it becomes

.. math::

    d\Pi = \left( \frac{\partial V}{\partial t}
            + \mu S \left( \frac{\partial V}{\partial S} + \Delta \right)
            + \frac{1}{2} \mu^2 S^2 \frac{\partial^2 V}{\partial S^2}
           \right) dt
            + \left( \frac{\partial V}{\partial S} + \Delta \right) dW
            + r C dt.

The equation shows that we can eliminate all volatility from the portfolio if
we purchase or sell shares in response to changes in the option price relative
to share price. That is,

.. math::

    \Delta = - \frac{\partial V}{\partial S}

This would require us to sell short (:math:`\Delta < 0`) if the option price
rises relative to the asset price. It also assumes that we have available cash
:math:`C` to make such purchases, which may require borrowing (:math:`C < 0`)
at the market rate :math:`r`.

If we purchase or sell shares in accordance with the non-volatility rule, then
the portfolio value should evolve deterministically, so that

.. math::

    d\Pi = \left( \frac{\partial V}{\partial t}
            + \frac{1}{2} \mu^2 S^2 \frac{\partial^2 V}{\partial S^2} + r C
           \right) dt

Although this differential form provides a deterministic method for predicting
the portfolio value, it requires that we know the option price :math:`V`, which
was the original intent of this analysis.

The real utility of this expression is to relate the change in option value to
a presumed market growth rate of the portfolio, from which we can derive a
particular form of the option price :math:`V`.


Portfolio Arbitrage
===================
The final major assumption of the Black-Scholes equation is the trend towards
*arbitrage*, or an equilibrium in market trading. In other words, you assume
that trading occurs at or near a point where no party has a price advantage. In
the Black-Scholes model, this translates to a portfolio that grows at the
market-competitve interest rate, :math:`r`:

.. math::

    d\Pi = r \Pi dt.

Using this and the expression for portfolio growth, we can construct a single
equation in :math:`V`:

.. math::

    r \left( V + S \Delta + C \right) dt
        = \left( \frac{\partial V}{\partial t}
            + \frac{1}{2} \mu^2 S^2 \frac{\partial^2 V}{\partial S^2} + r C
          \right) dt

After various substitutions, we can construct a well-defined partial
differential equation for the option price :math:`V`:

.. math::

    \frac{\partial V}{\partial t}
        + \frac{1}{2} \mu^2 S^2 \frac{\partial^2 V}{\partial S^2}
        = r \left( V - S \frac{\partial V}{\partial S} \right)

Along with the appopriate boundary conditions, solutions to this equation
indicate what is a "fair" price for an option to buy an asset at price
:math:`S` at a given time :math:`t`.


Disclaimers
===========
Aside from the assumptions of a simplistic market, the following assumptions
are required to derive the Black-Scholes option pricing model:

* Geometric Brownian motion: :math:`dS = \mu S dt + \sigma S dW`

* Non-volatile trading: :math:`\Delta = -( \partial V / \partial S )`

* Arbitrage market growth: :math:`d\Pi = r \Pi dt`

Any of these assumptions can be questioned, or modified to produce a slightly
different theory, including theories where it is not possible to eliminate
volatility.

I also have not thought much about the "European" versus "American" options, or
any of the other variants. I also haven't thought about the issue of
appropriate boundary conditions. As a "negative diffusive" equation, it's the
final value that most influences the value, rather than the initial value,

My main goal was to simply understand the derivation of the model. Most
references get the mathematics right, but they seem to be very sloppy in their
definition of the portfolio. Many ignore the role of the available cash,
:math:`C`, while others make confusing assumptions like a "fixed" number of
shares :math:`\Delta`, even though :math:`\Delta` must be able to change in
response to changes in :math:`S` (and consequently :math:`V`).

*(I also wanted to try and write a proper document in reStructuredText with
both inline equations and equation blocks. It seems to have turned out very
nice!)*

This derivation was effectively taken from the parabolic PDE chapter of the
`Applied Partial Differential Equations`_ textbook.

.. _Applied Partial Differential Equations:
    http://books.google.com/books/about/Applied_Partial_Differential_Equations.html?id=CdA6jcJWCToC&redir_esc=y

Existing curves
===============
### Retail curve
The joystick curve found in the retail game's source.

    n(x) = (9-x)/9
    f(I) = I*(s/9)+(I^5)*n(s)

![Retail curve](retail.png "Retail curve")

### Current curve for Windows version
The Windows version of `joy.cpp` got a new curve at some point.

    f(I) = I^(3-(s/4.5))

![Windows curve](windows.png "Windows curve")

Suggestions for new curves
===========================
The following curves will be added for testing.

### Herra's suggestion
Adapted from http://www.hard-light.net/forums/index.php?topic=67633.msg1336430#msg1336430

    f(I) = I^(s/9)*((1-cos(I*π))/2)^((9-s)/9)


![HerraTohtori (9)](herra_9.png "HerraTohtori (9)")

Alternatively, a wider range of curves can be achieved by a small change in the last exponent.

    f(I) = I^(s/9)*((1-cos(I*π))/2)^((9-s)/4.5)

![HerraTohtori (4.5)](herra_4.5.png "HerraTohtori (4.5)")

### Exponential curve (WIP)

    f(I) = (exp(I)-1)/(exp(1)-1)

NB: Requires sensitivity parameter - might not make the final cut.

![Exponential curve](exponential.png "Exponential curve")

### Logistic based (sigmoidal):

    S(x) = 1/(1+exp((8-s)*(-x+0.5)))

    f(I) = (S(I)-S(0))/(S(1)-S(0))

![Logistic curve](logistic.png "Logistic curve")

### Mixed curve
*Yet another Herra suggestion.*
Starts with an exponential shape at `s<5`, becomes linear at `s=5`, then becomes logarithmic at `s>5`.

    f(x) = I^(1+((5-s)/9))

NB: The linear point (5) might be changed.

![Mixed curve](mixed.png "Mixed curve")

### Polynomial

    f(I) = I*I^((9-s)/9)

NB: **Redundant**. The entire behaviour of this curve can be achieved with a subset of sensitivity settings `s` on the current Windows curve.

![Polynomial curve](polynomial.png "Polynomial curve")

List of symbols
===============

    I    : input percent (position of joystick on half-axis).
    s    : in-game sensitivity setting [0..9].
    f(I) : translation of input percent to output (the result of the curve function).

---
title: Spatial Mass distributions and Galactic Stability
author: 
description: Canonical use of marpx theme
keywords: [Marp, MarpX, Gödel, Paulo Cunha]

header:

marp: true
theme: einstein
paginate: true
transition: fade

size: 16:9
lang: en
math: mathjax
---
<!-- _class: title-academic -->
<!-- _backgroundColor: white  -->
<div class="title">Spatial Mass distributions and Galactic Stability</div>
<div class="subtitle">Advisor: Yuan Shi</div>
<div class="author">Jonah Cooke</div>
<div class="date">Mar. 5th 2026</div>
<div class="organization">Yuan Shi, Plasma Quantum Group</div>

---
<!-- _class: toc  -->

1. [The Problem](#3)
2. [Whats been tried](#4)
3. [What I'm trying](#5)
4. [why I'm trying it](#6-7)
5. [the process](#6-7)
6. [where Im at](#8)
7. [Next steps](#9)
8. [Ideas for future](#10)
9. [References, Appendix & Credits](#11)
---
# The Problem
<!-- _class: multicolumn -->
<div>
Via newtonian mechanics and a gausian integral we expect the velocity distribution of galaxies to look like:

The data shows it follows a curve like:

</div><div>

![h:400 center](./assets/images/math/puebk.png)
![h:185](./assets/images/math/math005.png)
<br><span class="figcaption">Math005.</
</div>

---

<!-- _class: multicolumn -->
<!-- _backgroundColor: black  -->
# Whats been Tried
<div>
<center>

Newtonian physics

$$F = -\frac{GMm}{r^2}\hat{r} $$

<video width="600" height="400" autoplay loop muted>
  <source src="newtonian.mp4" type="video/mp4">
</video>
</center>
</div><div>
<center>

General Relativistic 
$$R^\lambda_{\:\:\gamma\alpha}$$
<video width="600" height="400" autoplay loop muted>
  <source src="precesion_fade.mp4" type="video/mp4">
</video>
</center>
</div>
<!-- _footer: Code modified from  -->

---
# What I am trying
<!-- _class: multicolumn -->
<!-- _backgroundColor: black  -->
<div>
<center>
Variable mass:

$$M(r) \propto \sqrt{r} $$ 


<video width="600" height="400" autoplay loop muted>
  <source src="orbit.mp4" type="video/mp4">
</video>
</center>
</div><div>
<center>
Constant mass:

$$M(r) \propto M $$ 


<video width="600" height="400" autoplay loop muted>
  <source src="orbit_2.mp4" type="video/mp4">
</video>
</center>
</div>

---

# Why I am trying it do
- light traveling through plasma
$$\omega^2=\omega_p^2+k^2 \Longleftrightarrow E^2=m^2+p^2$$
- plasma frequency
$$\omega_p^2 = \frac{e^2 n(r)}{\epsilon_0m}$$
 - Since $n=n(r)$, maybe $m=m(r)$

---
# Why I am trying it cont.
<center>

$$\omega^2=\omega_p^2+k^2 $$

</center>
 Light incedent on plama

- $\Delta E = 0 \Rightarrow \Delta \omega = 0 \Rightarrow-\Delta\omega_{p}^2=\Delta k^2$

- In the case $\Delta v < 0 \Rightarrow \Delta\omega_{p}^2>0$
- Since $\omega_{p} \propto n \Rightarrow \Delta n>0$



---
# Why I am trying it cont.

<center>

$$\omega_p^2 = \frac{e^2 n(r)}{\epsilon_0m}$$

</center>

- $\Delta n > 0\Rightarrow n_1-n_1\frac{\sin(\theta_1)}{\sin(\theta_2)} > 0$
- $n_1-n_1\frac{\sin(\theta_1)}{\sin(\theta_2)} = \frac{n_1}{\sin(\theta_2)}(\sin(\theta_2)-\sin(\theta_1))$
- since $\theta_1, \theta_2 \in [0, \frac{\pi}{2}]$ for $\Delta n >0,\: \sin(\theta_2)>\sin(\theta_1)$ 
- for the domain $[0, \frac{\pi}{2}]$ this implies: $\quad\theta_2>\theta_1$
---
# The process
$$\mathcal{L} = \mu(r)\frac{\dot r^2}{2}+\mu(r)\frac{r^2\dot \phi^2}{2}- U(r)$$
$$\frac{\partial\mathcal{L}}{\partial{r}}=\frac{d}{dt}\frac{\partial\mathcal{L}}{\partial\dot{r}},\quad\frac{\partial\mathcal{L}}{\partial{\phi}}=\frac{d}{dt}\frac{\partial\mathcal{L}}{\partial\dot{\phi}}$$

---
# where I'm at
---

# Next steps

<!-- _footer: Vídeo de Nikolay Sobolev no Pexels: https://www.pexels.com/pt-br/video/ar-aviao-aeronave-aeroporto-16127349/ -->

---
# Ideas for future
Gravitational Lensing

---


<!-- _class: black-slide -->
# code
```python
import pygame
import numpy
```
---
---
# Appendix

## Bibliography, References, Appendix. etc.
<!-- _footer: Vídeo de Nikolay Sobolev no Pexels: https://www.pexels.com/pt-br/video/ar-aviao-aeronave-aeroporto-16127349/ -->
---

<!-- _class: "references" -->

# References

<div class="multicolumn"><div>

1. 

</div><div>

7. HEIDEGGER, Martin. **Sein und Zeit**. 11. ed. Tübingen: Max Niemeyer Verlag, 1967.

</div></div>

---

[![bg left:50%](https://images.pexels.com/photos/31586773/pexels-photo-31586773.jpeg)]()

<style scoped>
h2>a{
  color: red;
}
</style>

<!-- _class: blank -->

<div align="center">

# <!-- fit --> [Back to the](#1)

## <!-- fit --> [beginning](#1)

</div>
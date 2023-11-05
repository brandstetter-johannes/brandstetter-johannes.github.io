---
title: Data-Driven Simulations
summary: I am firmly convinced that AI is on the cusp of disrupting simulations at industry-scale. Therefore, I have started a new group at JKU Linz which has strong computer vision, simulation, and engineering components. My vision is shaped by experience both from university and from industry.
tags:
  - Learning2Simulate
  - AI4Science
  - AI4Engineering
  - Partial Differential Equations
  - Neural Solvers
  - Geometric Deep Learning
  - Deep Learning
date: '2023-10-01'

# Optional external URL for project (replaces project detail page).
external_link: ''

image:
  caption: AI is on the cusp of disrupting simulations at industry-scale
  focal_point: Smart

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides: example
---

My years in Amsterdam -- first at the [Amsterdam Machine Learning Lab](https://amlab.science.uva.nl/) and then 2 years at in the [AI4Science lab](https://www.microsoft.com/en-us/research/lab/microsoft-research-ai4science/) at Microsoft Research -- have shaped my research vision. I am firmly convinced that AI is on the cusp of disrupting simulations at industry-scale. Therefore, I have started a new group at JKU Linz which has strong computer vision, numerical simulation, and engineering components. We want to advance data-driven simulations at industry-scale, and place the Austrian industry engine Linz as a center for doing that.

# About my research

Working in [high energy physics](https://brandstetter-johannes.github.io/tag/high-energy-physics/) means to make the invisible visible. When we published for example the [first direct observation of the Higgs boson decaying into pairs of tau leptons](https://brandstetter-johannes.github.io/publication/cms-higgs/) non of the processes, i.e., the Higgs boson signal itself nor the many ''background'' processes, was measured directly. Everything needed to be reconstructed from terabytes of detector data, and -- even more fascinating to me -- by using sophisticated physical simulations. 

My first contact with simulations in the context of Deep Learning was through the work on
[Boundary graph neural networks for 3D simulations](https://brandstetter-johannes.github.io/publication/mayr-2021-bgnn), which was financed by the [Austrian Research Promotion Agency (FFG)](https://www.ffg.at/en) after winning a research grant together with [DCS computing](https://www.aspherix-dem.com/).

During my years in Amsterdam I fully pivoted towards neural modeling of [partial differential equations (PDEs)](https://brandstetter-johannes.github.io/tag/neural-solvers/). For example: 
- In [Message Passing Neural PDE Solvers](https://brandstetter-johannes.github.io/publication/brandstetter-2022-mpnn/), we replaced all heuristically designed components in numerical PDE solvers with backprop-optimized neural function approximators. 
- We studied how to use [Lie Point Symmetries of PDEs](https://brandstetter-johannes.github.io/publication/brandstetter-2022-lpsda/) to improve sample complexity of neural PDE solvers.
- In [Clifford Neural Layers for PDE Modeling](https://brandstetter-johannes.github.io/publication/brandstetter-2022-clifford/) and [Geometric Clifford Algebra Networks](https://brandstetter-johannes.github.io/publication/ruhe-2023-cgans/), we introduced neural network layers for PDE modeling, which are based on operations on composite objects of scalars, vectors, and higher order objects.
- In [Towards Multi-spatiotemporal-scale Generalized PDE Modeling](https://brandstetter-johannes.github.io/publication/gupta-2022-pdearena/), we introduce [PDEArena](https://microsoft.github.io/pdearena/), a modern PyTorch Lightning-based deep learning framework for neural PDE modeling with a plethora of state-of-the art neural PDE surrogates and various temporal PDEs in 1-, 2-, and 3-spatial dimensions. 
- In [ClimaX](https://brandstetter-johannes.github.io/publication/nguyen-2023-climax/), we developed a flexible and generalizable deep learning model for weather and climate science that can be trained using heterogeneous datasets. ClimaX is the first foundation model for weather and climate.

# How to disrupt simulations at industry-scale

Recent years have shown that scalable ideas, improving the datasets, and clever engineering are the ingredients for ever better Deep Learning systems. LLMs and large-scale computer vision models have given birth to the heavily overused term "foundation model".
After language and computer vision, foundation models have spread over to various disciplines, with [AlphaFold](https://www.nature.com/articles/s41586-021-03819-2) as very prominent example. 

I want to go one step further, and bring foundation models to the every-day engineering world, and in doing so, disrupt how our industry works. Every day thousands and thousands of compute hours are spent on turbulence modeling, simulations of fluid or air flows, heat transfer in materials, traffic flows, and many more. Many of these processes follow similar underlying patterns, but yet need different and extremely specialized softward to simulate. Even worse, for different parameter settings the costly simulations need to be run at full length from scratch. 

This is what I want to change! Deep Learning techniques are ready to develope models which run simulations in seconds instead of days or even weeks. The hardware is ready to digest high-resolutional industry-scale inputs, e.g., 3D meshes or images, and subsequently sets the stage to train Deep Learning models at scale. 

But what about the data you might ask? Don't we need high-quality ground truth data, which usually must come from the very simulations we are going to replace, presenting us with a proverbial chicken-and-egg problem? Luckily, many of the above mentioned processes have common underlying dynamics -- similar to how different languages share structure and grammar. Simulation data is abundant, we just need to use the right ones, and many of that. 

Personally, I have experienced modern computer vision as one of the driving tools for developing data-driven simulations. But it will take much more. It will need expertise in numerical simulations, geometric and physics-informed deep learning, and engineering at scale. We have already put together a very strong interdisciplinary team with different expertise, and keep hiring. The journey is going to be exciting.

## Stay stuned, first works will appear soon
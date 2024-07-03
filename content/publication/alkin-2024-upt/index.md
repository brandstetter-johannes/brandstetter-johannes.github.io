---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Universal Physics Transformers -- A Framework For Efficiently Scaling Neural Operators
subtitle: ''
summary: 'We introduce Universal Physics Transformers (UPTs), an efficient and unified learning paradigm for a wide range of spatio-temporal problems. UPTs operate without grid- or particle-based latent structures, enabling flexibility and scalability across meshes and particles.'
authors:
- Benedikt Alkin 
- Andreas Fürst
- Simon Schmid
- Lukas Gruber
- Markus Holzleitner
- Johannes Brandstetter
tags: ['Partial Differential Equations', 'AI4Science', 'Neural PDE Solvers', 'Learning2Simulate', 'Deep Learning']
categories: ['Learning2Simulate']
date: 2024-02-19T12:55:17+02:00
lastmod: 2024-02-19T12:55:17+02:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: 'Universal Physics Transformers'
  focal_point: 'TopRight'
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2022-02-07T12:55:17+02:00'
publication_types:
- '1'
abstract: 'Neural operators, serving as physics surrogate models, have recently gained increased interest. With ever increasing problem complexity, the natural question arises: what is an efficient way to scale neural operators to larger and more complex simulations - most importantly by taking into account different types of simulation datasets. This is of special interest since, akin to their numerical counterparts, different techniques are used across applications, even if the underlying dynamics of the systems are similar. Whereas the flexibility of transformers has enabled unified architectures across domains, neural operators mostly follow a problem specific design, where GNNs are commonly used for Lagrangian simulations and grid-based models predominate Eulerian simulations. We introduce Universal Physics Transformers (UPTs), an efficient and unified learning paradigm for a wide range of spatio-temporal problems. UPTs operate without grid- or particle-based latent structures, enabling flexibility and scalability across meshes and particles. UPTs efficiently propagate dynamics in the latent space, emphasized by inverse encoding and decoding techniques. Finally, UPTs allow for queries of the latent space representation at any point in space-time. We demonstrate diverse applicability and efficacy of UPTs in mesh-based fluid simulations, and steady-state Reynolds averaged Navier-Stokes simulations, and Lagrangian-based dynamics.'
publication: 'Preprint'
url_pdf: https://arxiv.org/abs/2402.12365
url_code: https://github.com/ml-jku/UPT
url_project: https://ml-jku.github.io/UPT/
---
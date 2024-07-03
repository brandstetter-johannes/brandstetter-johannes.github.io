---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Message Passing Neural PDE Solvers
subtitle: ''
summary: 'In this work, we introduce a message passing neural PDE solver that replaces all heuristically designed components in numerical PDE solvers with backprop-optimized neural function approximators. Published at ICLR 2022 (Spotlight).'
authors:
- Johannes Brandstetter 
- Daniel E. Worrall
- Max Welling
tags: ['Partial Differential Equations', 'Learning2Simulate', 'Neural Solvers', 'AI4Science', 'Graph Neural Networks', 'Deep Learning']
categories: ['Neural Solvers']
date: 2022-02-07T12:55:17+02:00
lastmod: 2022-02-07T12:55:17+02:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: 'Message Passing Neural PDE Solver'
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
abstract: 'The numerical solution of partial differential equations (PDEs) is difficult, having led to a century of research so far. Recently, there have been pushes to build neural--numerical hybrid solvers, which piggy-backs the modern trend towards fully end-to-end learned systems. Most works so far can only generalize over a subset of properties to which a generic solver would be faced, including: resolution, topology, geometry, boundary conditions, domain discretization regularity, dimensionality, etc. In this work, we build a solver, satisfying these properties, where all the components are based on neural message passing, replacing all heuristically designed components in the computation graph with backprop-optimized neural function approximators. We show that neural message passing solvers representationally contain some classical methods, such as finite differences, finite volumes, and WENO schemes. In order to encourage stability in training autoregressive models, we put forward a method that is based on the principle of zero-stability, posing stability as a domain adaptation problem. We validate our method on various fluid-like flow problems, demonstrating fast, stable, and accurate performance across different domain topologies, equation parameters, discretizations, etc., in 1D and 2D.'
publication: '*10th International Conference on Learning Representations (ICLR), 2022* (**Spotlight**)'
url_pdf: https://arxiv.org/abs/2202.03376
url_code: https://github.com/brandstetter-johannes/MP-Neural-PDE-Solvers
url_poster: https://brandstetter-johannes.github.io/media/MP-PDE-Solvers_poster.pdf
url_slides: https://brandstetter-johannes.github.io/media/MP-PDE-Solvers_slides.pdf
---
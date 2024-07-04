---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Lie Point Symmetry Data Augmentation for Neural PDE Solvers
subtitle: ''
summary: 'We present how to use Lie Point Symmetries of PDEs to improve sample complexity of neural PDE solvers. Published at ICML 2022 (Spotlight).'
authors:
- Johannes Brandstetter 
- Max Welling
- Daniel E. Worrall
tags: ['Partial Differential Equations', 'Learn2Simulate', 'Neural Surrogates', 'Neural Operators', 'AI4Science', 'Geometric Deep Learning', 'Lie Point Symmetries', 'Deep Learning']
categories: ['Lie Point Symmetries']
date: 2022-02-15T12:55:17+02:00
lastmod: 2022-02-15T12:55:17+02:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: 'TopRight'
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2022-02-15T12:55:17+02:00'
publication_types:
- '1'
abstract: 'Neural networks are increasingly being used to solve partial differential equations (PDEs), replacing slower numerical solvers. However, a critical issue is that neural PDE solvers require high-quality ground truth data, which usually must come from the very solvers they are designed to replace. Thus, we are presented with a proverbial chicken-and-egg problem. In this paper, we present a method, which can partially alleviate this problem, by improving neural PDE solver sample complexity -- Lie point symmetry data augmentation (LPSDA). In the context of PDEs, it turns out that we are able to quantitatively derive an exhaustive list of data transformations, based on the Lie point symmetry group of the PDEs in question, something not possible in other application areas. We present this framework and demonstrate how it can easily be deployed to improve neural PDE solver sample complexity by an order of magnitude.'
publication: '*39th International Conference on Machine Learning (ICML), 2022* (**Spotlight**)'
url_pdf: https://arxiv.org/abs/2202.07643
url_code: https://github.com/brandstetter-johannes/LPSDA
url_poster: https://brandstetter-johannes.github.io/media/LPSDA-poster.png
url_slides: https://brandstetter-johannes.github.io/media/LPSDA-slides.pdf
---

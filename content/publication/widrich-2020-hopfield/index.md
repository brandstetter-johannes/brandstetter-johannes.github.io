---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Modern hopfield networks and attention for immune repertoire classification
subtitle: ''
summary: 'We exploit the storage capacity of modern Hopfield networks to solve a challenging multiple instance learning (MIL) problem in computational biology: immune repertoire classification. Published at NeurIPS 2020 (Spotlight).'
authors:
- Michael Widrich
- Bernhard Schäfl
- Milena Pavlović
- Hubert Ramsauer
- Lukas Gruber
- Markus Holzleitner
- Johannes Brandstetter
- Geir Kjetil Sandve
- Victor Greiff
- Sepp Hochreiter
- Günter Klambauer
tags: ['Modern Hopfield Networks', 'Self-Attention', 'Transformer', 'Associative Memory', 'Immune Repertoire Classification', 'Deep Learning']
categories: ['Modern Hopfield Networks']
date: 2020-07-13T12:55:17+02:00
lastmod: 2020-07-13T12:55:17+02:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: 'Immune repertoire classification as multiple instance learning problem'
  focal_point: 'TopRight'
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2020-07-13T12:55:17+02:00'
publication_types:
- '1'
abstract: 'A central mechanism in machine learning is to identify, store, and recognize patterns. How to learn, access, and retrieve such patterns is crucial in Hopfield networks and the more recent transformer architectures. We show that the attention mechanism of transformer architectures is actually the update rule of modern Hopfield networks that can store exponentially many patterns. We exploit this high storage capacity of modern Hopfield networks to solve a challenging multiple instance learning (MIL) problem in computational biology: immune repertoire classification. In immune repertoire classification, a vast number of immune receptors are used to predict the immune status of an individual. This constitutes a MIL problem with an unprecedentedly massive number of instances, two orders of magnitude larger than currently considered problems, and with an extremely low witness rate. Accurate and interpretable machine learning methods solving this problem could pave the way towards new vaccines and therapies, which is currently a very relevant research topic intensified by the COVID-19 crisis. In this work, we present our novel method DeepRC that integrates transformer-like attention, or equivalently modern Hopfield networks, into deep learning architectures for massive MIL such as immune repertoire classification. We demonstrate that DeepRC outperforms all other methods with respect to predictive performance on large-scale experiments including simulated and real-world virus infection data and enables the extraction of sequence motifs that are connected to a given disease class.'
publication: '*Thirty-third Conference on Neural Information Processing Systems (NeurIPS), 2020* (**Spotlight**)'
url_pdf: https://arxiv.org/abs/2007.13505
url_code: https://github.com/ml-jku/DeepRC
url_poster: https://brandstetter-johannes.github.io/media/Deep-RC_poster.pdf
links:
- name: Blog post
  url: https://github.com/ml-jku/hopfield-layers
---

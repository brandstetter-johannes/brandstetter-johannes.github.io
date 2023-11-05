---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Hopfield Networks is All You Need
subtitle: ''
summary: 'We introduce a modern Hopfield network with continuous states and a corresponding update rule. The new update rule is equivalent to the attention mechanism used in transformers. Published at ICLR 2021.'
authors:
- Hubert Ramsauer
- Bernhard Schäfl
- Johannes Lehner
- Philipp Seidl
- Michael Widrich
- Thomas Adler
- Lukas Gruber
- Markus Holzleitner
- Milena Pavlović
- Geir Kjetil Sandve
- Victor Greiff
- David Kreil
- Michael Kopp
- Günter Klambauer
- Johannes Brandstetter
- Sepp Hochreiter
tags: ['Modern Hopfield Networks', 'Self-Attention', 'Transformer', 'Associative Memory', 'Deep Learning']
categories: ['Modern Hopfield Networks']
date: 2020-07-16T12:55:17+02:00
lastmod: 2020-07-16T12:55:17+02:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: 'Pattern retrieval in Modern Hopfield Networks'
  focal_point: 'TopRight'
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2020-07-16T12:55:17+02:00'
publication_types:
- '1'
abstract: 'We introduce a modern Hopfield network with continuous states and a corresponding update rule. The new Hopfield network can store exponentially (with the dimension of the associative space) many patterns, retrieves the pattern with one update, and has exponentially small retrieval errors. It has three types of energy minima (fixed points of the update): (1) global fixed point averaging over all patterns, (2) metastable states averaging over a subset of patterns, and (3) fixed points which store a single pattern. The new update rule is equivalent to the attention mechanism used in transformers. This equivalence enables a characterization of the heads of transformer models. These heads perform in the first layers preferably global averaging and in higher layers partial averaging via metastable states. The new modern Hopfield network can be integrated into deep learning architectures as layers to allow the storage of and access to raw input data, intermediate results, or learned prototypes. These Hopfield layers enable new ways of deep learning, beyond fully-connected, convolutional, or recurrent networks, and provide pooling, memory, association, and attention mechanisms. We demonstrate the broad applicability of the Hopfield layers across various domains. Hopfield layers improved state-of-the-art on three out of four considered multiple instance learning problems as well as on immune repertoire classification with several hundreds of thousands of instances. On the UCI benchmark collections of small classification tasks, where deep learning methods typically struggle, Hopfield layers yielded a new state-of-the-art when compared to different machine learning methods. Finally, Hopfield layers achieved state-of-the-art on two drug design datasets. '
publication: '*9th International Conference on Learning Representations (ICLR), 2021*'
url_pdf: https://arxiv.org/abs/2008.02217
url_code: https://github.com/ml-jku/hopfield-layers
links:
- name: Blog post
  url: https://ml-jku.github.io/hopfield-layers/
---

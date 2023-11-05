---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Looking at the Performer from a Hopfield point of view
subtitle: ''
summary: 'Blog post which analyzes the the Performer paper from a Hopfield point of view. Published as blog post at ICLR 2022.'
authors:
- Johannes Brandstetter 
- Hubert Ramsauer
- Markus Holzleitner
- Sepp Hochreiter
- Bernhard Schäfl
tags: ['Modern Hopfield Networks', 'Self-Attention', 'Transformer', 'Associative Memory', 'Linear Attention', 'Deep Learning']
categories: ['Modern Hopfield Networks']
date: 2020-12-12T12:55:17+02:00
lastmod: 2020-12-12T12:55:17+02:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: 'Linearized Performer attention'
  focal_point: 'TopRight'
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2020-12-12T12:55:17+02:00'
publication_types:
- '1'
abstract: 'The recent paper Rethinking Attention with Performers constructs a new efficient attention mechanism in an elegant way. It strongly reduces the computational cost for long sequences, while keeping the intriguing properties of the original attention mechanism. In doing so, Performers have a complexity only linear in the input length, in contrast to the quadratic complexity of standard transformers. This is a major breakthrough in the strive of improving transformer models.
In this blog post, we look at the Performer from a Hopfield Network point of view and relate aspects of the Performer architecture to findings in the field of associative memories and Hopfield Networks.'
publication: '*10th International Conference on Learning Representations (ICLR), 2022* (**Blogpost**)'
links:
- name: Blog post
  url: https://ml-jku.github.io/blog-post-performer/
---

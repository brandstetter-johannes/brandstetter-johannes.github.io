---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Clifford Group Equivariant Neural Networks
subtitle: ''
summary: 'We introduce a novel method to construct E(n)- and O(n)-equivariant neural networks using Clifford algebras. Published at NeurIPS 2023 (Oral).'
authors:
- David Ruhe
- Johannes Brandstetter
- Patrick Forré
tags: ['Clifford Algebras', 'Geometric Algebras', 'Geometric Deep Learning', 'AI4Science', 'Graph Neural Networks', 'Equivariance', 'Deep Learning']
categories: ['Geometric Deep Learning']
date: 2023-05-18T12:55:17+02:00
lastmod: 2023-05-18T12:55:17+02:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: 'CGENN layers'
  focal_point: 'TopRight'
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2023-05-18T12:55:17+02:00'
publication_types:
- '1'
abstract: 'We introduce Clifford Group Equivariant Neural Networks: a novel approach for constructing O(n)- and E(n)-equivariant models. We identify and study the Clifford group, a subgroup inside the Clifford algebra tailored to achieve several favorable properties. Primarily, the action of the group forms an orthogonal automorphism that extends beyond the typical vector space to the entire Clifford algebra while respecting the multivector grading. This leads to several non-equivalent subrepresentations corresponding to the multivector decomposition. Furthermore, we prove that the action respects not just the vector space structure of the Clifford algebra but also its multiplicative structure, i.e., the geometric product. These findings imply that every polynomial in multivectors, An advantage worth mentioning is that we obtain expressive layers that can elegantly generalize to inner-product spaces of any dimension. We demonstrate, notably from a single core implementation, state-of-the-art performance on several distinct tasks, including a three-dimensional n-body experiment, a four-dimensional Lorentz-equivariant high-energy physics experiment, and a five-dimensional convex hull experiment.'
publication: '*Thirty-seventh Conference on Neural Information Processing Systems (NeurIPS), 2023* (**Oral**)'
url_pdf: https://arxiv.org/abs/2305.11141
url_code: https://github.com/DavidRuhe/clifford-group-equivariant-neural-networks
links:
- name: Blog post
  url: https://davidruhe.github.io/2023/06/14/clifford-group.html
---

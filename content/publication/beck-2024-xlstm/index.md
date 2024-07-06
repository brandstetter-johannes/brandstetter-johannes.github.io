---
# Documentation: https://wowchemy.com/docs/managing-content/

title: xLSTM -- Extended Long Short-Term Memory
subtitle: ''
summary: 'How far do we get in language modeling when scaling LSTMs to billions of parameters, leveraging the latest techniques from modern LLMs, but mitigating known limitations of LSTMs?'
authors:
- Maximilian Beck
- Korbinian Poeppel
- Markus Spanring
- Andreas Auer
- Oleksandra Prudnikova
- Michael Kopp
- Günter Klambauer
- Johannes Brandstetter
- Sepp Hochreiter
tags: ['Large Language Models', 'xLSTM', 'Deep Learning']
categories: ['Large Language Models']
date: 2024-05-07T12:55:17+02:00
lastmod: 2024-05-07T12:55:17+02:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: 'xLSTM family'
  focal_point: 'TopRight'
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2024-05-07T12:55:17+02:00'
publication_types:
- '1'
abstract: 'In the 1990s, the constant error carousel and gating were introduced as the central ideas of the Long Short-Term Memory (LSTM). Since then, LSTMs have stood the test of time and contributed to numerous deep learning success stories, in particular they constituted the first Large Language Models (LLMs). However, the advent of the Transformer technology with parallelizable self-attention at its core marked the dawn of a new era, outpacing LSTMs at scale. We now raise a simple question: How far do we get in language modeling when scaling LSTMs to billions of parameters, leveraging the latest techniques from modern LLMs, but mitigating known limitations of LSTMs? Firstly, we introduce exponential gating with appropriate normalization and stabilization techniques. Secondly, we modify the LSTM memory structure, obtaining: (i) sLSTM with a scalar memory, a scalar update, and new memory mixing, (ii) mLSTM that is fully parallelizable with a matrix memory and a covariance update rule. Integrating these LSTM extensions into residual block backbones yields xLSTM blocks that are then residually stacked into xLSTM architectures. Exponential gating and modified memory structures boost xLSTM capabilities to perform favorably when compared to state-of-the-art Transformers and State Space Models, both in performance and scaling.'
publication: 'Preprint'
url_pdf: https://arxiv.org/abs/2405.04517
url_code: https://github.com/NX-AI/xlstm
---
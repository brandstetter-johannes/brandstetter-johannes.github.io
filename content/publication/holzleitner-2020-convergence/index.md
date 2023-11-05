---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Convergence proof for actor-critic methods applied to ppo and rudder
subtitle: ''
summary: 'We prove under commonly used assumptions the convergence of actor-critic reinforcement learning algorithms. Published at Transactions on Large-Scale Data-and Knowledge-Centered Systems XLVIII.'
authors:
- Markus Holzleitner 
- Lukas Gruber
- José A. Arjona-Medina
- Johannes Brandstetter
- Sepp Hochreiter
tags: ['Reinforcement Learning', 'Delayed Rewards', 'Convergence Proof', 'Deep Learning']
categories: ['Reinforcement Learning']
date: 2020-12-02T12:55:17+02:00
lastmod: 2020-12-02T12:55:17+02:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: 'Convergence proof for actor-critic RL algorithms'
  focal_point: 'TopRight'
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2020-12-02T12:55:17+02:00'
publication_types:
- '2'
abstract: 'We prove under commonly used assumptions the convergence of actor-critic reinforcement learning algorithms, which simultaneously learn a policy function, the actor, and a value function, the critic. Both functions can be deep neural networks of arbitrary complexity. Our framework allows showing convergence of the well known Proximal Policy Optimization (PPO) and of the recently introduced RUDDER. For the convergence proof we employ recently introduced techniques from the two time-scale stochastic approximation theory.
Previous convergence proofs assume linear function approximation, cannot treat episodic examples, or do not consider that policies become greedy. The latter is relevant since optimal policies are typically deterministic. Our results are valid for actor-critic methods that use episodic samples and that have a policy that becomes more greedy during learning.'
publication: '*Transactions on Large-Scale Data-and Knowledge-Centered Systems XLVIII, 2021*'
url_pdf: https://arxiv.org/abs/2012.01399
---

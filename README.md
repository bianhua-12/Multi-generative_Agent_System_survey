# A Survey on Multi-Generative Agent System: Recent Advances and New Frontiers

This repository contains the figure and data related to the paper "**A Survey on Multi-Generative Agent System: Recent Advances and New Frontiers**." The paper provides a survey on the recent advancements and future directions in multi-agent systems based on large language models (LLMs). It covers both the theoretical and practical aspects, including relevant Multi-Generative Agent System (MGAS) architecture, applications, challenges, and potential directions. For more details, refer to the
[paper](https://arxiv.org/abs/2412.17481).

![Paper Thumbnail](figures/mgas.png)  

## Table of Contents
- [A Survey on Multi-Generative Agent System: Recent Advances and New Frontiers](#a-survey-on-multi-generative-agent-system-recent-advances-and-new-frontiers)
  - [Table of Contents](#table-of-contents)
  - [MGASs for Solving Complex Tasks](#mgass-for-solving-complex-tasks)
    - [Reasoning Framework](#reasoning-framework)
    - [Communication Optimization](#communication-optimization)
  - [MGASs for Simulating Specific Scenarios](#mgass-for-simulating-specific-scenarios)
  - [MGASs for Evaluating Generative Agents](#mgass-for-evaluating-generative-agents)
  - [Resources](#resources)

## MGASs for Solving Complex Tasks

In most scenarios in reality, completing a task requires multiple roles, multiple steps, and so on. This is difficult for a single agent, but multiple agents working together will be well suited to this task. Further, each of these agents can be trained  independently. Compared with a single agent, MGAS can achieve better results. That is, the multi-agent collaboration will improve the overall performance. For recent works, we summarize two aspects, reasoning framework and communication optimization.

### Reasoning Framework

We summarize three aspects by the pipeline of reasoning, including:

- multi-stage framework
- collective decision making
- self-refine framework

Just as its name implies, multi-stage framework refers to a pipeline that agents act as serial problem solvers at different stages, while collective decision making refers that different agents vote or debate for one goal. Self-refine framework refers that one agent iterates itself in the loop.

### Communication Optimization

We summarize two aspects in Communication Optimization, including:

- speed optimization
- distribute discuss

Speed optimization refers that researchers try to speed up the communication of agents, while distribute discuss refers that agents try to solve tasks without enough information. Agents need to communicate with each other to achieve their goal.

## MGASs for Simulating Specific Scenarios

This section will illustrate the application for MGAS in simulation. Researchers apply agents to simulate a certain scenario to study its impact on a specific subject like social science. On the one hand, compared with rule-based methods, generative agents with natural  communication can be more intuitive for humans. On the other hand, environment determines the properties of the simulation, which is the core of the entire simulation. We summarize main domain where researchers apply simulation, including:

- Game
- Social Media
- Tiny Society
- Politics
- Economics
- Wireless Framework

## MGASs for Evaluating Generative Agents

With LLM prevailing in the community, how to evaluate the ability of LLM is an open question. Existing evaluation methods suffer from the following shortcomings:

- constrained evaluation abilities
- vulnerable benchmarks
- unobjective metrics.

The complexity and diversity of MGAS have indicated that MGAS can evaluate LLM. Researchers mainly evaluate strategic and emotional ability of generative agent.

Similarly, MGAS can also be used in training generative agents. We summarize three aspects of training:

- Supervised Fine-Tuning (SFT)
- Reinforcement Learning (RL)
- Synthesizing data for training.

## Resources

This repository includes all the necessary code to reproduce the experiments in the paper. The code is organized as follows:

- `/data`: Datasets used in the experiments.
- `/figures`: Figures and diagrams used in the paper.

For foreigner in this field, please see table 1, table 2 and table 3 for open-source code and benchmark or datasets in [paper](https://arxiv.org/abs/2412.17481).

Our collected papers are published in [this link](https://south-colony-f37.notion.site/167fe4b85d7480148386f2d100f5617f?v=167fe4b85d74811e9db9000ceb088ea4&pvs=4)
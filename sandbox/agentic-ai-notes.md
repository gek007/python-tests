# Agentic AI Notes

## Definition
Agentic AI describes artificial intelligence systems that autonomously pursue goals by acting independently with minimal or no human intervention. Unlike traditional AI that primarily generates outputs (e.g., text), an agentic AI runs a control loop involving decision-making, real-world tool usage, observation, and adaptation until the task is completed or human intervention occurs.

Agentic AI is a spectrum ranging from simple assistants with limited autonomy to fully strategic agents managing complex workflows.

## Core Workflow Loop (Decide, Act, Observe)
Agentic AI generally follows a repeating loop:
1. **Decide:** Examine the goal and current context/state; select the next action (e.g., call an API, write code, ask user, stop).
2. **Act:** Execute the chosen action through a tool or direct intervention (e.g., HTTP request, file edit, robot command).
3. **Observe:** Read results, update memory/context, detect errors, decide next steps — continue, retry, or finish.

This cycle is sometimes called the ReAct loop (Reasoning + Acting).

## Key Workflow Steps & Components
- **Perception:** Collect relevant real-time data via sensors, APIs, user input, or memory retrieval.
- **Reasoning:** Interpret the data within domain knowledge frameworks; analyze context, recognize patterns, and deduce implications.
- **Goal Setting:** Define clear objectives and formulate strategies, possibly decomposing goals into sub-tasks or multi-step plans.
- **Decision Making:** Evaluate alternatives using probabilistic or utility-based models; select actions optimizing efficiency, accuracy, safety.
- **Execution:** Carry out actions by invoking tools, APIs, software systems, or physical devices.
- **Learning & Adaptation:** Use feedback to improve over time via reinforcement learning or self-supervised methods.
- **Orchestration:** Coordinate multiple agents or systems to collaborate on complex tasks or workflows harmoniously.

## Characteristics That Make AI Agentic
- Goal-directed behavior: Independent progress towards defined outcomes.
- Multi-step planning and decomposition of tasks.
- Real action execution beyond output generation.
- Adaptivity and dynamic error recovery.
- Persistent state/memory across sessions.
- Autonomous stopping criteria and escalation.
- Collaboration with humans and other agents.
- Specialization into domain experts, leveraging coordinated agentic architectures.

## Applications
- Coding agents managing pull requests and code edits.
- Research assistants synthesizing information and planning experiments.
- Sales pipeline management without supervision.
- Autonomous vehicles, medical diagnosis aid, customer support automation.
- Incident response automation, supply chain optimization.

## Challenges
- Monitoring to avoid unsafe or unintended actions.
- Mitigating risks from flawed reward functions or shortcuts.
- Need for transparency, interpretability, and governance frameworks.

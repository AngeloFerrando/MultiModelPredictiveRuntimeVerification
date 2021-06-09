# MultiModelPredictiveRuntimeVerification

This repository contains a very small Python tool to generate and execute predictive monitors when using multiple models (i.e., when applied to compound systems).

## How to install

- Download and Install Python3 (https://www.python.org/downloads/)
- Download and Install Spot (https://spot.lrde.epita.fr/install.html) and make sure it works on your machine

## How to use

Things to know before rushing into the tool:
- The models have to be passed as HOA formatted file (http://adl.github.io/hoaf/)
- The trace has to be a text file where in each line is reported a single event

To run a standard non-predictive monitor which analyses a given LTL property over a given trace of events
```bash
-$ python3 monitor.py <LTL_property> <trace_file>
```

To run a centralised multi-model predictive monitor which analyses a given LTL property over a given trace of events considering a single model (or a set of models) to predict future events
```bash
-$ python3 monitor.py <LTL_property> <trace_file> --models <model> --centralised
```
If multiple models are passed, they are combined together and then used to predict future events.

To run a composition multi-model predictive monitor which analyses a given LTL property over a given trace of events considering a set of models to predict future events
```bash
-$ python3 monitor.py <LTL_property> <trace_file> --models <model_0> ... <model_N> --composition
```
Composition means that the property is decomposed (if possible) and for each sub-property so generated, a predictive monitor is generated. This can help when sub-properties consider a subset of the system and only a subset of the models is necessary to predict future events.

## Try an example

Inside the models folder, there are two models that can be used to test the tool (agent and wheels models). An example trace file can also be found in the main folder.

To run a standard non-predictive monitor on the example
```bash
-$ python3 monitor.py '(G(forward_wh->(!stop_wh U set_wheels_speed_0_wh))) & (G(move_to_A_ag->(!action_fail_ag U move_to_B_ag)))' trace.txt
```

To run a centralised multi-model predictive monitor on the example
```bash
-$ python3 monitor.py '(G(forward_wh->(!stop_wh U set_wheels_speed_0_wh))) & (G(move_to_A_ag->(!action_fail_ag U move_to_B_ag)))' trace.txt --models ./models/wheels.hoa ./models/agent.hoa --centralised
```

To run a composition multi-model predictive monitor on the example
```bash
-$ python3 monitor.py '(G(forward_wh->(!stop_wh U set_wheels_speed_0_wh))) & (G(move_to_A_ag->(!action_fail_ag U move_to_B_ag)))' trace.txt --models ./models/wheels.hoa ./models/agent.hoa --multi
```

## Experiments

To test the tool over a given property, and set of models, the experiments.py script can be used.
```bash
-$ python3 experiments.py <min_trace_length> <max_trace_length> <step>
```
This script runs multiple times the different monitors over traces with different lengths (from min to max, considering a fixed increment step).

For instance
```bash
-$ python3 experiments.py 10 100 10
```
It runs the monitors on traces of length: 10, 20, 30, ..., 100.
The results are reported in a CSV file automatically generated (the monitor synthesis time, the execution time, and so on).

P.S. The experiments.py script uses the generate_trace function (defined in it). For now, this function generates a trace suitable for testing the property and models left for example. Nonetheless, if you need to test a custom property and models, it is enough to update the generate_trace function to generate the trace of events you want to verify.

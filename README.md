### ThreatWeaver

ThreatWeaver is an extensible logical attack-graph generation and analysis tool that supports customizable and pluggable interaction rules.
One of its main design goals is to overcome the limitations of static tools like MulVAL, which struggle to incrementally generate attack graphs in dynamic environments.

#### Installation

Make sure you have Python 3.10+ installed, then install the latest release of threat-weaver (version 1.0.0) via pip:

> pip install threat-weaver==1.0.0


After installation, simply run the main script:

> python main.py

#### File Description

`3H1G.P`: This file follows the MulVAL standard input format. It serves as a benchmark for comparing attack-graph generation results between ThreatWeaver and MulVAL.

`interaction.yaml`: This YAML file defines a set of customizable attack interaction rules. It corresponds to MulVAL’s interaction model and can be extended to support additional attack semantics.


### Differences
Compared to v0.7.4, the latest version includes the following updates:

- Renamed class names, function names, and variable names for improved clarity and consistency.

- Enhanced comments and documentation to increase readability.

- Refined the package structure for better organization and maintainability.



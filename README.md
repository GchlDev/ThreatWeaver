### ThreatWeaver
ThreatWeaver is a dynamic attack graph generation and analysis tool that supports customizable and extensible interaction rules. It is designed for comparative analysis with tools like MulVAL.

Installation
Make sure you have Python 3.8+ installed, then install the latest version of ThreatWeaver via pip:

> pip install threat-weaver

After installation, simply run the main script:

> python main.py

### Input Files
`3H1G.P`: This is the input file in the standard format used by the MulVAL tool. It serves as a baseline for comparison between ThreatWeaver and MulVAL in terms of attack graph generation.

`interaction.yaml`: This YAML file defines a set of customizable attack interaction rules. It corresponds to the interaction model used in MulVAL and can be extended to support additional attack semantics.

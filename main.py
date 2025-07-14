from threat_weaver import analyze
from threat_weaver import reader
from threat_weaver import graph


unique = set()
viewer = graph.MulVALGraph(name='Small-Scale Enterprise Network')
analyzer = analyze.LogicAnalyzer()

data_loader = reader.MulVALLoader('3H1G.P')
for predicate, attributes in data_loader.next_fact():
    results = analyzer.update(predicate, attributes)
    for result in results:
        description = ','.join(result[0]) + '-' + result[1] + '->' + ','.join(result[2])
        if description not in unique:
            viewer.insert(result)
            unique.add(description)


viewer.to_gml('ThreatWeaver')
viewer.to_pdf('ThreatWeaver')



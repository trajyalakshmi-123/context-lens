def build_graph(dependencies):
    graph = {}

    for d in dependencies:
        src = d["source"]
        tgt = d["target"]

        if src not in graph:
            graph[src] = []

        graph[src].append(tgt)

    return graph


def find_downstream(dataset, graph):
    return graph.get(dataset, [])


def find_upstream(pipeline, dependencies):
    upstream = []

    for d in dependencies:
        if d["target"] == pipeline:
            upstream.append(d["source"])

    return upstream





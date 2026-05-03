def format_context(context, incident):

    lines = []

    lines.append(f"Incident: {incident['description']}\n")

    if context["pipeline"]:
        lines.append(f"Observed: Pipeline '{context['pipeline']}' failure")

    if context["dataset"]:
        lines.append(f"Dependency: Pipeline depends on dataset '{context['dataset']}'")

    if context["change"]:
        lines.append(f"Change: Dataset modified via change '{context['change']}'")

    if context["ticket"]:
        lines.append(f"Ticket: Change tracked under '{context['ticket']}'")

    if context["gaps"]:
        lines.append("\nGap Identified:")
        for g in context["gaps"]:
            lines.append(f"- {g}")

    lines.append("\nConclusion:")
    lines.append(context["conclusion"])

    return "\n".join(lines)
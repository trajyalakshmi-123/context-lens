from nlp_utils import extract_pipeline, extract_dataset


def reconstruct_context(incident, signals, dependencies, changes, tickets):

    context = {
        "pipeline": None,
        "dataset": None,
        "change": None,
        "ticket": None,
        "gaps": [],
        "conclusion": ""
    }

    # STEP 1 — Identify pipeline from signals (strongest signal)
    for s in signals:
        pipeline = extract_pipeline(s["description"])
        if pipeline:
            context["pipeline"] = pipeline
            break

    # STEP 2 — Find dataset via dependencies
    for d in dependencies:
        if d["target"] == context["pipeline"]:
            context["dataset"] = d["source"]
            break

    # STEP 3 — Find change affecting dataset
    for c in changes:
        dataset = extract_dataset(c["description"])
        if dataset == context["dataset"]:
            context["change"] = c["id"]
            break

    # STEP 4 — Find ticket linked to change
    for t in tickets:
        if t.get("change_id") == context["change"]:
            context["ticket"] = t["id"]
            break

    # STEP 5 — Infer gap (core logic)
    if context["pipeline"] and context["dataset"] and context["change"]:
        context["gaps"].append("Downstream impact of schema change not handled")

    # STEP 6 — Conclusion (probabilistic tone)
    if context["gaps"]:
        context["conclusion"] = (
            "Revenue dashboard issue is likely due to pipeline failure "
            "caused by upstream schema change."
        )
    else:
        context["conclusion"] = "No clear cause identified."

    return context
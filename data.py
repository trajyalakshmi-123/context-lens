# Business incident
incident = {
    "id": "INC001",
    "description": "Revenue dashboard numbers are incorrect since yesterday"
}

# Signals (system observations)
signals = [
    {
        "type": "pipeline_failure",
        "description": "revenue_job failed due to column mismatch error"
    }
]

# Dependencies (CMDB-style)
dependencies = [
    {"source": "orders", "target": "revenue_job"}
]

# Changes (release/change logs)
changes = [
    {
        "id": "C1",
        "description": "Updated schema of orders table to include new column"
    }
]

# Tickets (intent layer)
tickets = [
    {
        "id": "T1",
        "description": "Schema update for orders table",
        "change_id": "C1"
    }
]
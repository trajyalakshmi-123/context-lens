def extract_pipeline(text):
    text = text.lower()

    if "revenue" in text:
        return "revenue_job"

    return None


def extract_dataset(text):
    text = text.lower()

    if "orders" in text:
        return "orders"

    return None
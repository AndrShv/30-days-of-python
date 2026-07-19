def filter_and_boost_metrics(metrics: list, min_threshold: float, history=None) -> list:
    if history is None:
        history = []
    filtered_metrics = filter(lambda f: f > min_threshold, metrics)
    boosted_metrics = map(lambda b: b + 0.5 , filtered_metrics)
    history.extend(boosted_metrics)
    return history



import json

# process the cursor results into the expected format and return as json
def process_results(results):
    gaps = {}
    for elr_code, gap_start, gap_end in results:
        if elr_code not in gaps:
            gaps[elr_code] = []

        gaps[elr_code].append({
            "mileage_from": f"{gap_start:.3f}",
            "mileage_to": f"{gap_end:.3f}"
        })

    return json.dumps(gaps, indent=4)
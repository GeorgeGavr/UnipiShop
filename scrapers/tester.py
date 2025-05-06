from scrapers.test_webscrap import scrape_test
import json

results = scrape_test("travel")
print(json.dumps(results, indent=2))
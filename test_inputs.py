import unittest

from source_fixture import load


class ExchangeInputs(unittest.TestCase):
    def test_related_source_records(self):
        exchange = load()
        initial = exchange["initial"]
        changes = exchange["changes"]
        self.assertNotIn("/permits/other.xml", initial)
        events = changes[0]["routes"]["/site/handover"]["body"]["events"]
        self.assertTrue(any(e["type"] == "incoming-check-in" for e in events))
        self.assertFalse(any(e["type"] == "clearance" for e in events))
        self.assertEqual(changes[1]["routes"]["/site/handover"]["body"]["events"][0]["signed"], "S-72")

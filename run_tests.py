import yaml
import pytest

def load_test_plan():
    with open('test_plan.yaml', 'r') as file:
        test_plan = yaml.safe_load(file)
    return test_plan['test_plan']

if __name__ == "__main__":
    test_plan = load_test_plan()
    for item in test_plan:
        test_file = item['test']
        devices = item['devices']
        for device in devices:
            pytest.main(['--device', device, test_file])

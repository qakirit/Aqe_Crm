import yaml
import os


def load_env_config():
    base_path = os.path.join(os.path.dirname(__file__), '..', 'configuration')

    # Load environment name from env.yaml
    with open(os.path.join(base_path, 'env.yaml')) as env_file:
        env_name = yaml.safe_load(env_file)["env"]

    # Load config from that environment file
    with open(os.path.join(base_path, f"{env_name}.yaml")) as config_file:
        return yaml.safe_load(config_file)

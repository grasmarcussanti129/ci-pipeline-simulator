import json
import time

class CIpipeline:
    def __init__(self, config_file):
        self.config_file = config_file
        self.load_config()

    def load_config(self):
        with open(self.config_file) as f:
            self.config = json.load(f)

    def build(self):
        print('Starting build process...')
        time.sleep(2)
        print('Build completed!')

    def test(self):
        print('Running tests...')
        time.sleep(2)
        print('All tests passed!')

    def deploy(self):
        print('Deploying to staging...')
        time.sleep(2)
        print('Deployment successful!')

    def run_pipeline(self):
        self.build()
        self.test()
        self.deploy()

if __name__ == '__main__':
    pipeline = CIpipeline('config.json')
    pipeline.run_pipeline()

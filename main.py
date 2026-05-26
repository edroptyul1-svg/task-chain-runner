#!/usr/bin/env python3
"""Chain multiple tasks together with automatic data passing between steps"""

class App:
    def __init__(self):
        self.config = {}
    
    def run(self):
        print("Running task-chain-runner...")
        return True

if __name__ == "__main__":
    app = App()
    app.run()

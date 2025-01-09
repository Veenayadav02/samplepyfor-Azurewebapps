import time

def run():
    while True:
        print("WebJob is running in the background!")
        time.sleep(10)  # Sleep for 10 seconds to simulate background task

if __name__ == "__main__":
    run()

from tqdm import tqdm
from threading import Thread
import itertools
import time


def run_with_progress(func, description, *args, **kwargs):
    """
    display a progress bar.
    
    """

    result = {}

    def worker():
        result["value"] = func(*args, **kwargs)

    thread = Thread(target=worker)
    thread.start()

    with tqdm(
        total=100,
        desc=description,
        bar_format="{l_bar}{bar}| {percentage:3.0f}%"
    ) as pbar:

        for _ in itertools.cycle(range(100)):
            if not thread.is_alive():
                break

            if pbar.n < 95:
                pbar.update(1)

            time.sleep(0.08)

        pbar.n = 100
        pbar.refresh()

    thread.join()

    return result["value"]
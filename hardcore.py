import math
import time
import multiprocessing

# Funkce pro výpočet Fibonacciho čísla (intenzivní výpočet)
def compute_fibonacci(n):
    if n <= 1:
        return n
    return compute_fibonacci(n-1) + compute_fibonacci(n-2)

def cpu_intensive_task():
    start_time = time.time()
    processes = []
    num_processes = multiprocessing.cpu_count() * 2  # Vytvoříme dvojnásobek procesů oproti počtu jader

    # Opakovaný intenzivní výpočet
    for _ in range(5):  # Počet opakování, aby se CPU déle zatížilo
        # Vytvoříme procesy
        for _ in range(num_processes):
            p = multiprocessing.Process(target=compute_fibonacci, args=(35,))  # Zvýšení složitosti na 35
            processes.append(p)
            p.start()

        # Počkáme, až všechny procesy dokončí výpočet
        for p in processes:
            p.join()

    end_time = time.time()
    print(f"CPU výpočet trval: {end_time - start_time:.2f} sekund")

if __name__ == "__main__":
    cpu_intensive_task()

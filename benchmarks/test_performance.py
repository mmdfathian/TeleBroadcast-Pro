import time
import statistics
import logging

# Setup basic logging for benchmark results
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def run_benchmark(task_name, func, *args, iterations=100):
    """
    Executes a function multiple times and calculates performance metrics.
    """
    logger.info(f"--- Running Benchmark: {task_name} ({iterations} iterations) ---")
    
    execution_times = []
    
    for _ in range(iterations):
        start = time.perf_counter()
        func(*args)
        end = time.perf_counter()
        execution_times.append(end - start)
    
    metrics = {
        "average": statistics.mean(execution_times),
        "min": min(execution_times),
        "max": max(execution_times),
        "stdev": statistics.stdev(execution_times) if iterations > 1 else 0
    }
    
    logger.info(f"Result: Avg: {metrics['average']:.6f}s | Min: {metrics['min']:.6f}s | Max: {metrics['max']:.6f}s")
    logger.info("-" * 50)
    return metrics

# --- Mock functions to simulate TeleBroadcast-Pro tasks ---

def simulate_message_formatting(user_count):
    """Simulates the time taken to format messages for a list of users."""
    return [f"Hello User {i}, this is a broadcast!" for i in range(user_count)]

def simulate_session_loading(session_count):
    """Simulates loading multiple Telethon session files."""
    # Simulating a small delay for I/O operations
    time.sleep(0.01) 
    return [f"session_{i}.session" for i in range(session_count)]

if __name__ == "__main__":
    print("\n🚀 Starting TeleBroadcast-Pro Performance Analysis\n")
    
    # Benchmark 1: Formatting 5,000 messages
    run_benchmark("Message Formatting (5k)", simulate_message_formatting, 5000)
    
    # Benchmark 2: Simulating 20 Session Loads
    run_benchmark("Session Prep (20 sessions)", simulate_session_loading, 20, iterations=10)

    print("\n✅ Benchmarking Complete.")

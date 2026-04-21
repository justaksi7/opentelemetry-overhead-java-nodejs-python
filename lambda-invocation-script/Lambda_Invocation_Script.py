import asyncio
import aioboto3
import json
import time

LAMBDA_NAME = "arn:aws:lambda:eu-central-1:arn*"
TOTAL_INVOCATIONS = 1200
MAX_CONCURRENCY = 200

payload_bytes = json.dumps({"test": "benchmark"}).encode("utf-8")

async def worker(client, queue, semaphore):
    while not queue.empty():
        idx = await queue.get()
        async with semaphore:
            try:
                await client.invoke(
                    FunctionName=LAMBDA_NAME,
                    InvocationType="Event",
                    Payload=payload_bytes,
                )
            except Exception as e:
                print(f"Fehler bei {idx}: {e}")
            finally:
                queue.task_done()

async def main():
    semaphore = asyncio.Semaphore(MAX_CONCURRENCY)
    queue = asyncio.Queue()
    
    for i in range(TOTAL_INVOCATIONS):
        queue.put_nowait(i)

    session = aioboto3.Session()
    
    start_time = time.perf_counter()
    
    # Nur ein Client für alle Aufrufe 
    async with session.client("lambda", region_name="eu-central-1") as client:
        workers = [
            asyncio.create_task(worker(client, queue, semaphore))
            for _ in range(MAX_CONCURRENCY)
        ]
        
        await queue.join() 
        for w in workers:
            w.cancel()

    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"--- FERTIG ---")
    print(f"{TOTAL_INVOCATIONS} Aufrufe in {duration:.2f} Sekunden gesendet.")
    print(f"Rate: {TOTAL_INVOCATIONS / duration:.2f} Aufrufe/Sekunde")

if __name__ == "__main__":
    asyncio.run(main())

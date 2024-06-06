import asyncio,time

async def producer(queue,n):
    for i in range(n):
        task = f"task-{i}"
        await queue.put(task)
        print(f"Produced {task}",time.time())
        await asyncio.sleep(0.1)

async def worker(queue,worker_id):
    while True:
        task=await queue.get()
        if not task:
            break
        print(f"Worker-{worker_id} processing {task}")
        await asyncio.sleep(1)
        print(f"Worker-{worker_id} completed {task}")
        queue.task_done()


async def main():
    queue=asyncio.Queue()
    num_tasks=10
    num_workers=3

    producer_coroutine=producer(queue,num_tasks)
    worker_coroutine_list=[worker(queue,i) for i in range(num_workers)]
    await asyncio.gather(producer_coroutine,*worker_coroutine_list)
    await queue.join()
    await asyncio.gather(*worker_coroutine_list)

if __name__ == "__main__":
    asyncio.run(main())



import asyncio

async def fool():
    print("fool111")
    await autudo()
    print("fool222")
    await asyncio.sleep(2)
    print("fool333")

autudoa=0
async def autudo():
    global autudoa
    print(f"autodo={autudoa}")
    autudoa += 1

async def fool2():
    await autudo()
    print("2fool111")
    await asyncio.sleep(2)
    print("2fool222")

async def main():
    await asyncio.gather(fool(), fool2())

def demo():
    asyncio.run(main())

if __name__ == '__main__':
    demo()

# fool111
# autodo=0
# fool222
# autodo=1
# 2fool111
# fool333
# 2fool222
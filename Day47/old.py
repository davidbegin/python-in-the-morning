print("\033c")

import asyncio

async def api_call1(req):
    print("API Call 1")
    # yield

async def api_call2(req):
    print("API Call 2")
    # yield

async def api_call3(req):
    print("API Call 3")
    # yield



def step1(req):
    print("Step 1")

def step2(req):
    print("STep 2")

def step3(req):
    print("STep 3")

# @asyncio.coroutine
def old_three_stages(request1):
    # response1 = yield from api_call1(request1)
    # TypeError: 'NoneType' object is not iterable
    response1 = yield from api_call1(request1)
    # stage 1
    request2 = step1(response1)
    response2 = yield from api_call2(request2)
    # stage 2
    request3 = step2(response2)
    response3 = yield from api_call3(request3)

    # stage 3
    step3(response3)

# TypeError: object generator can't be used in 'await' expression
async def three_stages(request1):
    response1 = await api_call1(request1)
    # stage 1
    request2 = step1(response1)
    response2 = await api_call2(request2)
    # stage 2
    request3 = step2(response2)
    response3 = await api_call3(request3)
    # stage 3
    step3(response3)

loop = asyncio.get_event_loop()

# This could be anything
request1 = "Peace"
loop.create_task(three_stages(request1))
loop.run_forever()




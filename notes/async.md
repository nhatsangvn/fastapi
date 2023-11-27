```
>>> import time
>>>
>>> def q():
...     print("Why can't programmers tell jokes?")
...     time.sleep(3)
...
>>> def a():
...     print("Timing!")
...
>>> def main():
...     q()
...     a()
...
>>> main()
Why can't programmers tell jokes?
<3sec>
Timing!
```

```
>>> import asyncio
>>>
>>> async def q():
...     print("Why can't programmers tell jokes?")
...     await asyncio.sleep(3)
...
>>> async def a():
...     print("Timing!")
...
>>> async def main():
...     await asyncio.gather(q(), a())
...
>>> asyncio.run(main())
Why can't programmers tell jokes?
Timing!
```

Python thinks:
    Execute q(). Well, just the first line right now.
    Okay, you lazy async q(), I’ve set my stopwatch and I’ll come back to you in three seconds.
    In the meantime I’ll run a(), printing the answer right away.
    No other await, so back to q().
    Boring event loop! I’ll sit here aaaand stare for the rest of the three seconds.
    Okay, now I’m done.

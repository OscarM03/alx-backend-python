<h1 style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 36px;">Python - Async</h1>
<h2 style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 30px;">Learning Objectives</h2>
<p style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">At the end of this project, you are expected to be able to <a href="https://intranet.alxswe.com/rltoken/RzzuxS2J7-SysSxP0Hu3cA" title="explain to anyone" target="_blank" style="color: transparent;">explain to anyone</a>, <strong><strong>without the help of Google</strong></strong>:</p>
<ul style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <li><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">async</code> and <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">await</code> syntax</li>
    <li>How to execute an async program with <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">asyncio</code></li>
    <li>How to run concurrent coroutines</li>
    <li>How to create <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">asyncio</code> tasks</li>
    <li>How to use the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">random</code> module</li>
</ul>
<h2 style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 30px;">Tasks</h2>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">0. The basics of async</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <p>Write an asynchronous coroutine that takes in an integer argument (<code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">max_delay</code>, with a default value of 10) named <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">wait_random</code> that waits for a random delay between 0 and <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">max_delay</code> (included and float value) seconds and eventually returns it.</p>
            <p>Use the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">random</code> module.</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

wait_random = __import__(&apos;0-basic_async_syntax&apos;).wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))

bob@dylan:~$ ./0-main.py
9.034261504534394
1.6216525464615306
10.634589756751769
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-python</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x01-python_async_function</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0-basic_async_syntax.py</code></li>
                </ul>
            </div>
        </div>
        <div style="color: rgb(245, 245, 245);background-color: rgb(245, 245, 245);border-top: 0px solid rgb(221, 221, 221);">
            <div>
                <div><button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">&nbsp;Done?</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Get a sandbox</button></div>
                <div style="font-size: 1.5rem !important;"><br></div>
            </div>
        </div>
    </div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">1. Let&apos;s execute multiple coroutines at the same time with async</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <p>Import <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">wait_random</code> from the previous python file that you&rsquo;ve written and write an async routine called <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">wait_n</code> that takes in 2 int arguments (in this order): <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">n</code> and <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">max_delay</code>. You will spawn <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">wait_random</code> <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">n</code> times with the specified <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">max_delay</code>.</p>
            <p><code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">wait_n</code> should return the list of all the delays (float values). The list of the delays should be in ascending order without using <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">sort()</code> because of concurrency.</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3
&apos;&apos;&apos;
Test file for printing the correct output of the wait_n coroutine
&apos;&apos;&apos;
import asyncio

wait_n = __import__(&apos;1-concurrent_coroutines&apos;).wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))

bob@dylan:~$ ./1-main.py
[0.9693881173832269, 1.0264573845731002, 1.7992690129519855, 3.641373003434587, 4.500011569340617]
[0.07256214141415429, 1.518551245602588, 3.355762808432721, 3.7032593997182923, 3.7796178143655546, 4.744537840582318, 5.50781365463315, 5.758942587637626, 6.109707751654879, 6.831351588271327]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
</code></pre>
            <p>The output for your answers might look a little different and that&rsquo;s okay.</p>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-python</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x01-python_async_function</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">1-concurrent_coroutines.py</code></li>
                </ul>
            </div>
        </div>
        <div style="color: rgb(245, 245, 245);background-color: rgb(245, 245, 245);border-top: 0px solid rgb(221, 221, 221);">
            <div>
                <div><button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">&nbsp;Done?</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Get a sandbox</button></div>
                <div style="font-size: 1.5rem !important;"><br></div>
            </div>
        </div>
    </div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">2. Measure the runtime</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <p>From the previous file, import <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">wait_n</code> into <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">2-measure_runtime.py</code>.</p>
            <p>Create a <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">measure_time</code> function with integers <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">n</code> and <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">max_delay</code> as arguments that measures the total execution time for <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">wait_n(n, max_delay)</code>, and returns <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">total_time / n</code>. Your function should return a float.</p>
            <p>Use the <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">time</code> module to measure an approximate elapsed time.</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

measure_time = __import__(&apos;2-measure_runtime&apos;).measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))

bob@dylan:~$ ./2-main.py
1.759705400466919
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-python</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x01-python_async_function</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">2-measure_runtime.py</code></li>
                </ul>
            </div>
        </div>
        <div style="color: rgb(245, 245, 245);background-color: rgb(245, 245, 245);border-top: 0px solid rgb(221, 221, 221);">
            <div>
                <div><button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">&nbsp;Done?</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Get a sandbox</button></div>
                <div style="font-size: 1.5rem !important;"><br></div>
            </div>
        </div>
    </div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">3. Tasks</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <p>Import <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">wait_random</code> from <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0-basic_async_syntax</code>.</p>
            <p>Write a function (do not create an async function, use the regular function syntax to do this) <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">task_wait_random</code> that takes an integer <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">max_delay</code> and returns a <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">asyncio.Task</code>.</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ cat 3-main.py
#!/usr/bin/env python3

import asyncio

task_wait_random = __import__(&apos;3-tasks&apos;).task_wait_random


async def test(max_delay: int) -&gt; float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))

bob@dylan:~$ ./3-main.py
&lt;class &apos;_asyncio.Task&apos;&gt;
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-python</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x01-python_async_function</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">3-tasks.py</code></li>
                </ul>
            </div>
        </div>
        <div style="color: rgb(245, 245, 245);background-color: rgb(245, 245, 245);border-top: 0px solid rgb(221, 221, 221);">
            <div>
                <div><button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">&nbsp;Done?</button> <button style="text-align: center;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 12px;border: 1px solid rgb(204, 204, 204);">Get a sandbox</button></div>
                <div style="font-size: 1.5rem !important;"><br></div>
            </div>
        </div>
    </div>
</div>
<div style="text-align: start;color: rgb(51, 51, 51);background-color: rgb(255, 255, 255);font-size: 14px;">
    <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);border: 1px solid rgb(221, 221, 221);">
        <div style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);border-bottom: 1px solid rgb(221, 221, 221);">
            <h3 style="color: rgb(51, 51, 51);font-size: 16px;">4. Tasks</h3>
            <div><strong><span style="text-align: center;color: rgb(255, 255, 255);background-color: rgb(152, 163, 174);font-size: 10.5px;">mandatory</span></strong></div>
        </div>
        <div>
            <p>Take the code from <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">wait_n</code> and alter it into a new function <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">task_wait_n</code>. The code is nearly identical to <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">wait_n</code> except <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">task_wait_random</code> is being called.</p>
            <pre style="color: rgb(51, 51, 51);background-color: rgb(245, 245, 245);font-size: 13px;border: 1px solid rgb(204, 204, 204);"><code style="color: inherit;font-size: inherit;">bob@dylan:~$ cat 4-main.py
#!/usr/bin/env python3

import asyncio

task_wait_n = __import__(&apos;4-tasks&apos;).task_wait_n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))

bob@dylan:~$ ./4-main.py
[0.2261658205652346, 1.1942770588220557, 1.8410422186086628, 2.1457353803430523, 4.002505454641153]
</code></pre>
        </div>
        <div>
            <div style="color: rgb(255, 255, 255);background-color: rgb(255, 255, 255);">
                <p><strong><strong>Repo:</strong></strong></p>
                <ul>
                    <li>GitHub repository: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">alx-backend-python</code></li>
                    <li>Directory: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">0x01-python_async_function</code></li>
                    <li>File: <code style="color: rgb(199, 37, 78);background-color: rgb(249, 242, 244);font-size: 12.6px;">4-tasks.py</code></li>
                </ul>
            </div>
        </div>
    </div>
</div>
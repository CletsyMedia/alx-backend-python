
<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/RzzuxS2J7-SysSxP0Hu3cA" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<ul>
<li><code>async</code> and <code>await</code> syntax</li>
<li>How to execute an async program with <code>asyncio</code></li>
<li>How to run concurrent coroutines</li>
<li>How to create <code>asyncio</code> tasks</li>
<li>How to use the <code>random</code> module</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>python3</code> (version 3.7)</li>
<li>All your files should end with a new line</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.5.x)</li>
<li>All your functions and coroutines must be type-annotated.</li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your functions should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code></li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>

  </div>
</div>


      

      

        
          <h2 class="gap">Tasks</h2>

    <div data-role="task11625" data-position="1" id="task-num-0">
      <div class="panel panel-default task-card " id="task-11625">
  <span id="user_id" data-id="422289"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. The basics of async
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="422289"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write an asynchronous coroutine that takes in an integer argument (<code>max_delay</code>, with a default value of 10) named <code>wait_random</code> that waits for a random delay between 0 and <code>max_delay</code> (included and float value) seconds and eventually returns it.</p>

<p>Use the <code>random</code> module.</p>

<pre><code>bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

wait_random = __import__(&#39;0-basic_async_syntax&#39;).wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))

bob@dylan:~$ ./0-main.py
9.034261504534394
1.6216525464615306
10.634589756751769
</code></pre>

  </div>

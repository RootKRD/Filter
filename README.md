# URL to fetch and Filter 'uFilter' :fire:

#Install & Set :
<pre class="notranslate"><code>git clone https://github.com/RootKRD/Filter
cd Filter
python uFilter.py
</code></pre>

# Usage : 

```
python uFilter.py -h
python uFilter.py https://example.com -txt
python uFilter.py https://example.com -txt -js -json
```


https://user-images.githubusercontent.com/109300095/231968508-d8e1c7c2-3f10-4109-9f5e-520919f5bc8c.mp4

<div class="highlight highlight-source-kotlin notranslate position-relative overflow-auto" dir="auto" data-snippet-clipboard-copy-content="fun getAppData(): AppData {
    val data = &quot;&lt;your encoded server info&gt;&quot;
    val text = decode(data)
    return Gson().fromJson(text, AppData::class.java)
}"><pre><span class="pl-k">fun</span> <span class="pl-en">getAppData</span>(): <span class="pl-en">AppData</span> {
    <span class="pl-k">val</span> data <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">"</span>&lt;your encoded server info&gt;<span class="pl-pds">"</span></span>
    <span class="pl-k">val</span> text <span class="pl-k">=</span> decode(data)
    <span class="pl-k">return</span> <span class="pl-en">Gson</span>().fromJson(text, <span class="pl-en">AppData</span>::<span class="pl-c1">class</span>.java)
}</pre></div>

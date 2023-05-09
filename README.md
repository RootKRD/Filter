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
}"><pre>

# -*- coding:utf-8 -*-
import re
html = """
    <li><a href="http://www.meizitu.com/a/5575.html"  alt="短发女孩真的很可爱，君是不是有" width="64" height="64"></a></li>
    <li><a href="http://www.meizitu.com/a/5567.html"  alt="扶我起来！看到这些妹纸，你都会" width="64" height="64"></a></li>
    <li><a href="http://www.meizitu.com/a/5562.html" alt="保持一颗童心，你永远都那么可爱" width="64" height="64"></a></li>
    <li><a href="http://www.meizitu.com/a/5572.html" alt="简直...不一样的可爱风，刮的你" width="64" height="64"></a></li>
    <li><a href="http://www.meizitu.com/a/5579.html"  alt="颜值又高还拥有这么美的腿，我可" width="64" height="64"></a></li>
    <li><a href="http://www.meizitu.com/a/5578.html"  alt="盘点那些让我们浮想联翩的背影" width="64" height="64"></a></li>
    <li><a href="http://www.meizitu.com/a/5581.html"  alt="能娶到打排球的女孩，简直就是走" width="64" height="64"></a></li>
    <li><a href="http://www.meizitu.com/a/5571.html"  alt="我只想说，有酒窝的妹纸真可爱" width="64" height="64"></a></li>
    <li><a href="http://www.meizitu.com/a/5565.html"  alt="妹子即便你不带我去哪，默默跟在" width="64" height="64"></a></li>
    <li><a href="http://www.meizitu.com/a/5580.html" alt="这些完美翘臀真让人垂涎欲滴" width="64" height="64"></a></li>
    <li><a href="http://www.meizitu.com/a/5573.html" alt="周末福利图，个个身材都超赞" width="64" height="64"></a></li>
    
                </ul>
    
                </div>"""
partter = re.findall('<li.*?href="(.*?)".*?alt="(.*?)">(.*?)</a>',html,re.S)
results = re.compile(partter,html)
print(results)
for result in results:
    print(result)

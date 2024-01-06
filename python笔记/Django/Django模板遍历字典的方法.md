使用Python + [Django](https://so.csdn.net/so/search?q=Django&spm=1001.2101.3001.7020)做Web开发时，有时需要在view中传递一个字典给模板(template),如何在模板中遍历字典呢？

下面介绍两种方法：

  views.py代码如下：

```python
    dicts = {"key1": 1, "key2": 2, "key3": 3, }      
    return render_to_response("index.html",{"dicts":dicts,},context_instance = RequestContext(request))  
```



#### 1.第一种遍历方法：

 

  index.html代码如下：

```html
{% for key,value in dicts.items %}    
    <tr class="{% cycle 'altrow' '' %}">                  
        <td>{{ forloop.counter }}</td>                
        <td>{{ key }}</td> 
        <td>{{ value }}</td>              
    </tr>           
{% endfor %}
```


 这种方法遍历字典，简单明了，但由于字典是无序的， 不能满足特定的要求，如：首先输出key2,在输出key1，key3。要做到这点就需要使用第二种方法。



#### 2、第二种使用自定义过滤器

 

  1）:首先自定义过滤器：

   在***\*Django\****的app包的合适位置创建一个templatetags包，它应该和models.py，views.py等在同一级，例如:

   polls/ 
    models.py 
    templatetags/ 
    views.py 

  

   添加两个文件到templatetags包（即该目录下），一个__init__.py文件(来告诉***\*Python\****这是一个包含Python代码的模块)和一个包含你的自定义的标签/过滤器定义的文件，后者的文件名是你将在后面用来载入标签的名字，例如，如果你的自定义标签或者过滤器在一个叫myfilter.py文件里，你可以在模板里做下面的事情:
   myfilter.py代码如下：

```python
from django import template    
register = template.Library()    
def key(d,key_name):          
    value = 0          
    try:                
        value = d[key_name]        
     except KeyError:                
            value = 0        
     return value
```


模板index.html代码如下：

```python
<tr class="altrow">             
<td>1</td>                
<td>key2</td>             
<td>{{ dicts|key:"key2" }}    
</td>           
</tr>       
<tr>              
<td>2</td>                
<td>key1</td>             
<td>{{ dicts|key:"key1" }}    
</td>                  
</tr>        
<tr class="altrow">              
<td>3</td>              
<td>key3</td>            
<td>{{ dicts|key:"key3" }}</td>         
</tr>
```
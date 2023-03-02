### Q查询

大于、大于等于、小于、小于等于

```python
Student.objects.filter(age__gt=10)#查询年龄大于10岁的学生
Student.objects.filter(age__gte=10)#大于等于
```

不等于、不包含于

```python
Student.object.filter().excute(age=10)
Student.objects.filter().execute(age__in=[10,20])
```


1、查询某列数据重复的个数

以某列分组排列

```sql
select md5sum ,count(*) as a from DaglPerson GROUP BY md5sum ORDER BY a ;
```


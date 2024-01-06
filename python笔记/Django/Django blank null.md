HOSPITALNO = models.CharField('医院代码', max_length=20) 可以传递空字符串吗？blank=True null=True  有什么区别？



ChatGPT

ChatGPT

在 Django 模型中，`CharField` 的 `blank` 和 `null` 参数都用于指定字段是否允许为空，但它们有着不同的作用：

1. **`blank=True`：** 这个参数告诉 Django 表单验证系统该字段允许为空白值（空字符串 `''` 或空格）。对于数据库字段，`blank=True` 不会影响数据库中字段是否允许为 `NULL`，而只会影响 Django 表单的验证。如果在表单中输入了空白值，不会引发 ValidationError 错误。
2. **`null=True`：** 这个参数告诉数据库该字段允许存储 `NULL` 值。对于数据库字段，`null=True` 允许该字段为空。如果您使用数据库的迁移功能（migrations），这将在数据库层面将该字段设置为可以存储空值。

如果您的模型字段设置为 `HOSPITALNO = models.CharField('医院代码', max_length=20, blank=True, null=True)`：

- `blank=True`：在 Django 表单验证时允许空白值（`''` 或空格）。
- `null=True`：在数据库层面允许存储 `NULL` 值，即允许该字段为空。

因此，如果您想要在数据库中允许存储空字符串 `''`，同时在 Django 表单验证时也允许空白值，可以使用 `HOSPITALNO = models.CharField('医院代码', max_length=20, blank=True, null=True)` 这样的设置。
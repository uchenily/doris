```sql
CREATE TABLE IF NOT EXISTS example_table (
    id INT NOT NULL,
    name VARCHAR(50),
    age INT
)
DUPLICATE KEY(id)
DISTRIBUTED BY HASH(id) BUCKETS 1
PROPERTIES (
    "replication_num" = "1"
);


```sql
INSERT INTO example_table (id, name, age) VALUES
(1, 'Alice', 33),
(2, 'Bob', 44),
(3, 'Charlie', 55);
```

安装指定版本的protoc

```shell
pip install protobuf==6.31.1
```

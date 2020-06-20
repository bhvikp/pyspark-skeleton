# pyspark-skeleton
Skeleton for PySpark Application

### Installation
Build dependencies files.
```sh
make build
```

### Submit spark application
```s
cd dist/
spark-submit --master local --py-files dependencies.zip Main.py
```

###Thank You :)
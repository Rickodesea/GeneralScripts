# CEnumToString.py
This script converts a C enum source to string.

For example:
[input]
```text
enum {
	id_main,
	id_sub,
	id_add,
	id_mul,
	id_div
};
```



```
[console]
```bash
python3 CEnumToString.py
```

[output]
```C
const char * getidstring(unsigned int id) {
	switch(id) {
		case id_main: return "main";
		case id_sub: return "sub";
		case id_add: return "add";
		case id_mul: return "mul";
		case id_div: return "div";
	}
	
	return "--unnamed--";
}
```

If instead of a function, you want an array of strings, then use the flag `--type=array`.
For more details on available flags, and thus more features, call `python CEnumToString.py -h`.

[output: '--type=array']
```C
const char * array [] = {
	"main",
	"sub",
	"add",
	"mul",
	"div"
};
```


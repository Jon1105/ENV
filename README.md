# ENV 
Short script which allows to read 'environment' variables from .`.ini` and `.env` files

### Usage
```
import env

password = env.get_env('PASSWORD', './.env')
```

The second parameter (path) is optional
If it is not provided, the script will search the current directory for and `.ini` or `.env` files

`get_env('Invalid variable name')` will return `None`

** File format of `.env` file from example above:
```
PASSWORD=my_super_secret_password
```
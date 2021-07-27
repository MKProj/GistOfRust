# Program Structure
If you come from langauges like C, C++, Java then a **main** function is very familiar to you, in essence, it's the entry way of our program. Anything that's to be executed, must find it's way into the main function. 

In C++, a simple hello world program will look like this: 
```c++
#include<iostream>
int main(){
    std::cout << "Hello World!" << std::endl; 
}
```
However, in Rust it looks a bit differently: 
```rust
fn main(){
    println!("Hello World");
}
```

First, the main function is declared with `fn main()`, then enclosed in the brackets we see a weird print statement. In other languages, `print` is just another function, such as C's `printf()`, however in Rust, `println!` isn't a function but a macro, and this is symbolized with `!`. We won't go into much detail, but think of it as a smarter way to create code that's to be reused often. 

---
## Importing?

To import something, we use, well the `use` keyword. If we would like to import something from library `foo`, we would do the following: 

```rust
use foo; 
// Or if you want to dive deeper 
// use the :: operator
use foo::Bar; 
//If you would like to namespace something
// use the as keyword
use foo::Bar as B; 
```

We may import something from the standard library by importing from `std`: 
```rust
// src/main.rs
use std::fs; // Stand library file system module
fn main()->Result<(), std::io::Error>{
    //read a file and print it
    let s = fs::read_to_string("test.txt")?;
    println!("{}", s); 
    Ok(())
}
```
No way am I expecting you to understand this program, however it shows you what you'll be able to do in Rust, and that itself should get you excited. So continue to read on, and let's learn how we can get more idiomatic in Rust by understanding the gist of it. 
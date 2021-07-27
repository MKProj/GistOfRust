# What is Cargo?

We talked a little bit about Cargo already, but to review, Cargo is Rust's package manager and is your goto tool to create Rust programs. In Rust we have two different type of projects, `bin` & `lib`, which stand for binary & library respectively. 

- Binary: A program built to be executed, the program is compiled and executed by it's binary file.

- Library: A program built to store various modules, functions, etc. The program is meant to store various components a binary project may use. 

So why don't we create a cargo project? By default it's binary, and for our purposes that's completely fine. 

```bash
# To create a new project use cargo new <project name>
$ cargo new hello_world
     Created binary (application) `hello_world` package
$ cd hello_world # Change directory to hello_world 
$ ls
Cargo.toml src
```

A Cargo package contains the following: 
- Cargo.toml (Used to specify metadata of the project)
- src (Contains all the source code of the project)

Let's take a closer look at the Cargo.toml: 
```toml
[package]
name = "hello_world"
version = "0.1.0"
authors = []
edition = "2018"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
```
Here we can see that it contains information about the package, such as author, version, etc. and dependencies that can be found at [crates.io](https://crates.io), where all Crates can be published to. 

> Note: We will look more at dependencies at later sections once we know more Rust to properly utilize it. 

How about we compile our project? Well there's actually two different ways to do it: `cargo build` & `cargo run`. 
1. `cargo build`: Compiles and creates binary of project 
2. `cargo run`: Compiles and then excecutes binary of project 

Let's first use `cargo build` to see where our project's bianry is compiled to: 

```bash
# Make sure to still be in the hello_world directory
$ cargo build
# Once compiles, we see a target directory created
$ ls 
Cargo.lock Cargo.toml src target
# By default, Cargo compiles in debug mode
# So the binary will be found in target/debug
$ ./target/debug/hello_world
Hello World!
```

If we look at the `src/main.rs` file, we can see that it indeed is a Hello World program: 
```rust
fn main(){
    println!("Hello World");
}
```
In the next section, we will take a closer look at the program structure of a Rust program. 
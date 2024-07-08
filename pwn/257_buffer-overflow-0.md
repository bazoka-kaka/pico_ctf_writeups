# Buffer Overflow 0

## Problem

Let's start off simple, can you overflow the correct buffer? The program is available here. You can view source here. Connect using: nc saturn.picoctf.net 58164

## Solution

the following line in `int main()` is vulnerable to buffer overflow, so we can enter characters more than 100 as total

`gets(buf1); // this is vulnerable`

then pass to `vuln()` function, which is the following

```
void vuln(char *input){
  char buf2[16]; // you just have to enter values more than this total of chars to get the flag
  strcpy(buf2, input); // this is vulnerable
}
```

buf2 could only hold 16 characters, but strcpy is vulnerable to buffer overflow, so buf2 could be replaced with values more than 16 chars (returns sigsegv from the following handler `signal(SIGSEGV, sigsegv_handler);`)

Here's the flag: picoCTF{ov3rfl0ws_ar3nt_that_bad_c5ca6248}

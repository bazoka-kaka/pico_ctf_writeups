# Sleuthkit Intro

https://play.picoctf.org/practice/challenge/301

1.  Download the disk image

    ```
    $ wget [disk_image_url]
    ```

    <img src="../assets/301/301_1.png" />

2.  Unzip the disk image

    ```
    $ gunzip disk.img.gz
    ```

3.  Get the partitions' sizes using <code>mmls</code>

    ```
    $ mmls -a disk.img
    ```

    <img src="../assets/301/301_2.png" />

4.  Start netcat with command <code>nc</code>

    ```
    $ nc saturn.picoctf.net [port]
    ```

    <img src="../assets/301/301_3.png" />

5.  Enter the size
    <img src="../assets/301/301_4.png" />

Another solution:

1. gunzip `gunzip disk.img.gz`
2. show the partitions and sizes `mmls disk.img`
3. enter the size to the instance. Here's the full script

```
#!/usr/bin/bash

echo 202752 | nc saturn.picoctf.net 51031 | grep -oE picoCTF{.*?} --color=none
```

flag: picoCTF{mm15_f7w!}

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

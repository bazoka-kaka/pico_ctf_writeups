# First Find

https://play.picoctf.org/practice/challenge/320

1. Download the file

   ```
   $ wget [file_url]
   ```

   <img src="../assets/320/320_1.png" />

2. Show more information about the file

   ```
   $ file files.zip
   ```

   <img src="../assets/320/320_2.png" />

3. Unzip the file

   ```
   $ unzip files.zip
   ```

   <img src="../assets/320/320_3.png" />

4. Change directory to files using <code>cd</code>

   ```
   $ cd files
   ```

   <img src="../assets/320/320_4.png" />

5. Find the file named 'uber-secret.txt'

   ```
   $ find . -name uber-secret.txt
   ```

   <img src="../assets/320/320_5.png" />

6. Cat uber-secret.txt file location

   ```
   $ cat ./adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
   ```

   <img src="../assets/320/320_6.png" />

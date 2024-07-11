# Redaction Gone Wrong

## Problem

Now you DON’T see me. This report has some critical data in it, some of which have been redacted correctly, while some were not. Can you find an important key that was not redacted properly?

## Solution

we could use some tool called pdftotext to convert pdf to text. the command to translate the pdf to text:

`pdftotext Financial_Report_for_ABC_Labs.pdf text.txt` we then could grab the flag with the command `cat text.txt | grep -oE picoCTF{.*?} --color=none`

Here's the flag: picoCTF{C4n_Y0u_S33_m3_fully}

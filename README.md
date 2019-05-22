
# Creating lists

```console
f@u:~$
f@u:~/yourPATEHtoprogram$ python makelist.py
On.
Off.
```
The input is a download (Unicode-Block_Keilschrift.html) of the Unicode character lists of the website

http://www.unicode.org/charts/normalization


# CSV
The CSV file is ";;" separated. The columns have the following meaning: first column "count", second column "unicodename", third column "unicodenumber" and last column "translit".

# JS array
The program creates two JS / Python arrays. The first one relates the transliteration (key) to the unicode representation (value) and the second relates the unicode representation (key) to the HTML encding of the sign (value).

# Example of array usage

See the website

http://ecomparatio.net/~khk/keil/keili.html

for an example of usage. The website contains a small example conferter between transliteration and HTML cuneiform signes.
